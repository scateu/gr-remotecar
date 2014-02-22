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
#include "RemoteCarBaseBand_impl.h"

namespace gr {
  namespace remotecar {

    RemoteCarBaseBand::sptr
    RemoteCarBaseBand::make(double samp_rate,double up_down,double left_right)
    {
      return gnuradio::get_initial_sptr
        (new RemoteCarBaseBand_impl(samp_rate, up_down, left_right));
    }

    /*
     * The private constructor
     */
    RemoteCarBaseBand_impl::RemoteCarBaseBand_impl(double samp_rate,double up_down,double left_right)
      : gr::sync_block("RemoteCarBaseBand",
              gr::io_signature::make(0,0, 0),
              gr::io_signature::make(1,1, sizeof(float))),
        d_samp_rate(samp_rate),d_up_down(up_down),d_left_right(left_right)
    {
        n_phase = 0;
    }

    /*
     * Our virtual destructor.
     */
    RemoteCarBaseBand_impl::~RemoteCarBaseBand_impl()
    {
    }

    int
    RemoteCarBaseBand_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        float *out = (float *) output_items[0];

        int n_phase_0 = int(0.000520 * d_samp_rate); //520us
        int n_phase_10 = int(0.000300 * d_samp_rate); //300us
        int n_phase_11 = int(0.0013 * d_samp_rate); // 1.3ms
        int n_phase_2 = int(0.030 * d_samp_rate); // 20ms

        int n_phase_3 = int((n_phase_11 - n_phase_10) * d_up_down + n_phase_10);
        int n_phase_4 = int((n_phase_11 - n_phase_10) * d_left_right + n_phase_10);

        
        /*
                    -->|TIME3  |<--   TIME4
          --------+    +-------+    +-------+    +--------- ... -------+    +---.....
                  |    |       |    |       |    |                     |    |
                  |    |       |    |       |    |                     |    |
                  |    |       |    |       |    |                     |    |
                  |    |       |    |       |    |                     |    |
                  +----+       +----+       +----+                     +----+
                  TIME0              
               -->|                              TIME2                 |<---

        */


        for (int i = 0; i < noutput_items; i++){

            if (n_phase < n_phase_0){
                    out[i] = 0;
            } else if (n_phase < (n_phase_0 + n_phase_3)){
                    out[i] = 1;
            } else if (n_phase < (n_phase_0 + n_phase_3 + n_phase_0)) {
                    out[i] = 0;
            } else if (n_phase < (n_phase_0 + n_phase_3 + n_phase_0 + n_phase_4)){
                    out[i] = 1;
            } else if (n_phase < (n_phase_0 + n_phase_3 + n_phase_0 + n_phase_4 + n_phase_0)){
                    out[i] = 0;
            } else {
                    out[i] = 1;
            }

            n_phase += 1;
            if (n_phase >= n_phase_2) { n_phase = 0;}
        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

    void RemoteCarBaseBand_impl::set_up_down(double up_down){
            d_up_down = up_down;
    }

    void RemoteCarBaseBand_impl::set_left_right(double left_right){
            d_left_right = left_right;
    }

  } /* namespace remotecar */
} /* namespace gr */

