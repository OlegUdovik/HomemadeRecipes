from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class RecipesApp(MDApp):
    def build(self):
        return MDLabel(text='Домашние рецепты', halign='center')



RecipesApp().run()


