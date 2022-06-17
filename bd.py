import asyncio
from datetime import datetime
from prisma import Prisma

class banco():

    async def inserir_usuario() -> None:
        prisma = Prisma()
        await prisma.connect()

        # write your queries here
        user = await prisma.usuario.create(
            data={
                'email': 'marta@gmail.com',
                'nome': 'Marta',
                'senha': '12345',
            }
        )

        users = await prisma.usuario.find_many()
        print(users)

        await prisma.disconnect()

    async def inserir_voucher() -> None:
        prisma = Prisma()
        await prisma.connect()

        # write your queries here
        user = await prisma.voucher.create(
            data={
                'titulo': 'BBB', 
                'descricao': '123',
                'gato': 'Bella',
                'local': 'Corredor',
                'lanche': 'banana',
                'duracao': datetime.now(),
                'imagem': 'url',
                'titular_id': 2,
            }
        )

        vouchers = await prisma.voucher.find_many()
        print(vouchers)

        await prisma.disconnect()
    
    async def nova_Troca() -> None:
        prisma = Prisma()
        await prisma.connect()

        # write your queries here
        user = await prisma.troca.create(
            data={
                'voucher1_id': 1,
                'voucher2_id': 3,
                'usuario1_id': 1,
                'usuario2_id': 2,
                'status': 0,
            }
        )

        trocas = await prisma.troca.find_many()
        print(trocas)

        vouchers = await prisma.voucher.find_many()
        print(vouchers)

        await prisma.disconnect()
    

if __name__ == '__main__':
    asyncio.run(banco.nova_Troca())

