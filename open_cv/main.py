from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.list import OneLineAvatarListItem, ImageLeftWidget
import time
import cv2
from kivy.clock import Clock
from kivy.graphics.texture import Texture

Window.size = (700, 700)

Builder.load_file("homescreen.kv")


class Homescreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Initialize OpenCV camera capture
        self.resultbox = self.ids.resultbox
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0)  # Update every 30 fps

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.flip(frame, 0)
            # Convierte la imagen de BGR (OpenCV) a RGB (Kivy)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Crea una textura Kivy desde la imagen
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(frame_rgb.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
            # Actualiza la textura del widget Image
            self.ids.myvideo.texture = texture

    def captureyouface(self):
        # Create timestamp for the image file
        timenow = time.strftime("%Y%m%d_%H%M%S")

        # Export the camera capture to a PNG image
        cv2.imwrite("myimage_{}.png".format(timenow), self.capture.read()[1])
        self.resultbox.add_widget(
            OneLineAvatarListItem(
                ImageLeftWidget(
                    source="myimage_{}.png".format(timenow),
                    size_hint_x=0.3,
                    size_hint_y=1,
                    size=(300, 300)
                ),
            )
        )


class MyApp(MDApp):
    def build(self):
        return Homescreen()


if __name__ == "__main__":
    MyApp().run()
