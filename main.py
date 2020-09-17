import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Gio
import sys


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="SGen Desktop", application=app)
        self.set_default_size(250, 50)

        # Prepare the layout
        outer_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(outer_box)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        outer_box.pack_start(listbox, True, True, 0)



        # Create the UI elements
        # Row 1
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        self.length_label = Gtk.Label(label="Length: ")
        self.length = Gtk.SpinButton(value=10, climb_rate=1, digits=0)

        hbox.pack_start(self.length_label, True, True, 0)
        hbox.pack_start(self.length, True, True, 0)
        listbox.add(row)


        # Row 2
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        self.amount_label = Gtk.Label(label="Amount: ")
        self.amount = Gtk.SpinButton(value=10, climb_rate=1, digits=0)

        hbox.pack_start(self.amount_label, True, True, 0)
        hbox.pack_start(self.amount, True, True, 0)
        listbox.add(row)


        # Row 3
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        self.lowercase = Gtk.CheckButton(label="Lowercase Letters")
        self.uppercase = Gtk.CheckButton(label="Uppercase Letters")
        self.numbers = Gtk.CheckButton(label="Numbers")
        self.special = Gtk.CheckButton(label="Special Characters")

        hbox.pack_start(self.lowercase, True, True, 0)
        hbox.pack_start(self.uppercase, True, True, 0)
        hbox.pack_start(self.numbers, True, True, 0)
        hbox.pack_start(self.special, True, True, 0)
        listbox.add(row)
        

        # Row 4
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        self.submit_button = Gtk.Button(label="Submit")
        self.submit_button.connect("clicked", self.submit)

        hbox.pack_start(self.submit_button, True, True, 0)
        listbox.add(row)


        # Row 5
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
    
        self.scroller = Gtk.ScrolledWindow ()
        self.output = Gtk.TextView(editable=False)

        self.scroller.add (self.output)
        hbox.pack_start (self.scroller, fill = True, expand = True, padding = 0)
        listbox.add(row)

    def submit(self, submit_button):
        text = ""
        for i in range (100):
            text += "Test\n"
        self.output.get_buffer().set_text(text)


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
