# Estruturação de Processo XP e Scrum - AgileTech Solutions

## 1. Quadro Kanban no GitHub Projects

**Link para o quadro:** [GitHub Projects - AgileTech Solutions](COLOQUE_AQUI_O_LINK_DO_SEU_PROJECT)

### 1.1 Colunas configuradas

O quadro combina o fluxo visual do Kanban com os artefatos do Scrum e as práticas de qualidade do XP:

1. **Backlog do Produto**: todas as user stories priorizadas pelo Product Owner.
2. **Sprint Backlog**: itens selecionados na Sprint Planning para a Sprint atual.
3. **Em Desenvolvimento (WIP: 3)**: itens em implementação, com limite de trabalho em progresso para evitar sobrecarga (elemento Kanban).
4. **Em Revisão / Testes**: itens aguardando revisão de código (pareamento ou pull request) e execução de testes automatizados (elemento XP).
5. **Concluído (Done)**: itens que atendem à Definição de Pronto: código revisado, testes passando e integrado à branch principal.

### 1.2 Cards do quadro (user stories)

1. **US-01**: Como usuário, quero me cadastrar com nome, email e senha para acessar o sistema.
2. **US-02**: Como usuário, quero fazer login com email e senha para entrar na minha conta.
3. **US-03**: Como Product Owner, quero criar projetos com nome e descrição para organizar o trabalho da equipe.
4. **US-04**: Como membro da equipe, quero criar e mover tarefas em um quadro Kanban para acompanhar o fluxo de trabalho.
5. **US-05**: Como Product Owner, quero priorizar itens do backlog para orientar o planejamento da Sprint.
6. **US-06 (tarefa técnica)**: Configurar pipeline de integração contínua com execução automática de testes.

## 2. Práticas de XP adotadas pela equipe

1. **Programação em pares (Pair Programming)**: duas pessoas por estação, com papéis de piloto e navegador trocados frequentemente. Garante revisão contínua e dissemina conhecimento na equipe pequena.
2. **Desenvolvimento orientado a testes (TDD)**: escreve-se primeiro o teste que falha, depois o código mínimo que o faz passar, seguido de refatoração. Cria uma rede de segurança para as mudanças frequentes de requisitos.
3. **Integração contínua**: o código é integrado à branch principal várias vezes ao dia, com build e testes automáticos a cada integração. Evita a "integração big bang" e mantém o software sempre entregável.
4. **Refatoração contínua**: o design é melhorado de forma constante e segura (apoiada pelos testes), mantendo o código limpo mesmo com evolução acelerada.
5. **Design simples (YAGNI)**: implementa-se apenas o necessário para os requisitos atuais, sem antecipar funcionalidades hipotéticas. Reduz complexidade e custo de mudança.
6. **Propriedade coletiva do código**: qualquer membro pode alterar qualquer parte do código. Elimina gargalos e reforça a responsabilidade compartilhada pela qualidade.
7. **Releases pequenas**: entregas frequentes de incrementos pequenos e funcionais, alinhadas à pressão da empresa por demonstrar valor ao mercado.

## 3. Integração das práticas XP ao framework Scrum

Scrum e XP são complementares: o Scrum organiza **o processo de gestão** (papéis, eventos, artefatos), enquanto o XP fornece **as práticas de engenharia** que sustentam a qualidade técnica dentro de cada Sprint.

- A **Sprint** do Scrum é o contêiner de tempo dentro do qual as práticas de XP acontecem diariamente: pareamento, TDD, integração contínua e refatoração.
- A **Sprint Planning** define o Sprint Backlog; o **design simples (YAGNI)** orienta a equipe a estimar e implementar apenas o que a Sprint exige.
- A **Daily Scrum** é o momento natural para formar e rotacionar os pares do dia e sinalizar necessidades de refatoração ou impedimentos técnicos.
- A **Definição de Pronto** incorpora as práticas XP: um item só é "Done" se tiver testes escritos (TDD), tiver sido revisado (pareamento) e estiver integrado com o build verde (integração contínua).
- A **Sprint Review** se beneficia das releases pequenas: há sempre um incremento funcional para demonstrar ao cliente.
- A **Retrospectiva** avalia também a saúde das práticas de engenharia (cobertura de testes, frequência de integração, qualidade dos pareamentos), gerando melhorias no processo técnico.

## 4. Fluxo de trabalho semanal da equipe

- **Segunda-feira**:
  - Sprint Planning (na primeira semana da Sprint) ou refinamento rápido do backlog (na segunda semana).
  - Formação dos pares da semana e definição das metas.
- **Diariamente (terça a sexta)**:
  - Daily Scrum às 9h30 (15 minutos): o que foi feito, o que será feito, impedimentos.
  - Sessões de pareamento com TDD durante o dia; integrações à branch principal pelo menos uma vez por dia por par.
  - Atualização do quadro Kanban no GitHub Projects conforme os cards avançam.
