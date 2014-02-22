#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Example Tx Ii With Geosson Gui
# Generated: Mon Feb 17 14:43:29 2014
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import remotecar

class example_tx_II_with_geosson_gui(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Example Tx Ii With Geosson Gui")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 8000000

        ##################################################
        # Blocks
        ##################################################
        self.remotecar_RemoteCarIIBaseBand_0 = remotecar.RemoteCarIIBaseBand(samp_rate,True, 99)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(27.15e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(50, 0)
        self.osmosdr_sink_0.set_bb_gain(30, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.remotecar_RemoteCarIIBaseBand_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.remotecar_RemoteCarIIBaseBand_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.osmosdr_sink_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = example_tx_II_with_geosson_gui()
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()

