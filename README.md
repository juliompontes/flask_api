# Minha primeira API!

## API construída em Flask que retorna dados armazenados em um banco de dados relacional (SQLite) com deploy no Heroku.

### Visão geral do projeto

API é uma das ferramentas mais utilizadas em desenvolvimento de software e seu uso também é amplo entre profissionais das áreas de dados. Uma API (Application Programming Interface) nada mais é do que uma interface de comunicação - realizada através de uma série de protocolos - entre diversos sistemas. Engenheiros de dados constroem pipelines a partir de API's, enquanto analistas e cientistas de dados as consomem para produzir suas análises, dashboards, modelos de Machine Learning...

Nesse projeto foi construída uma API que retorna dados salariais dos profissionais da área de economia (minha área de formação) no Brasil em 2019. A API foi construída baseada em **Flask**, um framework web muito utilizado para construir aplicações web de forma rápida e utilizando **Python**. A API desse projeto foi construída para apenas retornar dados, não sendo possível deletar, atualizar ou inserir novos dados. Não seria difícil criar essas funcionalidades utilizando Flask, mas para esse projeto apenas a funcionalidade de retornar dados atende ao seu propósito. Com a API construída, foi realizado o deploy utilizando **Heroku**.

Assim, é possível consultar a API através [desse link](https://economists-salary-br.herokuapp.com/). 

A API possui 3 endpoints:
* ["/"](https://economists-salary-br.herokuapp.com/): apresentação da API;
* ["/data_sample"](https://economists-salary-br.herokuapp.com/data_sample): retorna as 10 primeiras entradas do banco de dados. Serve como referência para entender como os dados estão estruturados;
* ["/all_data"](https://economists-salary-br.herokuapp.com/all_data): retorno todo o conjunto de dados.

Falando um pouco sobre os dados. Os dados foram obtidos diretamente de uma fonte na internet, no caso, dados da RAIS de 2019, disponibilizados pelo Ministério da Economia [nesse endereço](ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2019/). A coleta dos dados foi realizada através de um script shell - arquivo "collect_data.sh". Esse script **automatiza** os processos de download e descompactação dos arquivos. 

Após a execução do script shell, temos os arquivos de dados em formato ".txt" prontos para serem lidos. É utilizado então um **Jupyter Notebook** para ler os dados através da biblioteca **Dask** e realizar as transformações necessárias através de **Pandas**. Por fim, é criado um banco de dados relacional **SQLite**, onde são inseridos os dados já tratados e limpos. 

Com o banco de dados pronto para ser utlizado, a API é criada no arquivo "app.py". Nesse arquivo temos o código que define os endpoints e os métodos (nesse caso apenas o método "GET") disponíveis. Com os endpoints e os métodos definidos, são realizadas as consultas via SQL que consultarão o banco de dados e gerarão os objetos que retornarão os dados propriamente ditos. 

Temos, portanto, a **construção de todo um pipeline de dados**: coleta, transformação, armazenamento e disponibilização dos dados. Esse é, sem dúvida, o grande objetivo desse projeto.

Além disso, uma API é também uma forma de produtizar o trabalho com dados, ao apresentar uma forma estruturada de entregar dados da maneira mais adequada para o consumidor final.

### Como esse projeto pode ser aplicado para resolver um problema?

Esse projeto realiza toda a construção de um pipeline de dados:

1. Coleta de dados automatizada de uma fonte na web (site do Ministério da Economia do Brasil) a partir de um script shell;
2. Leitura dos arquivos com uma biblioteca python de computação paralela: **Dask**;
3. Limpeza dos dados;
4. Armazenamento dos dados em um banco de dados apropriado;
5. Disponibilização dos dados.

Esses são alguns dos desafios enfrentados pelos engenheiros de dados nas empresas: coletar dados de forma sustentável, limpar e preparar os dados para uso, armazenar os dados adequadamente - tendo em vista limitações de orçamento, capacidade das máquinas e outras - e disponibilizar os dados para cientistas e analistas. Quase todo esse pipeline de dados é realizado nesse projeto de forma relativamente simples, mas de forma eficiente e cumprindo o objetivo proposto.

### Tecnologias

- [x] **Flask** como framework baseado em python para criar a API
- [x] **Shell script** para baixar, descompactar e mover os arquivos com os dados para o diretório correto
- [x] **Python** - bibliotecas **Dask** para ler e manipular grandes arquivos; **Pandas** e **Numpy** para trabalhar com a transformação dos dados; **SQLite** para manipular banco de dados
- [x] **SQL** para criar o banco de dados, fazer a ingestão de dados e realizar as consultas que retornarão os dados na API
- [x] **Heroku** para fazer o deploy da API

### No que você deve ficar de olho :eyes:

* :bulb: Construção de todo um **pipline de dados**: coleta, leitura, transformação e disponibilização 
* :chart_with_upwards_trend: Criação de uma **API** que retorna dados reais de forma estruturada
* :mechanical_arm: Deploy da API no **Heroku**

### Como esse projeto poderia ficar ainda melhor?

- Exigir a autenticação do usuário via token ou OAuth
- Criar outros endpoints para disponibilizar mais dados
- Permitir a execução de outros métodos além de "GET", como, por exemplo, "PUT" (atualizar dados), "POST" (inserir novos dados) e "DELETE" (remover dados)

Não introduzi esses elementos apenas por motivo de simplificação do projeto.

### Como executar esse projeto

1. executar o arquivo do tipo shell "collect_data.sh" para fazer o download, descompactar e mover os arquivos com os dados;
2. executar o jupyter notebook "create_database.ipynb" para realizar a leitura e limpeza dos dados. E também para criar o banco de dados e realizar a ingestão de dados;
3. executar o arquivo python "app.py" para criar a API.
