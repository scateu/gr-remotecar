/* -*- c++ -*- */
/* 
 * Copyright 2014 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "RemoteCarIIBaseBand_impl.h"

namespace gr {
  namespace remotecar {

    RemoteCarIIBaseBand::sptr
    RemoteCarIIBaseBand::make(double samp_rate,bool run, int command)
    {
      return gnuradio::get_initial_sptr
        (new RemoteCarIIBaseBand_impl(samp_rate, run, command));
    }

    /*
     * The private constructor
     */
    RemoteCarIIBaseBand_impl::RemoteCarIIBaseBand_impl(double samp_rate,bool run, int command)
      : gr::sync_block("RemoteCarIIBaseBand",
              gr::io_signature::make(0,0,0),
              gr::io_signature::make(1,1,sizeof(float)))
    {
        bool_run = run; // output on off
        d_samp_rate = samp_rate; 

        n_command = command; // command code 
        n_pre = 4; // pre pulse number

        current_command = 0;
        current_pre = 0;

        current_sample_index = 0;

    }

    /*
     * Our virtual destructor.
     */
    RemoteCarIIBaseBand_impl::~RemoteCarIIBaseBand_impl()
    {
    }

    int
    RemoteCarIIBaseBand_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        float *out = (float *) output_items[0];

        int pre_length_0 = d_samp_rate * 0.00055 * 3;
        int pre_length_1 = d_samp_rate * 0.00055 * 4;

        int command_length_0 = d_samp_rate * 0.00055 ;
        int command_length_1 = d_samp_rate * 0.00055 * 2 ;

        for (int i = 0;i < noutput_items; i++){
                if (bool_run) {
                        if (current_pre < n_pre) {
                            if (current_sample_index < pre_length_0) {
                                    out[i] = 1;
                                    current_sample_index += 1;
                            }
                            else if (current_sample_index < pre_length_1){
                                    out[i] = 0;
                                    current_sample_index += 1;
                            } else { // a long pre pulse generated.
                                current_sample_index = 0;
                                current_pre += 1;
                            }
                        }
                        else if (current_command < n_command) {
                            // 4 pre long pulse generated, then generate other short pulse.
                            if (current_sample_index < command_length_0 ) {
                                    out[i] = 1;
                                    current_sample_index += 1;
                            }
                            else if (current_sample_index < command_length_1){
                                    out[i] = 0;
                                    current_sample_index += 1;
                            } else { // a short command pulse generated
                                current_sample_index = 0;
                                current_command += 1;
                            }

                        }
                        else {
                                // 1 frame generated
                              current_pre = 0;
                              current_command = 0;
                              current_sample_index = 0;
                        }
                } else { // muted
                        out[i] = 0;
                }

        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

    void RemoteCarIIBaseBand_impl::set_run(bool run) {
            bool_run = run;
    }

    void RemoteCarIIBaseBand_impl::set_command(int command) {
            n_command = command;
    }

  } /* namespace remotecar */
} /* namespace gr */

