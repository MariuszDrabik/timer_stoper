from kivy.app import App
from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from datetime import datetime, timedelta
from kivy.config import Config


Builder.load_file("timer.kv")
Config.set('graphics', 'width', '500')


class Timer(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.event = None
        self.count = 0
    count_enable = BooleanProperty(False)
    button_enable = BooleanProperty(False)
    clock_label = StringProperty("0")
    max_slider = NumericProperty(0)
    slider = NumericProperty(0)
    button_text = StringProperty("Start")
    text_input_str = StringProperty("Foo")

    def start_counting(self):
        if self.event and self.count_enable:
            self.count_enable = False
            self.event.cancel()
            self.button_text = 'Start'
        else:
            self.event = Clock.schedule_interval(self.callback_clock, 1)
            self.count_enable = True
            print("Przycisk kliknięty")

    # def on_slider_value(self, widget):
    #     print(f"Slider {int(widget.value)}")

    def on_text_validate(self, widget):
        print('onece', widget.text)
        try:
            self.count = int(widget.text)
            self.max_slider = self.count
            self.slider = self.count
            self.clock_label = str(timedelta(seconds=self.count))
            self.button_enable = True
        except ValueError as e:
            e = 'Liczba panie'
            self.clock_label = e

    def callback_clock(self, dt):
        if self.count == 1:
            self.event.cancel()
            self.button_text = 'Start'
            self.button_enable = False
        self.count = self.count - 1
        self.button_text = 'Pause'
        self.slider = self.count
        self.clock_label = str(timedelta(seconds=self.count))

  


class ClockApp(App):
    
    def build(self):
        self.manager = Timer()
        return self.manager

    # def build(self):
    #     self.myLabel = Label(text='Waiting for updates...')

    #     Clock.schedule_interval(self.Callback_Clock, 1)

    #     return self.myLabel

    # def Callback_Clock(self, dt):
    #     self.count = self.count + 1
    #     self.myLabel.text = "Updated % d...times" % self.count


if __name__ == '__main__':
    ClockApp().run()
