from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

class ChatScreen(BoxLayout):
    def init(self, **kwargs):
        super(ChatScreen, self).init(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # منطقة عرض الرسائل
        self.scroll = ScrollView(size_hint=(1, 0.85))
        self.chat_history = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.chat_history.bind(minimum_height=self.chat_history.setter('height'))
        self.scroll.add_widget(self.chat_history)
        self.add_widget(self.scroll)

        # منطقة الإرسال
        input_layout = BoxLayout(size_hint=(1, 0.15), spacing=5)
        self.msg_input = TextInput(hint_text='اكتب رسالتك...', multiline=False)
        send_btn = Button(text='إرسال', size_hint=(0.25, 1), background_color=(0.2, 0.6, 1, 1))
        send_btn.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.msg_input)
        input_layout.add_widget(send_btn)
        self.add_widget(input_layout)

    def send_message(self, instance):
        text = self.msg_input.text.strip()
        if text:
            msg_label = Label(
                text=f"أنت: {text}",
                size_hint_y=None,
                height=40,
                color=(1, 1, 1, 1),
                halign='right'
            )
            self.chat_history.add_widget(msg_label)
            self.msg_input.text = ''

class CrisChatApp(App):
    def build(self):
        self.title = 'CRIS CHAT'
        return ChatScreen()

if name == 'main':
    CrisChatApp().run()
