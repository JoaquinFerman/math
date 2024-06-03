from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from operators import *

# declaro una lista que contenera el tamano de X e Y de la pantalla
Wsize = []
cycle = 0

# tamaño X e Y de la pantalla (para android)
ancho =  Window.width
alto = Window.height
Wsize.append(ancho)
Wsize.append(alto)

# tamaño prefijado para pantallas de computadoras (para pruebas)
Wsize = (360, 600)
Window.size = Wsize

# inicia la construccion de la app
class Matapp(MDApp):
    # lista que contendra las propiedades de los widgets
    widgets = ListProperty([])
    def build(self):
        global inicio, Wsize
        # la dispocision va a ser "libre"
        layout = FloatLayout()

        with layout.canvas.before:  #fondo de la app
            Color(rgb=get_color_from_hex('#999999'))
            Rectangle(pos_hint=(0, 0), size=(Wsize[0], Wsize[1]))
        
        user = TextInput(multiline=False, size_hint=(0, 0), pos_hint={'center_x':2, 'center_y':2})

        self.box1 = TextInput(multiline=False, size_hint=(0.8, 0.05), pos_hint={'center_x':0.5, 'center_y':0.9}, hint_text='Conjunto 1')
        self.box2 = TextInput(multiline=False, size_hint=(0.8, 0.05), pos_hint={'center_x':0.5, 'center_y':0.825}, hint_text='Conjunto 2')
        self.box3 = TextInput(multiline=False, size_hint=(0.8, 0.05), pos_hint={'center_x':0.5, 'center_y':0.75}, hint_text='Condicion')
                
        result = Button(
            size_hint=(0.5, 0.05),
            pos_hint={'center_x':0.5, 'center_y':0.675},
            text='Calcular'
        )
        result.bind(on_press=self.operate)

        title = Label(
            text = 'Calculadora de conjuntos',
            pos_hint = {'center_x':0.5, 'center_y':0.95},
            font_size = Wsize[1]/35,
            halign = 'center',
            color = (0, 0, 0, 1)
            )

        # agrego al display los widgets fundamentales para el funcionamiento de la app
        layout.add_widget(user)
        layout.add_widget(result)
        layout.add_widget(title)
        layout.add_widget(self.box1)
        layout.add_widget(self.box2)
        layout.add_widget(self.box3)

        return layout
    
    def operate(self, instance):
        global cycle

        if cycle > 0:
            self.root.remove_widget(self.result_label)
            try:
                self.root.remove_widget(self.symetry)
                self.root.remove_widget(self.relation_label)
                self.root.remove_widget(self.transitivity)
                self.root.remove_widget(self.reflexivity)
            except:
                pass

            cycle -= 1
        
        cycle += 1

        pair_1 = self.box1.text
        pair_2 = self.box2.text

        pair_1 = pair_1.split()
        pair_2 = pair_2.split()

        condition = self.box3.text

        product = pair_product(pair_1, pair_2)

        relation = pair_relation(product, condition)

        results = pair_properties(relation)

        product = self.set_adaptate(product)
        relation = self.set_adaptate(relation)

        self.result_label = Label(
            text = f'P = {product}',
            pos_hint = {'center_x':0.5, 'center_y':0.33},
            font_size = Wsize[1]/35,
            halign = 'center',
            text_size=(Wsize[0], None),
            color = (0, 0, 0, 1)
        )

        try:
            self.relation_label = Label(
                text = f'R = {relation}',
                pos_hint = {'center_x':0.5, 'center_y':0.167},
                font_size = Wsize[1]/35,
                halign = 'center',
                text_size=(Wsize[0], None),
                color = (0, 0, 0, 1)
            )
            self.symetry = Label(
                text = results['symmetry'],
                pos_hint = {'center_x':0.5, 'center_y':0.6},
                font_size = Wsize[1]/35,
                halign = 'center',
                color = (0, 0, 0, 1)
            )
            self.transitivity = Label(
                text = results['transitivity'],
                pos_hint = {'center_x':0.5, 'center_y':0.55},
                font_size = Wsize[1]/35,
                halign = 'center',
                color = (0, 0, 0, 1)
            )
            self.reflexivity = Label(
                text = results['reflexivity'],
                pos_hint = {'center_x':0.5, 'center_y':0.5},
                font_size = Wsize[1]/35,
                halign = 'center',
                color = (0, 0, 0, 1)
            )
            self.root.add_widget(self.symetry)
            self.root.add_widget(self.transitivity)
            self.root.add_widget(self.reflexivity)
            self.root.add_widget(self.relation_label)

        except:
            product = 'Ecuacion no valida'
            pass
        

        self.root.add_widget(self.result_label)

    def set_adaptate(self, set:list):
        output = '{'

        for pair in set:
            output += f'[{pair[0]};{pair[1]}]'
            if set.index(pair) != len(set)-1:
                output += ', '
        
        output += '}'

        return output

#inicia la app
if __name__ == "__main__":
    Matapp().run()