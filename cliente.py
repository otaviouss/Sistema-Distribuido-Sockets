import socket

class Cliente():

    def __init__(self):
        pass

    def conectar(self):
        s = socket.socket()
        # Define the port on which you want to connect
        port = 7777
        # connect to the server on local computer
        s.connect(('127.0.0.1', port))
        return s

    def solicitarCriarUsuario(self, email, nome, senha):
        s = self.conectar()

        s.sendall("CC:".encode())
        s.sendall(email.encode())
        s.sendall(":".encode())
        s.sendall(nome.encode())
        s.sendall(":".encode())
        s.sendall(senha.encode())

        s.close()

    def cadastrarVoucher(self, titulo, descricao, gato, local, lanche, duracao, imagem, titular_id):
        s = self.conectar()

        s.sendall("CV:".encode())
        s.sendall(titulo.encode())
        s.sendall(":".encode())
        s.sendall(descricao.encode())
        s.sendall(":".encode())
        s.sendall(gato.encode())
        s.sendall(":".encode())
        s.sendall(local.encode())
        s.sendall(":".encode())
        s.sendall(lanche.encode())
        s.sendall(":".encode())
        s.sendall(duracao.encode())
        s.sendall(":".encode())
        s.sendall(imagem.encode())
        s.sendall(":".encode())
        s.sendall(titular_id.encode())

        s.close()

    def proporTroca(self, id_voucher1, id_voucher2):
        s = self.conectar()

        s.sendall("PT:".encode())
        s.sendall(id_voucher1.encode())
        s.sendall(":".encode())
        s.sendall(id_voucher2.encode())

        s.close()

    def realizarTroca(self, id_troca):
        s = self.conectar()

        s.sendall("RT:".encode())
        s.sendall(id_troca.encode())

        s.close()

    def negarTroca(self, id_troca):
        s = self.conectar()

        s.sendall("NT:".encode())
        s.sendall(id_troca.encode())

        s.close()

    def apresentarVouchers(self):
        s = self.conectar()

        s.sendall("AV".encode())

        s.close()

def main():
    c = Cliente()
    c.solicitarCriarUsuario(email="gm", nome="AAA", senha="123")	
    c.cadastrarVoucher(titulo="TI", descricao="DS", gato="GT", local="LC", lanche="LA", duracao="DU", imagem="IM", titular_id="1")
    c.proporTroca(id_voucher1="2", id_voucher2="4")
    c.realizarTroca(id_troca="1")
    c.negarTroca(id_troca="2")
    c.apresentarVouchers()

if __name__ == '__main__':
    main()