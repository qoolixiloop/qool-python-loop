#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GUI for the graphical number converter
# this should run on the VM, but Mac users may find they do not have GTK

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import numconv_backend as backend

class Ncwin(Gtk.Window):
    """
    Class to draw the UI window of the number converter.
    """

    def __init__(self):
        # This is where all the magic happens.
        # Graphical elements are registered one by one and 
        # connected to their callbacks

        # first initialize a window and set its default size
        Gtk.Window.__init__(self, title="Number Converter")
        self.set_size_request(300, 150)
        # make sure the window doesn't time out
        self.timeout_id = None
        
        # vatiables to send to the backend for processing
        # holds the options of the dropdown menus
        self.from_param = ""
        self.to_param = ""

        # make some boxes to align the elements in the window
        # the layout is very simple, there are just two rows
        # one contains all the fields and the second contains
        # the convert button
        vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        self.add(vbox)

        hbox = Gtk.Box(spacing = 10)
        vbox.pack_start(hbox, True, False, 0)
        
        hbox2 = Gtk.Box(spacing = 10)
        vbox.pack_start(hbox2, True, False, 0)

        # text label
        label1 = Gtk.Label("Convert")
        hbox.pack_start(label1, True, True, 10)

        # text entry field for the number to convert
        self.startn = Gtk.Entry()
        # execute self.on_startn_activate when the enter key is pressed
        # while the number field is in focis
        self.startn.connect("activate", self.on_startn_activate)
        hbox.pack_start(self.startn, True, True, 0)

        # another text label
        label2 = Gtk.Label("from")
        hbox.pack_start(label2, True, True, 0)

        # dropdown menu with supported number bases
        choices = ["Decimal", "Binary", "Octal", "Hexadecimal"]
        fromlist = Gtk.ComboBoxText()
        # execute self.on_fromlist_changed when an option is selected
        fromlist.connect("changed", self.on_fromlist_changed)
        for choice in choices:
            fromlist.append_text(choice)
        fromlist.set_active(0)
        hbox.pack_start(fromlist, True, True, 0)

        # yet another text label
        label3 = Gtk.Label("to")
        hbox.pack_start(label3, True, True, 0)
        
        # second dropdown
        # we reuse the same list of choices  as for the first one
        tolist = Gtk.ComboBoxText()
        # execute self.on_tolist_changed when an option is selected
        tolist.connect("changed", self.on_tolist_changed)
        for choice in choices:
            tolist.append_text(choice)
        # set the starting value to "binary"
        tolist.set_active(1)
        hbox.pack_start(tolist, True, True, 0)

        # last text label
        # now  the whole thing reads:
        # Convert [number] from [base] to [base] = [result]
        label4 = Gtk.Label("=")
        hbox.pack_start(label4, True, True, 0)

        # result field
        # this is a text entry field, but it's set to not be editable
        self.result_field = Gtk.Entry()
        self.result_field.props.editable = False
        hbox.pack_start(self.result_field, True, True, 10)

        # finally, the action button
        act_button = Gtk.Button("Convert!")
        # execute self.on_convert_clicked when the convert button is clicked
        act_button.connect("clicked", self.on_convert_clicked)
        hbox2.pack_start(act_button, True, False, 0)
        hbox2.set_center_widget(act_button)

    # callbacks
    # these should be more or less self-explanatory
    # for each of these, the field that they are connected to is automatically
    # passed as a second parameter to the function

    def on_fromlist_changed(self, combo):
        text = combo.get_active_text()
        self.from_param = text

    def on_tolist_changed(self, combo):
        text = combo.get_active_text()
        self.to_param = text

    def on_startn_activate(self, entry):
        self.from_num = entry.get_text()
        conv = backend.convert(self.from_param, self.to_param, self.from_num)
        self.result_field.set_text(conv)

    def on_convert_clicked(self, button):
        self.from_num = self.startn.get_text()
        conv = backend.convert(self.from_param, self.to_param, self.from_num)
        self.result_field.set_text(conv)

# main function to setup the GUI
def main():
    win = Ncwin()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
