import json
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

        file = json.dumps({"op": "CC", "email": email, "nome": nome, "senha": senha})

        s.sendall(file.encode())

        s.close()

    def realizarLogin(self, email, senha):
        s = self.conectar()

        file = json.dumps({"op": "FL", "email": email, "senha": senha})

        s.sendall(file.encode())

        dados = s.recv(1024).decode()
        print(dados)
        if(dados=="1"): print("Sucesso!")
        else:         print("Falha!")

        s.close()

    def cadastrarVoucher(self, titulo, descricao, gato, local, lanche, duracao, imagem, titular_id):
        s = self.conectar()

        file = json.dumps({"op": "CV", "titulo": titulo, "descricao": descricao,
                            "gato": gato, "local": local, "lanche": lanche,
                            "duracao": duracao, "imagem": imagem, "titular_id": titular_id})

        s.sendall(file.encode())

        s.close()

    def proporTroca(self, id_voucher1, id_voucher2):
        s = self.conectar()

        file = json.dumps({"op": "PT", "id_voucher1": id_voucher1, "id_voucher2": id_voucher2})
        
        s.sendall(file.encode())

        s.close()

    def realizarTroca(self, id_troca):
        s = self.conectar()

        file = json.dumps({"op": "RT", "id_troca": id_troca})

        s.sendall(file.encode())

        s.close()

    def negarTroca(self, id_troca):
        s = self.conectar()

        file = json.dumps({"op": "NT", "id_troca": id_troca})

        s.sendall(file.encode())

        s.close()

    def apresentarVouchers(self):
        s = self.conectar()
        
        file = json.dumps({"op": "AV"})

        s.sendall(file.encode())

        s.close()

def main():
    c = Cliente()
    #c.solicitarCriarUsuario(email="test", nome="AAA", senha="123")	
    #c.cadastrarVoucher(titulo="hahah", descricao="hehehe", gato="GT", local="LC", lanche="LA", duracao="DU", imagem="IM", titular_id="1")
    #c.proporTroca(id_voucher1="2", id_voucher2="4")
    #c.realizarTroca(id_troca="1")
    #c.negarTroca(id_troca="2")
    #c.apresentarVouchers()
    c.realizarLogin("lsls", "123")

if __name__ == '__main__':
    main()