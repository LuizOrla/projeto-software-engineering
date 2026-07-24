# Sistema de Gerenciamento de Tarefas

## Descrição do Projeto
O Sistema de Gerenciamento de Tarefas será uma aplicação web desenvolvida para gerenciamento e acompanhamento de tarefas, seguindo os modelos de metodologias ágeis (Kanban).

O objetivo do projeto é criar uma aplicação simples que permita ao usuário cadastrar, visualizar, editar e remover tarefas, mantendo os dados armazenados localmente através de arquivos de persistência no formato JSON.

## Objetivo
O objetivo principal do projeto é desenvolver uma aplicação web funcional para gerenciamento de tarefas, aplicando conceitos de:
- Organização de projetos de software;
- Controle de versão utilizando Git e GitHub;
- Modelagem utilizando UML;
- Desenvolvimento orientado a testes;
- Integração contínua.

## Escopo Inicial
A primeira versão do sistema terá como objetivo disponibilizar um CRUD básico de tarefas.

Funcionalidades previstas:
- Criar novas tarefas;
- Visualizar tarefas cadastradas;
- Editar informações de tarefas;
- Excluir tarefas;
- Salvar e carregar os dados do projeto.

Cada tarefa possuirá inicialmente as seguintes informações:
- Título;
- Descrição;
- Status;
- Usuários atribuídos.

O sistema não utilizará banco de dados. Os dados serão armazenados em arquivos locais, permitindo que o usuário salve e carregue os projetos quando necessário.

Funcionalidades adicionais poderão ser incluídas posteriormente através de alterações de escopo.

## Tecnologias Utilizadas
As tecnologias planejadas para o desenvolvimento são:

- Python;
- NiceGUI para criação da interface web;
- JSON para persistência dos dados;
- Pytest para testes automatizados;
- Git e GitHub para controle de versão;
- GitHub Actions para integração contínua.

## Metodologia de Desenvolvimento
O projeto será desenvolvido utilizando uma abordagem baseada em Kanban.

O gerenciamento das atividades será realizado através do GitHub Projects, utilizando as seguintes colunas:

- **A Fazer**: atividades planejadas;
- **Em Progresso**: atividades em desenvolvimento;
- **Concluído**: atividades concluídas.

As alterações no escopo serão registradas no histórico do projeto, incluindo atualização do Kanban, implementação da funcionalidade e documentação da mudança.

## Estrutura Inicial do Projeto
A estrutura planejada do projeto é:
-  src/
	-  main.py
	-  gui.py
	-  classes.py
	-  storage.py
	-  config.py
-  tests/
-  docs/ 
-  data/
	-  projects.json
-  .github/
	-  workflows/
-  README.md
-  .gitignore


## Modelagem do Sistema
Antes do desenvolvimento será realizada a modelagem inicial do sistema utilizando UML.

Os diagramas previstos são:
- Diagrama de Casos de Uso;
- Diagrama de Classes.

Os diagramas estarão disponíveis na pasta /docs.

## Testes Automatizados
Durante o desenvolvimento serão criados testes automatizados para validar as principais funcionalidades do sistema.

As funcionalidades previstas para teste incluem:
- Criação de tarefas;
- Alteração de tarefas;
- Exclusão de tarefas;
- Persistência dos dados.

Os testes serão executados automaticamente através do GitHub Actions.

## Integração Contínua
O projeto contará com um pipeline de integração contínua utilizando GitHub Actions.

O pipeline será responsável por:
- Instalar as dependências do projeto;
- Executar os testes automatizados;
- Validar o funcionamento básico da aplicação.

## Mudança de Escopo
Durante o desenvolvimento será realizada uma simulação de alteração de escopo.

A alteração será documentada posteriormente nesta seção, contendo:
- Nova funcionalidade adicionada;
- Motivo da alteração;
- Impacto no projeto;
- Atualização realizada no Kanban.

## Autor
Luiz Orlando
