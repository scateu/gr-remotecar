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

#ifndef INCLUDED_REMOTECAR_REMOTECARIIBASEBAND_IMPL_H
#define INCLUDED_REMOTECAR_REMOTECARIIBASEBAND_IMPL_H

#include <remotecar/RemoteCarIIBaseBand.h>

namespace gr {
  namespace remotecar {

    class RemoteCarIIBaseBand_impl : public RemoteCarIIBaseBand
    {
     private:
             double d_samp_rate;
             bool bool_run;

             int n_pre;
             int n_command;

             int current_pre;
             int current_command;

             int current_sample_index;

     public:
      RemoteCarIIBaseBand_impl(double samp_rate,bool run, int command);
      ~RemoteCarIIBaseBand_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
      void set_run(bool run);
      void set_command(int command);
    };
     

  } // namespace remotecar
} // namespace gr

#endif /* INCLUDED_REMOTECAR_REMOTECARIIBASEBAND_IMPL_H */

