import asyncio
from datetime import datetime
from prisma import Prisma

class banco():

    async def inserir_usuario(email, nome, senha) -> int:
        prisma = Prisma()
        await prisma.connect()

        user = await prisma.usuario.create(
            data={
                'email': email,
                'nome': nome,
                'senha': senha,
            }
        )

        await prisma.disconnect()

        return user.id
    
    async def ver_usuarios() -> None:
        prisma = Prisma()
        await prisma.connect()

        users = await prisma.usuario.find_many()
        print(users)

        await prisma.disconnect()

    async def inserir_voucher(titulo, descricao, gato, local, lanche, duracao, imagem, titular_id) -> int:
        prisma = Prisma()
        await prisma.connect()

        voucher = await prisma.voucher.create(
            data={
                'titulo': titulo, 
                'descricao': descricao,
                'gato': gato,
                'local': local,
                'lanche': lanche,
                'duracao': datetime.now(),
                'imagem': imagem,
                'titular_id': titular_id,
            }
        )

        await prisma.disconnect()

        return voucher.id

    async def ver_vouchers() -> None:
        prisma = Prisma()
        await prisma.connect()

        vouchers = await prisma.voucher.find_many()
        print(vouchers)

        await prisma.disconnect()
    
    async def alterar_Titular_Voucher(id, novo_titular_id) -> None:
        prisma = Prisma()
        await prisma.connect()

        voucher = await prisma.voucher.update(
            data={
                'titular_id': novo_titular_id,
            },
            where={
                'id': id,
            }
        )

        await prisma.disconnect()

    async def nova_Troca(id_v1, id_v2) -> int:
        prisma = Prisma()
        await prisma.connect()

        troca = await prisma.troca.create(
            data={
                'voucher1_id': id_v1,
                'voucher2_id': id_v2,
                'status': 0,
            }
        )

        await prisma.disconnect()

        return troca.id

    async def ver_Trocas() -> None:
        prisma = Prisma()
        await prisma.connect()

        trocas = await prisma.troca.find_many()
        print(trocas)

        await prisma.disconnect()

    async def alterar_Status_Troca_Aceito(id) -> None:
        prisma = Prisma()
        await prisma.connect()

        troca = await prisma.troca.update(
            data={
                'status': 1,
            },
            where={
                'id': id,
            }
        )

        await prisma.disconnect()
    
    async def alterar_Status_Troca_Rejeitado(id) -> None:
        prisma = Prisma()
        await prisma.connect()

        troca = await prisma.troca.update(
            data={
                'status': 2,
            },
            where={
                'id': id,
            }
        )

        await prisma.disconnect()
    

if __name__ == '__main__':
    u = asyncio.run(banco.inserir_usuario("aaa@gmail.com", "Larissa", "123"))
    asyncio.run(banco.inserir_voucher("V1", "D1", "Belinha", "Sala", "Ração", "", "URL", u))
    asyncio.run(banco.nova_Troca(3, 4))
    asyncio.run(banco.ver_usuarios())
    asyncio.run(banco.ver_vouchers())
    asyncio.run(banco.alterar_Status_Troca_Rejeitado(1))
    asyncio.run(banco.ver_Trocas())


