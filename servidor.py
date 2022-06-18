import socket
from bd import banco

from _thread import *
import asyncio

class Servidor():

    def __init__():
        pass

    async def cadastrarCliente(email, nome, senha):
        await banco.inserir_usuario(email, nome, senha)

    async def cadastrarVoucher(titulo, descricao, gato, local, lanche, duracao, imagem, titular_id):
        await banco.inserir_voucher(titulo, descricao, gato, local, lanche, duracao, imagem, int(titular_id))

    async def proporTroca(id_voucher1, id_voucher2):
        await banco.nova_Troca(int(id_voucher1), int(id_voucher2))

    async def realizarTroca(id_troca):
        await banco.alterar_Status_Troca_Aceito(int(id_troca))

    async def negarTroca(id_troca):
        banco.alterar_Status_Troca_Rejeitado(int(id_troca))

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

        op = c.recv(1024).decode().split(":")

        if(op[0]=="CC"):
            asyncio.run(Servidor.cadastrarCliente(op[1], op[2], op[3]))
        elif(op[0]=="CV"):
            asyncio.run(Servidor.cadastrarVoucher(op[1],op[2],op[3],op[4],op[5],op[6],op[7], op[8]))
        elif(op[0]=="PT"):
            asyncio.run(Servidor.proporTroca(op[1],op[2]))
        elif(op[0]=="RT"):
            asyncio.run(Servidor.realizarTroca(op[1],))
        elif(op[0]=="NT"):
            asyncio.run(Servidor.negarTroca(op[1],))
        elif(op[0]=="AV"):
            asyncio.run(Servidor.apresentarVouchers())

        # send a thank you message to the client. encoding to send byte type.
        c.send('Thank you for connecting'.encode())

        # Close the connection with the client
        c.close()

        # Breaking once connection closed
        # break


if __name__ == '__main__':
    main()
