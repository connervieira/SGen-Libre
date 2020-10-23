# SGen Libre
# V0LT
# Licensed under the GPLv3
# Version 0.0.5

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Gio
import sys
import random


class GenerationOutput(Gtk.ApplicationWindow):
    def __init__(self):
        # Create window
        Gtk.Window.__init__(self, title="Generation Output")
        self.set_default_size(800, 600)
        self.show()

        self.scroller = Gtk.ScrolledWindow ()
        self.output = Gtk.TextView(editable=False)
        self.output.set_justification(Gtk.Justification.CENTER)
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

        
class AnalysisMenu(Gtk.ApplicationWindow):
    def __init__(self):
        # Create window
        Gtk.Window.__init__(self, title="Analysis Menu")
        self.set_default_size(300, 75)
        self.show()

        listbox = Gtk.ListBox()

        self.add(listbox)
    
        def uniquecharactercount(self):
            unique_character_count_window = UniqueCharacterCount()

        def uniquecharacterslist(self):
            pass

        def characterfrequency(self):
            character_frequency_window = CharacterFrequency()

        def lengthcalculator(self):
            string_length_window = StringLength()

        def probabilitycalculator(self):
            pass

        self.unique_character_count_button = Gtk.Button(label="Unique Character Count")
        self.unique_character_count_button.set_sensitive(True) # Enables button
        self.unique_character_count_button.connect("clicked", uniquecharactercount)
        listbox.add(self.unique_character_count_button)

        self.unique_characters_list_button = Gtk.Button(label="Unique Characters List")
        self.unique_characters_list_button.set_sensitive(False) # Disables button
        self.unique_characters_list_button.connect("clicked", uniquecharacterslist)
        listbox.add(self.unique_characters_list_button)

        self.character_frequency_counter_button = Gtk.Button(label="Character Frequency Counter")
        self.character_frequency_counter_button.set_sensitive(True) # Enables button
        self.character_frequency_counter_button.connect("clicked", characterfrequency)
        listbox.add(self.character_frequency_counter_button)

        self.length_calculator_button = Gtk.Button(label="String Length Calculator")
        self.length_calculator_button.set_sensitive(True) # Enables button
        self.length_calculator_button.connect("clicked", lengthcalculator)
        listbox.add(self.length_calculator_button)

        self.probability_calculator_button = Gtk.Button(label="Probability Calculator")
        self.probability_calculator_button.set_sensitive(False) # Disables button
        self.probability_calculator_button.connect("clicked", probabilitycalculator)
        listbox.add(self.probability_calculator_button)

        self.show_all()

class StringLength(Gtk.ApplicationWindow):
    def __init__(self):
        # Create window 
        Gtk.Window.__init__(self, title="String Length Calculator")
        self.set_default_size(400, 75)
        self.show()
        
        input_field = Gtk.Entry(editable=True)

        def analyze(self):
            global output_content
            string_to_analyze = input_field.get_text()
            output_content = len(string_to_analyze)
            analysis_window = AnalysisOutput()

        listbox = Gtk.ListBox()
        
        listbox.add (input_field)

        self.analyze_button = Gtk.Button(label="Analyze")
        self.analyze_button.connect("clicked", analyze)
        listbox.add(self.analyze_button)

        self.add (listbox)

        self.show_all()


class CharacterFrequency(Gtk.ApplicationWindow):
    def __init__(self):
        # Create window 
        Gtk.Window.__init__(self, title="Character Frequency Analysis")
        self.set_default_size(400, 75)
        self.show()
        
        input_field = Gtk.Entry(editable=True)

        def analyze(self):
            global output_content
            string_to_analyze = input_field.get_text()

            # Count number of times each character appears in the string.
            characters={} # Create an empty dictionary to fill with all of the characters in the string, as well as how many times they appear.
            for i in string_to_analyze:
                characters[i]=characters.get(i,0)+1

            # Display the characters in descending order from most frequent to least frequent.
            seperator_character = " - " # This is the character that will be used to seperate the character from its count in the output.
            output_content = "" # Reset the output content to empty. Without this, the following loop would add on to the last analysis run.
            for j in sorted(characters, key=characters.get, reverse=True):
                output_content = output_content + j + seperator_character + str(characters[j]) + "\n"
            analysis_window = AnalysisOutput()

        listbox = Gtk.ListBox()
        
        listbox.add (input_field)

        self.analyze_button = Gtk.Button(label="Analyze")
        self.analyze_button.connect("clicked", analyze)
        listbox.add(self.analyze_button)

        self.add (listbox)

        self.show_all()


class UniqueCharacterCount(Gtk.ApplicationWindow):
    def __init__(self):
        # Create window 
        Gtk.Window.__init__(self, title="Unique Character Count")
        self.set_default_size(400, 75)
        self.show()
        
        input_field = Gtk.Entry(editable=True)

        def analyze(self):
            global output_content
            string_to_analyze = input_field.get_text()

            # Count number of times each character appears in the string.
            characters={}
            for i in string_to_analyze:
                characters[i]=characters.get(i,0)+1

            output_content = len(characters)
            analysis_window = AnalysisOutput()

        listbox = Gtk.ListBox()
        
        listbox.add (input_field)

        self.analyze_button = Gtk.Button(label="Analyze")
        self.analyze_button.connect("clicked", analyze)
        listbox.add(self.analyze_button)

        self.add (listbox)

        self.show_all()


class AnalysisOutput(Gtk.ApplicationWindow):
    def __init__(self):
        # Create window 
        Gtk.Window.__init__(self, title="Analysis Output")
        self.set_default_size(350, 150)
        self.show()

        global output_content

        self.scroller = Gtk.ScrolledWindow ()
        self.output = Gtk.TextView(editable=False)
        self.output.set_justification(Gtk.Justification.CENTER)
        self.scroller.add (self.output)
        self.add (self.scroller)

        self.output.get_buffer().set_text(str(output_content))

        self.show_all()

 
class Main(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="SGen Libre", application=app)
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

        self.submit_button = Gtk.Button(label="Generate")
        self.submit_button.connect("clicked", self.submit)
        
        hbox.pack_start(self.submit_button, True, True, 0)
        listbox.add(row)


        # Row 5
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        self.analyze_button = Gtk.Button(label="Analysis Menu")
        self.analyze_button.connect("clicked", self.analyze)
        
        hbox.pack_start(self.analyze_button, True, True, 0)
        listbox.add(row)


    def analyze(self, submit_button):
        analysis_menu_window = AnalysisMenu()

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

        output_window = GenerationOutput()

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
