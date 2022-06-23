import json
import socket
import zlib

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
        self.s = self.conectar()

        file = json.dumps({"op": "CC", "email": email, "nome": nome, "senha": senha})

        self.s.sendall(file.encode())

        dados = self.s.recv(1024).decode()
        print(dados)
        if(dados=="1"):
            print("Sucesso!")
        else:
            print("Falha! Email já utilizado.")
        
        self.desconectar()

    def realizarLogin(self, email, senha):
        self.s = self.conectar()

        file = json.dumps({"op": "FL", "email": email, "senha": senha})

        self.s.sendall(file.encode())

        dados = self.s.recv(1024).decode()

        if(dados=="1"):
            self.user = email
            print("Sucesso!")
            self.desconectar()
            return 1
        else:
            print("Falha!")
            self.desconectar()
            return 0

    def cadastrarVoucher(self, titulo, descricao, gato, local, lanche, duracao, imagem, titular_id):
        self.s = self.conectar()

        file = json.dumps({"op": "CV", "titulo": titulo, "descricao": descricao,
                            "gato": gato, "local": local, "lanche": lanche,
                            "duracao": duracao, "imagem": imagem, "titular_id": titular_id})

        self.s.sendall(file.encode())

        self.desconectar()

    def proporTroca(self, id_voucher1, id_voucher2):
        self.s = self.conectar()

        file = json.dumps({"op": "PT", "id_voucher1": id_voucher1, "id_voucher2": id_voucher2})
        
        self.s.sendall(file.encode())

        self.desconectar()

    def realizarTroca(self, id_troca):
        self.s = self.conectar()

        file = json.dumps({"op": "RT", "id_troca": id_troca})

        self.s.sendall(file.encode())

        self.desconectar()

    def negarTroca(self, id_troca):
        self.s = self.conectar()

        file = json.dumps({"op": "NT", "id_troca": id_troca})

        self.s.sendall(file.encode())

        self.desconectar()

    def apresentarVouchersUsuario(self, id_usuario):
        self.s = self.conectar()
        
        file = json.dumps({"op": "VU", "id_usuario": id_usuario})

        self.s.sendall(file.encode())

        dados = self.s.recv(1048576).decode()

        print("V: ", json.loads(dados))

        self.desconectar()

    def apresentarVouchers(self):
        self.s = self.conectar()
        
        file = json.dumps({"op": "AV"})

        self.s.sendall(file.encode())

        dados = self.s.recv(1048576).decode()

        print("V: ", json.loads(dados))

        self.desconectar()
    
    def desconectar(self):
        self.s.close()

def main():
    c = Cliente()
    #c.solicitarCriarUsuario(email="teste", nome="AAA", senha="123")	
    c.realizarLogin("test", "123")
    #c.cadastrarVoucher(titulo="hahah", descricao="hehehe", gato="GT", local="LC", lanche="LA", duracao="DU", imagem="IM", titular_id="1")
    #c.proporTroca(id_voucher1="2", id_voucher2="4")
    #c.realizarTroca(id_troca="1")
    #c.negarTroca(id_troca="2")
    c.apresentarVouchersUsuario("2")
    #c.realizarLogin("lsls", "123")
    c.desconectar()

if __name__ == '__main__':
    main()