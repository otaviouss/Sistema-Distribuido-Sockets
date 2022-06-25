import kivy

kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class Login(Screen):
    
    def Clicou(self):
        login = self.ids.OK.text
        senha = self.ids.not_OK.text

        if (login != '') and (senha != ''):
            #self.ids.Jovem.text = login + "/" + senha
            return True

        return False


    def VerificarLogin(self, validado):
        if validado:
            self.parent.current = 'telamenu'
        else:
            self.ids.Jovem.text = 'Não deu'



class TelaCadastro(Screen):

    def CadastrarVoucher(self):
        gato = self.ids.gato.text
        titulo = self.ids.titulo.text
        descricao = self.ids.descricao.text
        local = self.ids.local.text
        lanche = self.ids.lanche.text

        if (gato != ''):
            print(gato, titulo, descricao, local, lanche)
            self.parent.current = 'telamenu'

class TelaMenu(Screen):

    def IrParaCadastro(self):
        self.parent.current = 'telacadastro'

    pass

class TestesInApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        manager.add_widget(TelaMenu(name='telamenu'))
        manager.add_widget(TelaCadastro(name='telacadastro'))


        return manager

Meu = TestesInApp()
Meu.run()