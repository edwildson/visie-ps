# About Persons

Este é um projeto `flask+Vuejs`

# <span style="color:#007bff"> Conteúdo </span>

-   [Pré requisitos](#Pré-requisitos)
-   [Tecnologias](#Tecnologias)
-   [Configuração do Ambiente](#Configuração-do-Ambiente)

## Pré requisitos
---

Certifique-se de que você tenha instalado os seguintes pré-requisitos em sua máquina de desenvolvimento ou produção.

-   `Node v16` - [Download & install Node](https://nodejs.org/en) Certifique-se preferenciamente de utilizar a versão 16 do Node.
-   `Python 3`- [Download & install Python](https://www.python.org/downloads/) Certifique-se de que a versão mais recente do Python tenha sido instalada em sua máquina.

### Tecnologias
---

Lista de tecnologias utilizadas neste projeto.

-   Python : Version 3.9.16
-   Flask: Version 2.3.2
-   Node: Version 16.20.1
-   Vue: Version 3.3.4

### Configuração para ambiente de desenvolvimento:
---

A depender da sua versão do docker compose, os comandos poderão ser executados como docker-compose ou como docker compose, então caso uma não funcione, tente a outra.

#### Backend

-   Vá até a pasta ./backend e rode o comando pip install -r requirements.txt
-   Crie o .env usando o .env.example como base e preencha as informações das variaveis
-   Após preencher as informações do .env execute o comando `python db.py` para criar a tabela de pessoas e preencher com as informações prévias
-   Execute o comando python app.py para rodar o servidor e iniciar o funcionamento do backend.


#### Frontend

-   Vá até a pasta ./fontend/vue-persons e instale as dependências com o comando `npm i`
-   Após instalar as dependências build e sirva o frontend com o comando a seguir `npm run dev`.

Acesse a aplicação em [http://localhost:5173](http://localhost:5173).

### Imagens
---

#### Desktop (1080p)
![Listagem](https://i.imgur.com/GRRnRr8.png)
![Visualização](https://i.imgur.com/poiuett.png)
#### Mobile (iPhone 12 Pro)
![Listagem](https://i.imgur.com/oX5N8V4.png)
![Visualização](https://i.imgur.com/v1EqKlv.png)
