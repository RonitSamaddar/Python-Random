import os


# Program to Show how to create a switch  
# import kivy module     
import kivy   
       
# base Class of your App inherits from the App class.     
# app:always refers to the instance of your application    
from kivy.app import App  

  
# Builder is used when .kv file is 
# to be used in .py file 
from kivy.lang import Builder 
  
# The screen manager is a widget 
# dedicated to managing multiple screens for your application. 
from kivy.uix.screenmanager import ScreenManager, Screen

#from android.permissions import request_permissions, Permission  
   
# You can create your kv code in the Python file 
Builder.load_string(""" 
<ScreenOne>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "HELLO! WELCOME TO THE YOLO APP"
            size_hint : 1, 0.75
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1
        Button: 
            text: "OPEN CAMERA"
            size_hint: 1, 0.25 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 0.25 
                root.manager.current = 'screen_two'
<ScreenTwo>:
    BoxLayout:
        orientation: 'vertical'
        ToggleButton:
            text: 'Play'
            size_hint_y: None
            height: '48dp'
        Button: 
            text: "CAPTURE"
            size_hint: 1, 0.25 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.capture()

<ScreenThree>:
    BoxLayout:
        orientation: 'vertical'
        Image:
            source : "IMG.png"
            size_hint: 1, 0.75
        Button: 
            text: "HOME"
            size_hint: 1, 0.25 
            background_color : 1, 0, 0, 1
            text_color : 1, 1, 1, 1 
            on_press: 
                # You can define the duration of the change 
                # and the direction of the slide
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 0.25 
                root.manager.current = 'screen_one'
""") 
   
# Create a class for all screens in which you can include 
# helpful methods specific to that screen 
class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        #camera = self.ids['camera']
        #camera.export_to_png("IMG.png")
        self.manager.transition.direction = 'left' 
        self.manager.transition.duration = 0.25 
        self.manager.current = 'screen_three' 
    pass
class ScreenThree(Screen): 
    pass

   
   
# The ScreenManager controls moving between screens 
screen_manager = ScreenManager() 
   
# Add the screens to the manager and then supply a name 
# that is used to switch screens 
screen_manager.add_widget(ScreenOne(name ="screen_one")) 
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three")) 
  
# Create the App class 
class ScreenApp(App): 
    def build(self):
        #request_permissions([Permission.WRITE_EXTERNAL_STORAGE])
        return screen_manager 
  
# run the app  
sample_app = ScreenApp() 
sample_app.run() 
