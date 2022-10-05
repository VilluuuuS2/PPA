from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.image import Image
from kivy.uix.image import Image
from kivy.graphics import *
import webbrowser

Builder.load_file("Inicial.kv")
Builder.load_file("Dicas.kv")
Builder.load_file("Invest.kv")
Builder.load_file("Simule.kv")
Builder.load_file("Relate.kv")

class Dicas(Screen):
    def materia1(self):
        webbrowser.open("https://gestran.com.br/economia-que-ajuda-o-seu-bolso/")
    def materia2(self):
        webbrowser.open("https://acqio.com.br/blog/economia-local-e-sua-importancia/")
    def materia3(self):
        webbrowser.open("https://empreendedores.mercadopago.com.br/maneiras-para-fazer-renda-extra")
    def materia4(self):
        webbrowser.open("https://blog.contaazul.com/orcamento-empresarial")
    pass

class Invest(Screen):
    pass

class Simule(Screen):
    pass

class Relate(Screen):
    pass

class MeuApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Inicial(name='Telainicial'))
        sm.add_widget(Dicas(name='Dicas'))
        sm.add_widget(Invest(name='Invest'))
        sm.add_widget(Simule(name='Simule'))
        sm.add_widget(Relate(name='Relate'))
        return sm

class Inicial(Screen):
    receita = ObjectProperty(None)
    despesa = ObjectProperty(None)
    receite = ObjectProperty(None)
    despese = ObjectProperty(None)
    saldo = ObjectProperty(None)
    def clicou1(self):
        try:
            Receita = float(self.receita.text)
        except ValueError:
            Receita = 0
        try:
            Despesa = float(self.despesa.text)
        except ValueError:
            Despesa = 0
        Receite = float(self.receite.text)
        Despese = float(self.despese.text)
        Saldo = float(self.saldo.text)
        Saldo = Saldo + Receita
        Saldo = Saldo - Despesa
        Receite = Receite + Receita
        Despese = Despese - Despesa
        self.saldo.text = f"{Saldo}"
        self.receite.text = f"{Receite}"
        self.despese.text = f"{Despese}"
        class MeuApp(App):
            def build(self):
                return Dicas()


if __name__ == '__main__':
    MeuApp().run()
