from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.recycleview import RecycleView

# Datos de ejemplo para la lista
initial_data = [{'text': str(x)} for x in range(10)]
class RV(RecycleView):
    data = ListProperty(initial_data)

    def add_item(self):
        new_index = len(self.data)
        self.data.append({'text': str(new_index)})
        self.refresh_from_data()

    def remove_item(self):
        if self.data:
            self.data.pop()
            self.refresh_from_data()

class mainApp(App):
    def build(self):
        return RV()

if __name__ == '__main__':
    mainApp().run()
