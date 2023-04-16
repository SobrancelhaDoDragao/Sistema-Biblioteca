<h1 align="center">Sistema Biblioteca</h1>

<h3 align="center">Gereciamento de livros, empréstimos e acervo de biblioteca</h3>

<div align="center">

<img src="https://github.com/SobrancelhaDoDragao/Sistema-Biblioteca/blob/master/biblioteca/assets/img/meninoLendo.png" alt="Menino lendo um livro na lua" width="100">

</div>

<h4 align="center">Status: em progresso</h4>

## Tópicos

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
- [x] Autenticação de usuários e bibliotecários
- [x] Gerenciamento de livros (adicionar, remover, editar e visualizar)
- [ ] Gerenciamento de empréstimos (adicionar, remover, editar e visualizar)
- [ ] Pesquisa de livros e empréstimos

## Tecnologias usadas

- Python
- Javascript
- Django rest framework
- Vue.js
- Nuxt
- Html 
- Css
- Pinia

## Banco de dados

Em andamendo

## Testes

Em andamento

## Instalação

### Requisitos

  - Python 3.8.10
  - Npm 18.15.0
  - Venv
  
### Instalação Front-End

1. Entre na pasta <code>biblioteca</code> pelo terminal
2. Instale as dependências com o comando <code>npm install</code> 
3. Para inciar o servidor: <code>npm run dev</code>

### Instalação Back-end

1. Entre na pasta <code>ApiBiblioteca</code> pelo terminal
2. Digite: <code>python -m venv env</code>, para criar um ambiente virtual para instalar as bibliotecas
3. Ative o ambiente virtual: <code>source env/bin/activate</code>
4. Agora digite: <code>pip install -r requirements.txt</code>, para instalar as bibliotecas
5. E finalmente rode o projeto:<code>python manage.py runserver</code>

## Licensa

[MIT](https://github.com/SobrancelhaDoDragao/Sistema-Biblioteca/blob/master/LICENSE.md)
