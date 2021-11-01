
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
#constructor de la grafic interface, utilitzem un box on posar una label i un button, i les situem en el lloc que volem
        self.box = Gtk.Box(orientation=1, spacing=6)
        self.box.override_background_color(0, Gdk.RGBA(0,0,8,1))
        self.add(self.box)
#per a que es pugui veure correctament la label li posem un markup i la fem mes gran
        self.label1 = Gtk.Label('<span foreground="white" size="x-large">Please, login with your university card</span>')
        self.label1.set_size_request(500,100)
        self.label1.set_use_markup(True)
        self.box.pack_start(self.label1, True, True, 0)
#el button1 al ser clicat executara la funcio on_button1_clicked
        self.button1 = Gtk.Button(label="Clear")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)
#iniciem un nou thread apart per a que executi la funcio scan_uid
        thread = threading.Thread(target=self.scan_uid)
        thread.setDaemon(True)
        thread.start()

    def on_button1_clicked(self, widget):
#quan el button1 es clicat reseteja el fons de la box i la label i executa scan_uid en un thread apart
        self.label1.set_label('<span foreground="white" size="x-large">Please, login with your university card</span>')
        self.box.override_background_color(0, Gdk.RGBA(0,0,8,1))
        
        thread = threading.Thread(target=self.scan_uid)
        thread.start()

    def scan_uid(self):
#la funcio scan uid utilitza la classe RfidACR122U que hem implementat en el puzzle1 per llegir la UID de la tarjeta
#i actualitza el color de la box i la label amb la informacio de la UID
        rf = RfidACR122U()
        uid = rf.read_uid()
        self.label1.set_label('<span foreground="white" size="x-large">UID:'+" "+uid+'</span>')
        self.box.override_background_color(0, Gdk.RGBA(8,0,0,1))

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
        
