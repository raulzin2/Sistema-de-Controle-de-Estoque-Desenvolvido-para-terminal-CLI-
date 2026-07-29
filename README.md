Sistema de Controle de Estoque
Um sistema de gerenciamento de estoque simples e robusto, com duas formas de uso: via terminal (CLI, em Python) e via navegador (interface web, em HTML/CSS/JS puro). Este projeto foi desenvolvido com foco em código limpo, modularização e boas práticas de programação.
Objetivo do Projeto
Demonstrar o domínio de fundamentos essenciais de programação: manipulação de estruturas de dados (dicionários/objetos), controle de fluxo, modularização através de funções, tratamento de erros e persistência de dados — tanto no back-end (Python) quanto no front-end (JavaScript).
Funcionalidades
Cadastrar produto: adiciona um novo item ao estoque com quantidade e preço (impede duplicatas e valores negativos).
Atualizar quantidade: altera a quantidade de um produto existente.
Remover produto: exclui permanentemente um item do estoque.
Listar estoque: exibe todos os itens cadastrados, com o valor total calculado automaticamente.
Consultar produto: busca um item específico e mostra seus dados.
Versões
1. `estoque.py` — versão CLI (terminal)
Versão original do projeto, rodando em Python puro. Os dados agora ficam salvos em `estoque.json`, então o estoque não é perdido ao fechar o programa.
Como executar:
```bash
python3 estoque.py
```
2. `web/index.html` — versão web (interface gráfica)
Versão visual do mesmo sistema, pensada para ser usada como demonstração no portfólio. Usa o mesmo modelo de dados do script Python (`{"nome": {"quantidade": ..., "preco": ...}}`), salva os dados no navegador (`localStorage`) e permite exportar o estoque em `.json` a qualquer momento — no mesmo formato salvo pela versão CLI.
Como executar: basta abrir o arquivo `web/index.html` no navegador, ou publicar via GitHub Pages.
Tecnologias e Conceitos Utilizados
Python 3.x — dicionários aninhados, funções, tratamento de exceções (`try`/`except`), persistência em JSON.
HTML / CSS / JavaScript puro — sem frameworks, manipulação de DOM, `localStorage` para persistência local.
Modelo de dados compartilhado entre as duas versões, o que facilita futuramente ligar uma interface web a um back-end real feito em Python.
Estrutura do repositório
```
.
├── estoque.py          # versão CLI
├── web/
│   └── index.html       # versão web (demo do portfólio)
└── README.md
```
Pré-requisitos (versão CLI)
Você precisa ter o Python instalado na sua máquina (versão 3.6 ou superior).
