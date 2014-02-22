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


#ifndef INCLUDED_REMOTECAR_REMOTECARBASEBAND_H
#define INCLUDED_REMOTECAR_REMOTECARBASEBAND_H

#include <remotecar/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace remotecar {

    /*!
     * \brief <+description of block+>
     * \ingroup remotecar
     *
     */
    class REMOTECAR_API RemoteCarBaseBand : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<RemoteCarBaseBand> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of remotecar::RemoteCarBaseBand.
       *
       * To avoid accidental use of raw pointers, remotecar::RemoteCarBaseBand's
       * constructor is in a private implementation
       * class. remotecar::RemoteCarBaseBand::make is the public interface for
       * creating new instances.
       */
      static sptr make(double samp_rate,double up_down,double left_right);
      virtual void set_up_down(double up_down) = 0;
      virtual void set_left_right(double left_right) = 0 ;
    };

  } // namespace remotecar
} // namespace gr

#endif /* INCLUDED_REMOTECAR_REMOTECARBASEBAND_H */

