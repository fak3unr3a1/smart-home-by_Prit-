##Importing libraries you are going to use
import kivy

## kivy framework inside app folder, in app.py module class App
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button

kivy.require("2.0.0") #kivy version


##the brackets show inheritance
class SmartHomeEntertainment(BoxLayout):
    ##constructor,
    def __init__(self, **kwargs): ##self, passing the object as a parameter so that it can access the variables and methods of the class, **kwargs
        
        ##super() allows you to call methods (usually the __init__ method)
        ##The super(SmartHomeEntertainment, self).__init__(**kwargs) line passes these keyword arguments to the parent class (BoxLayout),
        super(SmartHomeEntertainment, self).__init__(**kwargs)
        
        ##Assining values to the objects attributes
        self.orientation = 'vertical'
             

        # creating a lable for System status
        self.StatusLabel = Label(text="System Status: Off", font_size=24) 
               
        ## add_widget method is from the parent class box layout where we inherited from        
        self.add_widget(self.StatusLabel) #adds the StatusLabel to the SmartHomeEntertainment layout

        # creating a button for TV 
        self.TVbtn = Button(text="Turn TV On", on_press=self.toggle_tv) 
        self.add_widget(self.TVbtn) #adds the TVbtn to the SmartHomeEntertainment layout

        # creating a button for Audio system
        self.AudioBtn = Button(text="Turn Audio On", on_press=self.toggle_audio)
        self.add_widget(self.AudioBtn)#adds the Audio system button to the SmartHomeEntertainment layout

        # Volume
        self.VolLabel = Label(text="Volume: 0%", font_size=18)
        self.add_widget(self.VolLabel)
        
        self.VolSlider = Slider(min=0, max=100, value=0, step=1)
        self.VolSlider.bind(value=self.on_volume_change)
        self.add_widget(self.VolSlider)

        

        # State tracking
        self.TV_ON = False
        self.Audio_ON = False

    #TV
    def toggle_tv(self, instance):
        ##this changes the state of the tv from true to false
        ## so it comes as false the first time, the value is reversed to true
        ## so self.TV_ON = True turns on tv
        
        self.TV_ON = not self.TV_ON
        if self.TV_ON:
            instance.text = "Turn TV Off"
            self.StatusLabel.text = "System Status: TV On"
        else:
            instance.text = "Turn TV On"
            self.StatusLabel.text = "System Status: TV Off"

    #Audio system
    def toggle_audio(self, instance):
        self.Audio_ON = not self.Audio_ON
        if self.Audio_ON:
            instance.text = "Turn Audio Off"
            self.StatusLabel.text = "System Status: Audio On"
        else:
            instance.text = "Turn Audio On"
            self.StatusLabel.text = "System Status: Audio Off"

    def on_volume_change(self, instance, value):
        self.VolLabel.text = f"Volume: {int(value)}%"

##the brackets show inheritance
class SmartSystemApp(App):
    ##runs the root widget to display the application
    def build(self):
        return SmartHomeEntertainment()


if __name__ == "__main__":
    SmartSystemApp().run()
#Features:
#TV Control: Button to toggle the TV on and off.
#Volume Adjustment: Slider to control the volume level, displayed in percentage.
#Audio System: Button to turn the audio system on and off.
#Status Display: Label that shows the current state of the system (TV, media playback, audio).