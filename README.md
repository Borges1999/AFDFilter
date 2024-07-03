# AFDFilter


## O que é o AFDFilter?
Uma ferramenta desenvolvida em Python para filtragem e análise de arquivos AFD, que tem como objetivo principal agilizar e facilitar esses processos por meio do algoritmo utilizado em seu desenvolvimento.

- Python
  - Tkinter
  - CustomTkinter

<img width="600" alt="image" src="https://github.com/Borges1999/AFDFilter/assets/144748871/7fed1f14-8087-4b92-8063-a00ca017482d">


### Especificações técnicas 

Sistema Operacional: Windows 10/11 - x32 ou x64;

Python: Versões acima de 3.11.5;

Compatível com telas de resolução: 1920x1080 de 14 a 21,5 Pol.

### Pacotes e Arquivos

Download AFDFilter: https://drive.google.com/drive/folders/1NiUUrDXwuNuHeps1C5xLJzR_aIojrJLb?usp=drive_link

Download Python: https://python.org.br/instalacao-windows/



#
## Como funciona a filtragem por PIS/CPF?

A informação inserida no campo PIS/CPF é buscada dentro do arquivo e todas as ocorrências exatas desses valores são apresentadas no arquivo filtrado, o software busca por essas informações, armazena e por fim lista linha por linha no arquivo de saída.

Pela utilização de dados reais, os mesmos foram ocultados em todos os exemplos apresentados:

![image](https://github.com/Borges1999/AFDFilter/assets/144748871/1ceb5381-7f35-400d-878b-6710271e0414)

Como o campo busca pela ocorrência exata do valor preenchido, este campo pode funcionar como um "Coringa", por sua filtragem não ser posicional com base no início e fim dos caracteres como os demais, esse campo pode filtrar até mesmo por nome, desde que o valor preenchido seja exatamente igual dentro do arquivo, você também pode utilizá-lo para encontrar uma NSR especifica ou então até mesmo pelo código CRC das marcações.


#
## Filtragem por Data
Essa função realiza a filtragem posicional dos caracteres referente a data inicial e final dentro de um AFD, ou seja, o software pega o primeiro caractere informado da data inicial até o último caractere dessa data, identifica a posição dentro da linha e através desse posicionamento realiza a filtragem dessas informações até a data final linha por linha sendo realizado o mesmo processo.

 ![image](https://github.com/Borges1999/AFDFilter/assets/144748871/374192f3-0ee7-424c-bad0-2b7ff4eafe19)

Esse processo garante uma filtragem mais segura das informações, pois como a filtragem está sendo realizada pela posição dos caracteres isso impede que caso o usuário filtre um arquivo com por exemplo meio milhão de linhas, valores como da NSR não sejam confundidos com alguma data, fazendo com que o arquivo filtrado saía com informações desnecessárias e incorretas. O arquivo de saída ainda contém os dados de cabeçalho e trailer.


#
## Verificar AFD
E por último mas não menos importante, a função que acredito ser o diferencial desta ferramenta. Ela foi desenvolvida para realizar a validação de um arquivo AFD, para concluirmos se ele se encontra corrompido ou não.
Sua lógica funciona da seguinte maneira, sabemos que a NSR possui 9 caracteres e são esses valores que são validados linha a linha pelo software, o programa lê os primeiros 9 caracteres de cada linha e valida se as linhas estão seguindo uma ordem numérica crescente, caso os valores fujam dessa ordem crescente, o software armazena a posição da linha, seu conteúdo e ao final do processo cria um arquivo no formato txt com a quantidade de linhas com problema na NSR, com o número da linha problemática e seu conteúdo, e tudo isso em segundos independentemente do tamanho do AFD.

### Exemplo
![image](https://github.com/Borges1999/AFDFilter/assets/144748871/624e6889-81bc-48c8-8adf-60e2ad009dcd)

O exemplo acima demonstra um pulo na ordem numérica crescente da NSR, neste caso o sistema armazenaria em seu arquivo de saída, a posição da linha problemática, o conteúdo da linha e pôr fim a quantidade de linhas com problema no NSR dentro deste arquivo AFD.

### Arquivo de Saída

![image](https://github.com/Borges1999/AFDFilter/assets/144748871/34fee6ca-2f99-4713-b61a-55a68e961f6c)





