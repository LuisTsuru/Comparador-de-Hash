Programa feito com intuito de aprendizado.

O repositorio contém:
1. Um arquivo ".txt" que simula um banco de dados contendo hashes de senhas;  
2. Um arquivo ".txt" que simula um "rockyou.txt" contendo exemplos de possiveis senhas;
3. Um arquivo ".py" que possui o código do qual tranforma os exeplos do arquivo2 em hashes dos quais serao comparados com os exemplos do arquivo1;


O codigo possui duas funções:
    register():
    Essa função quando utilizada pergunta quantas senhas deseja registrar e logo em seguida te permite "registra-las". Após inserir as senhas, elas serão registradas em "plaintext" e em formato hash nos arquivos "rainbowtable.txt" e "database-teste.txt" respectivamente.
    decrypt():
    Ira pegar os hashs do arquivo "database-teste.txt" e comparar com as senhas "plaintext" do arquivo "rainbowtable.txt". Caso o hash seja o mesmo o arquivo ira printar o hash e o seu "plain text".
