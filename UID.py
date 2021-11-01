
import gi
from main import RfidACR122U
import threading
import time

gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="UID Scanner")

        self.box = Gtk.Box(orientation=1, spacing=6)
        self.box.override_background_color(0, Gdk.RGBA(0,0,8,1))
        self.add(self.box)

        self.label1 = Gtk.Label('<span foreground="white" size="x-large">Please, login with your university card</span>')
        self.label1.set_size_request(500,100)
        self.label1.set_use_markup(True)
        self.box.pack_start(self.label1, True, True, 0)

        self.button1 = Gtk.Button(label="Clear")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        thread = threading.Thread(target=self.scan_uid)
        thread.setDaemon(True)
        thread.start()

    def on_button1_clicked(self, widget):
        self.label1.set_label('<span foreground="white" size="x-large">Please, login with your university card</span>')
        self.box.override_background_color(0, Gdk.RGBA(0,0,8,1))
        
        thread = threading.Thread(target=self.scan_uid)
        thread.start()

    def scan_uid(self):
        rf = RfidACR122U()
        uid = rf.read_uid()
        self.label1.set_label('<span foreground="white" size="x-large">UID:'+" "+uid+'</span>')
        self.box.override_background_color(0, Gdk.RGBA(8,0,0,1))

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
        
