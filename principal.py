import kivy

kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

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
            self.parent.current = 'telatrocas'
        else:
            self.ids.Jovem.text = 'Não deu'



class TelaTrocas(Screen):
    pass



class TestesInApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        manager.add_widget(TelaTrocas(name='telatrocas'))

        return manager

Meu = TestesInApp()
Meu.run()