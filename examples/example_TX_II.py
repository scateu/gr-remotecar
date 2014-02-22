#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Example Tx Ii
# Generated: Sun Feb 23 02:20:02 2014
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import remotecar
import wx

class example_TX_II(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Example Tx Ii")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 8000000
        self.running = running = False
        self.command = command = 10

        ##################################################
        # Blocks
        ##################################################
        self._running_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.running,
        	callback=self.set_running,
        	label='running',
        	true=True,
        	false=False,
        )
        self.Add(self._running_check_box)
        self._command_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.command,
        	callback=self.set_command,
        	label='command',
        	choices=[58,64,28,34,10,22,40,46,52],
        	labels=['<-','->','<^','^>','^','^^','v','v>','<v'],
        	style=wx.RA_HORIZONTAL,
        )
        self.Add(self._command_chooser)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=2e-3,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_FREE,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.remotecar_RemoteCarIIBaseBand_0 = remotecar.RemoteCarIIBaseBand(samp_rate,running, command)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(27.15e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(14, 0)
        self.osmosdr_sink_0.set_if_gain(40, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.remotecar_RemoteCarIIBaseBand_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.remotecar_RemoteCarIIBaseBand_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.remotecar_RemoteCarIIBaseBand_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.osmosdr_sink_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

    def get_running(self):
        return self.running

    def set_running(self, running):
        self.running = running
        self.remotecar_RemoteCarIIBaseBand_0.set_run(self.running)
        self._running_check_box.set_value(self.running)

    def get_command(self):
        return self.command

    def set_command(self, command):
        self.command = command
        self._command_chooser.set_value(self.command)
        self.remotecar_RemoteCarIIBaseBand_0.set_command(self.command)

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = example_TX_II()
    tb.Start(True)
    tb.Wait()

