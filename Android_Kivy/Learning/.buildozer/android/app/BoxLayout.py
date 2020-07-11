import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=0,orientation='vertical')
        colors = [[1,0,0,1], [0,1,0,1],[0,0,1,1],[0,1,1,1],[1,1,0,1]]
        #each color is defined as [r,g,b,a]

        for i in range(5):
            c=random.choice(colors)
            colors.remove(c)
            btn = Button(text="Button #%s" % (i+1),
                         background_color=c,
                         size_hint=(1,(5-i)/15)
                         )

            layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()