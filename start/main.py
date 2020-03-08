from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):

    first = 0
    operator = 0
    second = 0

    def build(self):

        main_layout = BoxLayout(orientation="vertical")

        buttons = ['1','2','3','/','4','5','6','*','7','8','9','-','.','0','C','+']

        h_layout = BoxLayout()

        main_layout.add_widget(TextInput(multiline=False,readonly=True))

        for i in range(len(buttons)):

            btn = Button(text = buttons[i],
                        pos_hint = {'center_x':0.5,'center_y':0.5})

            h_layout.add_widget(btn)

            if(i%4 == 3):
                main_layout.add_widget(h_layout)
                h_layout = BoxLayout()

        main_layout.add_widget(Button(text='='))

        return main_layout

    def on_press_button(self):

        numbers = ['0','1','2','3','4','5','6','7','8','9']
        operators = ['/','*','-','+']

        if self.text in numbers:


if __name__ == '__main__':
    app = MainApp()
    app.run()