- **Quarta-feira**:
  - Sessão de refinamento do backlog com o Product Owner (45 minutos), preparando itens para a próxima Sprint.
- **Sexta-feira**:
  - Revisão técnica da semana: análise do build, dívidas técnicas e refatorações pendentes.
  - Na última sexta da Sprint: Sprint Review com o cliente, seguida da Retrospectiva da equipe.

## 5. Cronograma de uma Sprint de 2 semanas

### Semana 1

- **Dia 1 (segunda)**:
  - **Sprint Planning**: 2 horas. Participantes: toda a equipe (PO, 5 desenvolvedores). Define-se a meta da Sprint e o Sprint Backlog. Aplicação de XP: o design simples orienta o escopo; o jogo do planejamento (planning game) apoia as estimativas.
  - Tarde: formação dos pares e início do desenvolvimento com TDD.
- **Dias 2 a 5 (terça a sexta)**:
  - **Daily Scrum**: 15 minutos, todos os dias às 9h30. Participantes: equipe de desenvolvimento; PO como convidado.
  - Desenvolvimento com pareamento, TDD e integração contínua ao longo de todo o dia.
  - Dia 3 (quarta): refinamento de backlog com o PO (45 minutos).
  - Dia 5 (sexta): rotação de pares e revisão de dívidas técnicas.

### Semana 2

- **Dias 6 a 8 (segunda a quarta)**:
  - Daily Scrum diária (15 minutos).
  - Continuação do desenvolvimento com práticas XP; foco em fechar itens em "Em Revisão / Testes".
  - Dia 8 (quarta): refinamento do backlog para a próxima Sprint (45 minutos, com PO).
- **Dia 9 (quinta)**:
  - Estabilização: refatorações finais, correção de defeitos e verificação da Definição de Pronto de cada item.
  - Congelamento de novas funcionalidades da Sprint; apenas integração e ajustes.
- **Dia 10 (sexta)**:
  - **Sprint Review**: 1 hora. Participantes: equipe completa e cliente. Demonstração do incremento funcional e coleta de feedback.
  - **Sprint Retrospective**: 1 hora. Participantes: equipe de desenvolvimento e PO. Avaliação do processo e das práticas de engenharia, com ações de melhoria para a próxima Sprint.

### Entregas esperadas ao final da Sprint

- Incremento de software funcionando, integrado e potencialmente entregável (release pequena).
- Todos os itens concluídos atendendo à Definição de Pronto: testes automatizados passando, código revisado em par e integrado com build verde.
- Backlog refinado e priorizado para a próxima Sprint.
- Lista de ações de melhoria definidas na Retrospectiva.

## 6. Comparação: Scrum vs Kanban

| Aspecto | Scrum | Kanban |
|---------|-------|--------|
| Cadência | Iterações fixas (Sprints de 1 a 4 semanas) | Fluxo contínuo, sem iterações obrigatórias |
| Papéis | Definidos: Product Owner, Scrum Master, Time de Desenvolvimento | Não prescreve papéis |
| Planejamento | Sprint Planning define o escopo fixo da iteração | Itens são puxados sob demanda conforme há capacidade |
| Limitação de trabalho | Indireta, pelo escopo da Sprint | Explícita, por limites de WIP em cada coluna |
| Mudanças durante o ciclo | Desencorajadas dentro da Sprint | Permitidas a qualquer momento, respeitando o WIP |
| Métricas típicas | Velocity, burndown da Sprint | Lead time, cycle time, throughput |
| Cerimônias | Prescritas: Planning, Daily, Review, Retrospectiva | Opcionais: reuniões de cadência conforme necessidade |
| Quando usar | Desenvolvimento de produto com metas por iteração, necessidade de ritmo e previsibilidade de entrega | Fluxos de demanda contínua e imprevisível (sustentação, suporte, operações) ou quando se deseja evoluir o processo atual gradualmente |

### Como podem ser combinados (Scrumban)

A AgileTech adota uma combinação das duas abordagens:

- O **Scrum** fornece a estrutura de cadência: Sprints de 2 semanas, papéis definidos e cerimônias regulares, garantindo pontos previsíveis de contato com o cliente.
- O **Kanban** fornece a gestão visual do fluxo dentro da Sprint: quadro no GitHub Projects com colunas explícitas e **limite de WIP** na coluna "Em Desenvolvimento", evitando que a equipe inicie mais trabalho do que consegue terminar.
- As métricas se complementam: velocity apoia o planejamento das Sprints, enquanto cycle time revela gargalos no fluxo (por exemplo, itens parados em revisão).
- Essa combinação preserva a previsibilidade e o feedback regular do Scrum, com a eficiência de fluxo e a transparência do Kanban.
