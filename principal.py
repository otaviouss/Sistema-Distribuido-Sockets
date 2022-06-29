from tokenize import String
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
from kivy.uix.popup import Popup


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
        #print("__> ", self.selected)
        global selecionado
        selecionado = self.selected
        if is_selected:
            print("selection changed to {0}".format(index))
            pass
        else:
            print("selection removed for {0}".format(index))
            pass
    

class RV(RecycleView):
    rv_data_list = ListProperty()
    dupla_troca = []
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)



    # Carrega todos os Vouchers
    def LoadData(self):
        self.rv_data_list = []
        dados = c.apresentarVouchers()

        self.rv_data_list.extend([{'label_titulo': dados[str(i)]["titulo"],
                                   'label_descricao': dados[str(i)]["descricao"],
                                   'label_nome_gato': dados[str(i)]["gato"],
                                   'label_local': dados[str(i)]["local"],
                                   'label_lanche': dados[str(i)]["lanche"],
                                   'label_duracao': str(dados[str(i)]["duracao"])} for i in range(len(dados))])
    
    
    # Carrega os Vouchers do Usuário Logado
    def LoadDataUser(self):
        self.rv_data_list.clear()
        dados = c.apresentarVouchersUsuario()
        self.meus_vouchers = dados

        self.rv_data_list.extend([{'label_titulo': dados[str(i)]["titulo"],
                                   'label_descricao': dados[str(i)]["descricao"],
                                   'label_nome_gato': dados[str(i)]["gato"],
                                   'label_local': dados[str(i)]["local"],
                                   'label_lanche': dados[str(i)]["lanche"],
                                   'label_duracao': str(dados[str(i)]["duracao"])} for i in range(len(dados))])
    
    def IsAnyVoucherSelected(self):
        if not self.layout_manager.selected_nodes:
            return False
        
        return True

    def AddVoucherSelected(self):
        print("Check : ", self.dupla_troca)
        self.dupla_troca.append(self.layout_manager.selected_nodes[0])
        self.layout_manager.selected_nodes = []

    # Propõe uma Troca
    def GetPropostaTroca(self):
        print("HELPS : ", self.dupla_troca)
        todos_vouchers = c.apresentarVouchers()
        c.proporTroca(todos_vouchers[str(self.dupla_troca[0])]["id"], self.meus_vouchers[str(self.dupla_troca[1])]["id"])
        self.dupla_troca.clear()


    def InicializarTrocas(self):
        qtd_trocas = len(c.apresentarTrocas())

        self.rv_data_list = []
        self.rv_data_list.extend([{'label_titulo': 'Troca ' + str(i)} for i in range(qtd_trocas)])

    def LoadTrocas(self):
        trocas = c.apresentarTrocas()
        #print(trocas)
        i = 0
        for child in self.children[0].children[:]:
            child.label_trocaI_titulo = trocas[str(i)]['titulo_v1']
            child.label_trocaI_gato = trocas[str(i)]['gato_v1']
            child.label_trocaII_titulo = trocas[str(i)]['titulo_v2']
            child.label_trocaII_gato = trocas[str(i)]['gato_v2']
            i += 1
            
    




#------------------------------------------------------------------------------------
class PopupTroca(Popup):
    def Teste(self):
        print('Loucuras')

class VoucherII(BoxLayout): # Não suporta seleção do voucher na interface (não é clicavel)
    labelII_titulo = StringProperty()
    labelII_descricao = StringProperty()
    labelII_nome_gato = StringProperty()
    labelII_local = StringProperty()
    labelII_lanche = StringProperty()
    labelII_duracao = StringProperty()
class RVII(RecycleView):
    rvII_data_list = ListProperty()

    # Carrega os Vouchers do Usuário Logado
    def LoadData(self):
        self.rvII_data_list = []
        dados = c.apresentarVouchersUsuario()

        self.rvII_data_list.extend([{'labelII_titulo': dados[str(i)]["titulo"],
                                   'labelII_descricao': dados[str(i)]["descricao"],
                                   'labelII_nome_gato': dados[str(i)]["gato"],
                                   'labelII_local': dados[str(i)]["local"],
                                   'labelII_lanche': dados[str(i)]["lanche"],
                                   'labelII_duracao': str(dados[str(i)]["duracao"])} for i in range(len(dados))])


class VoucherSimples(BoxLayout):
    pass

class ComponenteTroca(BoxLayout):
    label_titulo = StringProperty()
    label_trocaI_titulo = StringProperty()
    label_trocaI_gato = StringProperty()
    label_trocaII_titulo = StringProperty()
    label_trocaII_gato = StringProperty()


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

    def PrintChildren(self):
        print("AAAH: ", self.children[0].children[1])
        pass

class TelaMeusVouchers(Screen):
    def IrParaMenu(self):
        self.parent.current = 'telamenu'

class Troca(BoxLayout): # Não suporta seleção do voucher na interface (não é clicavel)
    pass

class TelaTrocas(Screen):
    def loadData():
        print("A")
        pass
    def IrParaMenu(self):
        self.parent.current = 'telamenu'

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
    selecionado = False
    principal = TestesInApp()
    principal.run()


'''
https://stackoverflow.com/questions/40470992/too-many-indentation-levels-in-on-press-button
https://stackoverflow.com/questions/56226448/how-to-get-the-instance-from-a-recycleview-with-viewclass-as-button
'''