import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Gio
import sys
import random


class Output(Gtk.ApplicationWindow):
    def __init__(self):
        # Create window
        Gtk.Window.__init__(self, title="SGen Desktop Generate")
        self.set_default_size(200, 200)
        self.show()

        self.scroller = Gtk.ScrolledWindow ()
        self.output = Gtk.TextView(editable=False)
        self.scroller.add (self.output)
        self.add (self.scroller)

        self.show_all()
       
        global lowercase
        global uppercase
        global numbers
        global special 

        # Determine characters
        characters = ""
        if (lowercase == True):
            characters += "abcdefghijklmnopqrstuvwxyz" 
        if (uppercase == True):
            characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
        if (numbers == True):
            characters += "0123456789" 
        if (special == True):
            characters += "~!@#$%^&*()_-=+<>,.;:{}[]?/"

        generated = ""
        for i in range(amount):
            generated += "".join(random.choice(characters) for i in range(length)) + "\n"

        self.output.get_buffer().set_text(generated)

        
class Main(Gtk.ApplicationWindow):
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
        self.length = Gtk.SpinButton(adjustment=Gtk.Adjustment(10, 1, 32768, 1, 0, 0), value=10, climb_rate=1, digits=0)

        hbox.pack_start(self.length_label, True, True, 0)
        hbox.pack_start(self.length, True, True, 0)
        listbox.add(row)


        # Row 2
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        self.amount_label = Gtk.Label(label="Amount: ")
        self.amount = Gtk.SpinButton(adjustment=Gtk.Adjustment(8, 1, 32768, 1, 0, 0), value=10, climb_rate=1, digits=0)

        hbox.pack_start(self.amount_label, True, True, 0)
        hbox.pack_start(self.amount, True, True, 0)
        listbox.add(row)


        # Row 3
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        self.lowercase = Gtk.CheckButton(label="Lowercase Letters", active=True)
        self.uppercase = Gtk.CheckButton(label="Uppercase Letters", active=True)
        self.numbers = Gtk.CheckButton(label="Numbers", active=True)
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


    def submit(self, submit_button):
        global lowercase
        global uppercase
        global numbers
        global special
        global length
        global amount

        length = int(self.length.get_value())
        amount = int(self.amount.get_value())
        lowercase = self.lowercase.get_active()
        uppercase = self.uppercase.get_active()
        numbers = self.numbers.get_active()
        special = self.special.get_active()

        output_window = Output()

class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = Main(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
