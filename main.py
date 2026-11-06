import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# ضبط أبعاد الشاشة لتشبه الهاتف
Window.size = (360, 640)
Window.clearcolor = (0.05, 0.05, 0.05, 1) # تصميم داكن (أسود وفضي)

# الشاشة الرئيسية لبرنامج CRIS TOOLBOX
class HomeScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # الهيدر الاحترافي
        header = Label(
            text="[b]CRIS TOOLBOX[/b]\n[size=12][color=c0c0c0]V1.0 • By CRIS[/color][/size]",
            markup=True,
            font_size='22sp',
            size_hint_y=0.15,
            color=(0.9, 0.9, 0.9, 1)
        )
        main_layout.add_widget(header)
        
        # شبكة الأدوات التسع
        grid = GridLayout(cols=2, spacing=10, size_hint_y=0.85)
        
        tools = [
            "Device Info", "Calculator",
            "Text Tools", "SHA256 Gen",
            "Base64 Tool", "JSON Format",
            "Date & Time", "Network Diag",
            "Password Gen", "Settings"
        ]
        
        for tool_name in tools:
            btn = Button(
                text=tool_name,
                background_normal='',
                background_color=(0.15, 0.15, 0.15, 1),
                color=(0.85, 0.85, 0.85, 1),
                font_size='14sp',
                bold=True
            )
            grid.add_widget(btn)
            
        main_layout.add_widget(grid)
        self.add_widget(main_layout)

class CrisToolboxApp(App):
    def build(self):
        self.title = "CRIS TOOLBOX V1.0"
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        return sm

if name == 'main':
    CrisToolboxApp().run()