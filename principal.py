import kivy

from cliente import Cliente

kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.uix.recycleview import RecycleView
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior, RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''

class Voucher(RecycleDataViewBehavior, BoxLayout):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    '''Atributos Voucher'''
    label_titulo = StringProperty()
    label_descricao = StringProperty()
    label_nome_gato = StringProperty()
    label_local = StringProperty()
    label_lanche = StringProperty()
    label_duracao = StringProperty()
    '''----------------------------'''


    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(Voucher, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(Voucher, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    
    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            #print("selection changed to {0}".format(rv.data[index]))
            pass
        else:
            #print("selection removed for {0}".format(rv.data[index]))
            pass

class RV(RecycleView):
    rv_data_list = ListProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rv_data_list.extend([{'label_titulo': f'Crazy {i}',
                                   'label_descricao': f'Crow {i}',
                                   'button_nome_gato': f'Fresh {i}',
                                   'label_local': f'Crow {i}',
                                   'label_lanche': f'Crow {i}',
                                   'label_duracao': f'Crow {i}'} for i in range(1)])
    
    # Os dados dos vouchers a serem exibidos terão que ser passados como parâmetro aqui (ou função semelhante seguindo estrutura análoga)
    def AddData(self):
        self.rv_data_list.extend([{'label_titulo': f'Crazy {i}',
                                   'label_descricao': f'Crow {i}',
                                   'button_nome_gato': f'Fresh {i}',
                                   'label_local': f'Crow {i}',
                                   'label_lanche': f'Crow {i}',
                                   'label_duracao': f'Crow {i}'} for i in range(2)])

    def Clean(self):
        self.rv_data_list = []

#------------------------------------------------------------------------------------

class ComponenteTroca(BoxLayout):
    label_titulo = StringProperty()

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


class TelaVouchers(Screen):
    def IrParaMenu(self):
        self.parent.current = 'telamenu'

class TelaMeusVouchers(Screen):
    def IrParaMenu(self):
        self.parent.current = 'telamenu'

class TelaTrocas(Screen):
    pass

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

    def IrParaMeusVouchers(self):
        self.parent.current = 'telameusvouchers'

    def IrParaVouchers(self):
        self.parent.current = 'telavouchers'

    def IrParaTrocas(self):
        self.parent.current = 'telatrocas'

    pass

class TestesInApp(App):

    def build(self):
        Window.clearcolor = (1,1,1,1)
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(TelaMenu(name='telamenu'))
        manager.add_widget(TelaCadastro(name='telacadastro'))
        manager.add_widget(TelaMeusVouchers(name='telameusvouchers'))
        manager.add_widget(TelaVouchers(name='telavouchers'))
        manager.add_widget(TelaTrocas(name='telatrocas'))




        return manager

if __name__ == '__main__':
    c = Cliente() # Variável "global" por falta de melhor forma
    principal = TestesInApp()
    principal.run()