# API de Biblioteca — Exercício de Testes Automatizados e TDD

Projeto de formação em backend com **TypeScript, Express, Sequelize e Jest**, organizado em torno de uma API HTTP para gestão de livros, usuários e empréstimos de uma biblioteca.

## Contexto

Este repositório foi desenvolvido como parte de uma atividade de testes automatizados. A proposta do exercício envolve recuperar testes, completar casos pendentes e implementar funcionalidades de API orientadas por testes (TDD).

> Este projeto é uma atividade acadêmica/de formação. O enunciado original não deve ser confundido com documentação de produção nem com a autoria integral do código-base.

## Tecnologias

- TypeScript e Node.js
- Express
- Sequelize
- Jest e ts-jest
- SQLite para ambiente local/testes, conforme configuração do projeto
- PostgreSQL disponível entre as dependências

## Estrutura

```text
src/           # Código da aplicação
tests/         # Casos de teste
docs/          # Documentação adicional
jest.config.ts # Configuração do Jest
```

## Execução dos testes

O repositório utiliza Yarn e define o comando de teste no `package.json`:

```bash
yarn install
yarn test
```

> Os testes não foram executados durante esta revisão; a execução depende das configurações e dependências locais do repositório. Consulte os arquivos em `docs/` e o enunciado do projeto para requisitos adicionais.

## O que este projeto demonstra

- Leitura de requisitos de API HTTP.
- Desenvolvimento e manutenção de testes automatizados.
- Organização de código TypeScript para endpoints, regras de negócio e persistência.
- Aplicação de conceitos de TDD no contexto de um exercício de backend.

## Melhorias futuras

- Documentar quais tarefas foram implementadas pessoalmente e quais vieram do código inicial.
- Publicar o resultado de uma execução recente da suíte de testes.
- Criar um workflow de CI para validar testes automaticamente.
- Separar documentação de uso do enunciado original.
