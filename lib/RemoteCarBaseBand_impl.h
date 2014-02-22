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

#ifndef INCLUDED_REMOTECAR_REMOTECARBASEBAND_IMPL_H
#define INCLUDED_REMOTECAR_REMOTECARBASEBAND_IMPL_H

#include <remotecar/RemoteCarBaseBand.h>

namespace gr {
  namespace remotecar {

    class RemoteCarBaseBand_impl : public RemoteCarBaseBand
    {
     private:
       double  d_samp_rate;
       double  d_up_down;
       double  d_left_right;
       int     n_phase;

     public:
      RemoteCarBaseBand_impl(double samp_rate,double up_down,double left_right);
      ~RemoteCarBaseBand_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
      void set_up_down(double up_down);
      void set_left_right(double left_right);
    };

  } // namespace remotecar
} // namespace gr

#endif /* INCLUDED_REMOTECAR_REMOTECARBASEBAND_IMPL_H */

