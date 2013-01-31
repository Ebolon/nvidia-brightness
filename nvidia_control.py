#!/usr/bin/env python

import gtk
import subprocess


class Scale:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, -1)
        
        adjustment = gtk.Adjustment(0, -100, 100, 1, 1, 0)
        self.scale = gtk.HScale(adjustment)
        self.scale.set_digits(0)
        self.scale.set_update_policy(gtk.UPDATE_CONTINUOUS)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        self.scale.connect("value-changed", self.scale_moved)
        
        window.add(self.scale)
        window.show_all()

    def scale_moved(self, event):
        self.set_brightness(self.scale.get_value())

    def set_brightness(self, value):
        value = str(value / 100).replace('.', ',')
        colors = ['Red', 'Green', 'Blue']
        cmd = ':0[dpy:3]/{}Brightness={}'
        parm = []
        for color in colors:
            parm += ['-a'] + [cmd.format(color, value)]
        subprocess.Popen(["nvidia-settings"] + parm, stdout=subprocess.PIPE)

Scale()
gtk.main()
