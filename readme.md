## Trocat

Para executar o programa, inicie seu ambiente virtual python

Em seguida, instale as dependências listadas no arquivo requirements.txt utilizando o seguinte comando:

``pip3 install -r requirements.txt``

Após a instalação das dependências, execute o seguinte comando:

``prisma generate``

O objetivo desse comando é gerar a conexão com o banco por meio do prisma.

Em seguida, execute o seguinte comando:

``prisma py fetch``

Esse comando instala as dependências do prisma. Pode ser necessário rodar esse comando se o programa for executado um tempo depois de játer sido executado. Além disso, às vezes esse comando leva muiot tempo para chegar aos 100% e pode ser cancelado nos 80% e ainda assim irá funcionar (é um bug)

Por fim, execute o servidor em um terminal usando:

``python3 servidor.py``

E em outro terminal, execute o cliente:

``python3 principa.py``

Algumas informações podem ser impressas no terminal tanto do servidor quanto do cliente, o que pode facilitar o entendimento do que está acontecendo no back-end do programa.