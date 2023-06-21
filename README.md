<div align="center">

<img src="https://github.com/SobrancelhaDoDragao/Sistema-Biblioteca/blob/Alpha-3.0/biblioteca/public/img/meninoLendo.png" alt="Menino lendo um livro na lua" width="200">

</div>

<h1 align="center">Sistema Biblioteca</h1>

<h3 align="center">Gereciamento de livros, empréstimos e acervo de biblioteca</h3>

<div align="center">
    
![Bower](https://img.shields.io/bower/l/mi?color=9cf&style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/SobrancelhaDoDragao/Sistema-Biblioteca?color=9cf&style=for-the-badge)
![GitHub Repo forks](https://img.shields.io/github/forks/SobrancelhaDoDragao/Sistema-Biblioteca?color=9cf&style=for-the-badge)
    
</div>

<h4 align="center">Status: em progresso</h4>

<div align="center">
    
<img src="https://github.com/SobrancelhaDoDragao/Sistema-Biblioteca/blob/master/screenshots/aprensentacao2.gif">
    
</div>

-----------------------------------------------------------------------------------------------------------------

1. [Sobre](#sobre)
2. [Funcionalidades](#funcionalidades)
3. [Tecnologias usadas](#tecnologias-usadas) 
4. [Banco de dados](#banco-de-dados)
5. [Testes](#testes)
6. [Instalação](#instalação)
7. [Licensa](#licensa)

## Sobre

Este projeto tem como objetivo criar uma aplicação web completa para gerenciar o acervo, empréstimos e devoluções de livros em uma biblioteca. A aplicação conta com funcionalidades de login cadastro de usuários, cadastro de livros e bibliotecários.

Durante o meu aprendizado em Vue.js, percebi que o Vue.js carrega a página em branco antes de carregar o JavaScript e, consequentemente, o conteúdo da página. Após pesquisar sobre soluções para este problema, descobri o Server Side Rendering (SSR). Decidi utilizar o Nuxt, um framework baseado em Vue, para facilitar a renderização no lado do servidor e aplicar meus novos conhecimentos.

## Funcionalidades

- [x] Cadastro de usuários e bibliotecários
- [x] Autenticação de usuários e bibliotecários com JWT (JSON Web Token)
- [x] Gerenciamento de livros (adicionar, remover, editar e visualizar)
- [x] Gerenciamento de empréstimos (adicionar, remover, editar e visualizar)
- [x] Gerenciamento de arquivos de imagens para livros e fotos de usuários
- [x] Hierarquia de funcionalidades: a edição de livros e empréstimos é permitida apenas para administradores, enquanto os usuários comuns têm acesso a requisições seguras, como GET, HEAD e OPTIONS.
- [x] Responsividade
- [ ] Pesquisa de livros e empréstimos

## Tecnologias usadas

- Front-End
    - Nuxt
    - Vue.js
    - Javascript
    - Html
    - CSS
    - Pinia
- Back-End
    - Python
    - Django rest framework
    - uWsgi
    - Nginx
    - SqlLite (Pretendo trocar no futuro para o Postgresql)

## Banco de dados

### Diagrama do banco de dados relacional

<img src="https://github.com/SobrancelhaDoDragao/Sistema-Biblioteca/blob/master/screenshots/diagrama_banco.png" alt="Diagrama do banco de dados">

### End-points da Api

#### Cadastro de usuario

- <code>POST /cadastro/</code> End-poit para cadastro de usuario

#### Autenticação JWT(JSON Web Token)

- <code>POST /token/</code> Para efetuar o login
- <code>POST /token/refresh/ </code> End-point para renovar o tokens
- <code>POST /VerifyAuthenticated/</code> End-point para verificar se o usuarios está autenticado

#### User autenticado

##### Permissões: Apenas usuarios autenticados.

- <code>GET /user/</code> Retorna dados do usario autenticado do request
- <code>PUT /user/{id}/</code> Para editar dados do usario autenticado do resquest
- <code>PATCH /user/{id}/</code>Para editar parcialmente dados do usario autenticado do resquest
- <code>DELETE /user/{id}/</code> Para deletar usuario logado

#### Gerenciamento de usuarios

##### Permissões: Apenas usuarios admins tem acesso.

- <code>GET /all_users/</code> Para visualizar todos os usuarios do sistema
- <code>POST /all_users/</code> Para cadastro de um novo usuario
- <code>GET /all_users/{id}/</code> Para recuperar um usuario pelo id
- <code>PUT /all_users/{id}/</code> Para alterar dados de um usuario
- <code>PATCH /all_users/{id}/</code> Para alterar parcialmente dados de um usuario
- <code>DELETE /all_users/{id}/</code> Para deletar um usuario

#### Livros

##### Permissões: Cadastro, editar, excluir permitido apenas para admins. Usuarios comum permitdo apenas visualização.

- <code>GET /livros/</code> Para visualizar todos os livros
- <code>POST /livros/</code> Para cadastrar um novo livro
- <code>GET /livros/{id}/</code> Para recuperar um livro pelo id
- <code>PUT /livros/{id}/</code> Para editar dados de um livro
- <code>PATCH /livros/{id}/</code> Para editar parcialmente dados de um livro
- <code>DELETE /livros/{id}/</code> Para deletar um livro
- <code>GET /novoslivros/</code> Retorna os cinco ultimos livros retornado pelo sistema
- <code>GET /recomendacao/</code> Retorna cinco livros aleatorios

#### Empréstimo

##### Permissões: Cadastro, editar, excluir permitido apenas para admins. Usuarios comum permitdo apenas visualização.

- <code>GET /emprestimos/</code> Para todos visualizar emprestimos do sistema
- <code>POST /emprestimos/</code> Para cadastrar um novo emprestimo
- <code>GET /emprestimos/{id}/</code> Para recuperar um emprestimo especifico
- <code>PUT /emprestimos/{id}/</code> Para editar um emprestimo
- <code>PATCH /emprestimos/{id}/</code> Para editar parciamente um emprestimo
- <code>DELETE /emprestimos/{id}/</code> Para deletar em emprestimo
- <code>GET /usuarios/{id}/emprestimos/</code> Retorna todos os emprestimos relacionado ao usuario

## Estrutura do servidor / Projeto

Em andamento

## Testes

Para executar testes unitários entre na pasta ApiBiblioteca e digite o comando:<code>python manage.py test</code>

## Instalação

### Requisitos

  - Python 3.10.6
  - Venv
  - Pip
  - Node 18.16.0
  
### Instalação Front-End

1. Entre na pasta <code>biblioteca</code> pelo terminal.
2. Instale as dependências com o comando <code>npm install</code> .
3. Crie um arquivo .env para configurar a url do servidor, e adicione a seguinte linha no arquivo. <code>NUXT_PUBLIC_API_BASE_URL = "http://127.0.0.1:8000/"</code> Essa linha poderá mudar dependendo do seu computador.
4. Para inciar o servidor: <code>npm run dev</code>.

### Instalação Back-end

1. Entre na pasta <code>ApiBiblioteca</code> pelo terminal
2. Digite: <code>python -m venv env</code>, para criar um ambiente virtual para instalar as bibliotecas
3. Ative o ambiente virtual: <code>source env/bin/activate</code>
4. Agora digite: <code>pip install -r requirements.txt</code>, para instalar as bibliotecas
5. E finalmente rode o projeto:<code>python manage.py runserver</code>
6. Para cadastrar 55 livros apartir do backup <code>python manage.py loaddata livros_backup.json</code>

## Licensa

[MIT](https://github.com/SobrancelhaDoDragao/Sistema-Biblioteca/blob/master/LICENSE.md)
