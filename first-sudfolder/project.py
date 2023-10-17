from kivy.app import app

from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class CalculatorApp(App):
    def build(self):
        gl = GridLayout(cols = 4)

        gl.add_widget( Button(text="7") )
        gl.add_widget( Button(text="8") )
        gl.add_widget( Button(text="9") )
        gl.add_widget( Button(text="x") )

        gl.add_widget( Button(text="4") )
        gl.add_widget( Button(text="5") )
        gl.add_widget( Button(text="6") )
        gl.add_widget( Button(text="-") )

        gl.add_widget( Button(text="1") )
        gl.add_widget( Button(text="2") )
        gl.add_widget( Button(text="3") )
        gl.add_widget( Button(text="+") )

        gl.add_widget( Button() )
        gl.add_widget( Button(text="0") )
        gl.add_widget( Button(text=",") )
        gl.add_widget( Button(text="=") )

        return gl

if __name__ == "__maim__":
    CalculatorApp().run()
