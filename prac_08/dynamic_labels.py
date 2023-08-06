"""
CP1404 Practical 08
dynamic_labels.py
Estimated time: 30 mins
Actual time: 36 mins
"""

from kivy.app import App
from kivy.lang import Builder

class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        "Create labels and add to GUI"
        for name in self.name_to_phone:
            # create a loop for each entry
            label = Label(text=name)
            self.root.ids.entries_box.add_label(label)


DynamicLabelsApp().run()
