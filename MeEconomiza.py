from turtle import color
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
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import json

Builder.load_file("Inicial.kv")
Builder.load_file("Dicas.kv")
Builder.load_file("Invest.kv")
Builder.load_file("Relate.kv")
Builder.load_file("Grafico.kv")

class Dicas(Screen):
    def materia1(self):
        webbrowser.open("https://gestran.com.br/economia-que-ajuda-o-seu-bolso/")
    def materia2(self):
        webbrowser.open("https://acqio.com.br/blog/economia-local-e-sua-importancia/")
    def materia3(self):
        webbrowser.open("https://empreendedores.mercadopago.com.br/maneiras-para-fazer-renda-extra")
    def materia4(self):
        webbrowser.open("https://blog.nubank.com.br/orcamento-familiar/")
    pass

class Invest(Screen):
    def materia1(self):
        webbrowser.open("https://www.infomoney.com.br/guias/como-comecar-a-investir/")
    def materia2(self):
        webbrowser.open("https://www.uninter.com/noticias/5-areas-para-voce-investir-o-seu-dinheiro-em-2021")
    def materia3(self):
        webbrowser.open("https://blog.abcbrasil.com.br/erros-ao-investir/")
    def materia4(self):
        webbrowser.open("https://blog.abcbrasil.com.br/golpes-financeiros/")
    pass

class Relate(Screen):
    def graficos(self):
        mes=['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
        economia=[150,400,90,50,10,200,60,30,100,0,0,0]
        fig,ax=plt.subplots(figsize=(7,5))
        ax.bar(mes,economia,color=['seagreen', 'darkgreen', 'mediumseagreen'])
        ax.set_title('Valores economizados',fontsize=18)
        plt.show()
    pass

class MeuApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Inicial(name='Telainicial'))
        sm.add_widget(Dicas(name='Dicas'))
        sm.add_widget(Invest(name='Invest'))
        sm.add_widget(Relate(name='Relate'))
        sm.add_widget(Grafico(name='Grafico'))
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

            dado_saldo = self.saldo.text                          # Pega o nome que está digitado na tela
            dado_receite = self.receite.text                  # Pega o telefone que está digitado na tela
            dado_despese = self.despese.text   
            arquivo = open("Gravacao.json", "w")                       # Abre o arquivo para gravação
            dicio = {"saldo1": dado_saldo, "receita1": dado_receite, "despesa1": dado_despese}  # Monta o dicionário na variável `dicio`
            json.dump(dicio, arquivo)                               # Grava o conteúdo da variável `dicio` no arquivo
            arquivo.close() 
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

class Grafico(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        import matplotlib.pyplot as plt
        import matplotlib.colors as mcolors
        mes=['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
        economia=[150,400,90,50,10,200,60,30,100,0,0,0]
        fig,ax=plt.subplots(figsize=(7,5))
        ax.bar(mes,economia,color=['seagreen', 'darkgreen', 'mediumseagreen'])
        ax.set_title('Valores economizados',fontsize=18)
        plt.savefig('graph.png')
        



        # class MeuApp(App):
        #     def build(self):
        #         return Dicas()

        # def __init__(self, **kw):



        #     super().__init__(**kw)
        
        #     try:
        #         arquivo = open("Gravacao.json", "r")           # Abre o arquivo para leitura
        #         dicio = json.load(arquivo)                  # Carrega os dados do arquivo na variável `dicio`
        #         self.saldo.text = dicio["saldo1"]          # Escreve o nome no campo de nome
        #         self.receite.text = dicio["receita1"]  # Escreve o telefone no campo de telefone
        #         self.despese.text = dicio["despesa1"] 
        #     except KeyError:
        #         # Caso tente abrir uma chave que não existe no dicionário
        #         print("===== ERRO: Chave não encontrada. =====")
        #     except json.decoder.JSONDecodeError:
        #         # Caso o arquivo não esteja no formato JSON
        #         print("===== ERRO: O arquivo não está no formato JSON. =====")
        #     except FileNotFoundError:
        #         # Caso o arquivo ainda não tenha sido criado
        #         print("===== ERRO: O arquivo de dados não existe. =====")
        #     else:
        #         # Por último, fecha o arquivo
        #         arquivo.close()


if __name__ == '__main__':
    MeuApp().run()
