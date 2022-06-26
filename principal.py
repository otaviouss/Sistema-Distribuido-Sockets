import kivy

from cliente import Cliente

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
            r = c.realizarLogin(login, senha)
            self.VerificarLogin(r)
            return True
        else:
            self.ids.Jovem.text = 'Preencha todos os campos!'
            return False


    def VerificarLogin(self, validado):
        if validado:
            self.parent.current = 'telamenu'
        else:
            self.ids.Jovem.text = 'Credenciais Inválidas.'



class TelaCadastro(Screen):

    def CadastrarVoucher(self):
        titulo = self.ids.titulo.text
        descricao = self.ids.descricao.text
        gato = self.ids.gato.text
        local = self.ids.local.text
        lanche = self.ids.lanche.text
        duracao = self.ids.duracao.text

        if (titulo != '' and descricao != '' and gato != '' and local != '' and lanche != '' and duracao != ''):
            c.cadastrarVoucher(titulo, descricao, gato, local, lanche, duracao)
            self.parent.current = 'telamenu'
        else:
            self.ids.cad.text = 'Preencha todos os campos!'
    
    def IrParaMenu(self):
        self.ids.cad.text = 'Cadastrar Voucher'
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

if __name__ == '__main__':
    c = Cliente() # Variável "global" por falta de melhor forma
    principal = TestesInApp()
    principal.run()