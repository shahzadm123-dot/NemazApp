from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import csv
import os
from datetime import datetime

Window.clearcolor = (0.1, 0.1, 0.1, 1) # Dark background

class NemazApp(App):
    def build(self):
        self.title = "Nemaz Times Rajjar"

        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # Heading
        heading = Label(
            text='[b]Nemaz Times - Rajjar[/b]',
            markup=True,
            font_size='24sp',
            size_hint_y=None,
            height=50
        )
        main_layout.add_widget(heading)

        # Date input section
        input_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        input_layout.add_widget(Label(text='Date:', size_hint_x=0.2))

        self.date_input = TextInput(
            hint_text='1-31',
            input_filter='int',
            multiline=False,
            size_hint_x=0.3,
            font_size='18sp'
        )
        input_layout.add_widget(self.date_input)
        # Month set karo - abhi May 2026 hai
        self.month = datetime.now().strftime('%b').lower() # may
        month_label = Label(text=f'Month: {self.month.upper()}', size_hint_x=0.5)
        input_layout.add_widget(month_label)

        main_layout.add_widget(input_layout)

        # Button
        btn = Button(
            text='Nemaz Time Dekho', 
            size_hint_y=None, 
            height=60,
            background_color=(0.2, 0.6, 1, 1)
        )
        btn.bind(on_press=self.show_nemaz_time)
        main_layout.add_widget(btn)

        # Output area
        self.result_label = Label(
            text='Output here...',
            size_hint_y=None,
            height=100,
            color=(1, 1, 1, 1)
        )
        main_layout.add_widget(self.result_label)

        return main_layout
    def show_nemaz_time(self, instance):
        try:
            date = self.date_input.text
            if not date:
                self.result_label.text = 'Please enter date!'
                return

            month = self.month
            filename = f'{month}.csv'

            if not os.path.exists(filename):
                self.result_label.text = f'{month.upper()} CSV not found!'
                return

            # Read CSV
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                data = list(reader)

            # Find date
            for row in data:
                if row[0] == date:
                    output = f'[b]{month.upper()} {date} Times[/b]\n'
                    output += f'Fajr: {row[1]}\n'
                    output += f'Sunrise: {row[2]}\n'
                    output += f'Dhurhur: {row[3]}\n'
                    output += f'Asr: {row[4]}\n'
                    output += f'Maghrib: {row[5]}\n'
                    output += f'Isha: {row[6]}'

                    self.result_label.text = output
                    self.result_label.markup = True
                    return

            self.result_label.text = 'Date not found!'

        except Exception as e:
            self.result_label.text = f'Error: {str(e)}'

if __name__ == '__main__':
    NemazApp().run()