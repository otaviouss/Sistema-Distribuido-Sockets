import json
import socket
import asyncio

from bd import banco

class Servidor():

    def __init__():
        pass

    async def cadastrarCliente(email, nome, senha):
        try:
            await banco.inserir_usuario(email, nome, senha)
            return 1
        except:
            return 0
    
    async def checarCliente(email, senha):
        try:
            user = await banco.ver_usuario(email, senha)

            if user is None:
                return 0
             
            return 1
        except:
            return 0

    async def cadastrarVoucher(titulo, descricao, gato, local, lanche, duracao, imagem, titular_id):
        await banco.inserir_voucher(titulo, descricao, gato, local, lanche, duracao, imagem, int(titular_id))

    async def proporTroca(id_voucher1, id_voucher2):
        await banco.nova_Troca(int(id_voucher1), int(id_voucher2))

    async def realizarTroca(id_troca):
        try:
            await banco.alterar_Status_Troca_Aceito(int(id_troca))
            return 1
        except:
            return 0

    async def negarTroca(id_troca):
        await banco.alterar_Status_Troca_Rejeitado(int(id_troca))

    async def apresentarVouchers():
        await banco.ver_vouchers()


def main():
    s = socket.socket()		
    print ("Socket successfully created")

    # reserve a port on your computer
    port = 7777

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', port))		
    print ("socket binded to %s" %(port))

    # put the socket into listening mode
    s.listen(5)	
    print ("socket is listening")		

    # a forever loop until we interrupt it or
    # an error occurs
    while True:

        # Establish connection with client.
        c, addr = s.accept()	
        print ('Got connection from', addr )

        res = ''
        dados = c.recv(1024).decode()

        file = json.loads(dados)

        if(file["op"]=="CC"):
            asyncio.run(Servidor.cadastrarCliente(file["email"], file["nome"], file["senha"]))
        elif(file["op"]=="CV"):
            asyncio.run(Servidor.cadastrarVoucher(file["titulo"], file["descricao"], file["gato"], file["local"], file["lanche"], file["duracao"], file["imagem"], file["titular_id"]))
        elif(file["op"]=="PT"):
            asyncio.run(Servidor.proporTroca(file["id_voucher1"], file["id_voucher2"]))
        elif(file["op"]=="RT"):
            asyncio.run(Servidor.realizarTroca(file["id_troca"],))
        elif(file["op"]=="NT"):
            asyncio.run(Servidor.negarTroca(file["id_troca"],))
        elif(file["op"]=="AV"):
            asyncio.run(Servidor.apresentarVouchers())
        elif(file["op"]=="FL"):
            res = asyncio.run(Servidor.checarCliente(file["email"], file["senha"]))

        # send a thank you message to the client. encoding to send byte type.
        c.send(str(res).encode())

        # Close the connection with the client
        c.close()

        # Breaking once connection closed
        # break


if __name__ == '__main__':
    main()
