# Análise YAGNI - src/usuario_simples.py

O princípio YAGNI (You Aren't Gonna Need It) determina que não se deve implementar funcionalidade antes que ela seja realmente necessária. Os requisitos atuais do sistema são apenas três: **cadastrar** usuários (nome, email e senha), **fazer login** (validando email e senha) e **listar** todos os usuários. Tudo que não serve diretamente a esses três casos de uso é complexidade especulativa.

## 1. Atributos desnecessários da classe `Usuario`

| Atributo | Por que viola YAGNI |
|----------|---------------------|
| `id` | Nenhum requisito atual identifica usuários por id; a busca é feita por email no login. Gerar UUID antecipa uma necessidade hipotética de identificação única. |
| `data_cadastro` | Nenhuma funcionalidade atual consulta ou exibe a data de cadastro. É registro especulativo para auditoria futura. |
| `ultimo_login` | Só faria sentido em relatórios de atividade, que não são requisito. |
| `perfil` | Não existe requisito de tipos de usuário ou papéis; todos os usuários são iguais no sistema atual. |
| `permissoes` | Antecipação de um sistema de autorização que não foi solicitado. |
| `configuracoes` | Antecipação de preferências personalizadas por usuário, funcionalidade inexistente nos requisitos. |
| `historico_logins` | Nenhum requisito exige auditoria de acessos; além disso, registra um IP fixo falso ('0.0.0.0'), evidência de que a funcionalidade não é real. |
| `foto_perfil_url` | Não há requisito de perfil visual ou upload de foto. |
| `telefone` | O cadastro exige apenas nome, email e senha. |
| `endereco` | Idem; dado nunca preenchido nem consultado. |
| `empresa` | Antecipação de um cadastro corporativo que não existe. |
| `cargo` | Idem. |
| `departamento` | Idem. |

Cada um desses atributos aumenta o custo de manutenção (mais estado para entender, testar e migrar) sem entregar valor algum aos três requisitos atuais.

## 2. Métodos desnecessários

### 2.1 Classe `Usuario`

| Método | Por que viola YAGNI |
|--------|---------------------|
| `_gerar_id()` | Existe apenas para sustentar o atributo `id`, que não é necessário. |
| `adicionar_permissao()` | Sustenta o sistema de permissões, que não é requisito. |
| `remover_permissao()` | Idem. |
| `tem_permissao()` | Idem. |
| `atualizar_configuracao()` | Sustenta o dicionário de configurações, que não é requisito. |
| `registrar_login()` | Alimenta `ultimo_login` e `historico_logins`, dados que ninguém consome; o login exige apenas validar email e senha. |
| `exportar_json()` | Não há requisito de exportação de dados; antecipa integração futura. |
| `exportar_xml()` | Idem, e ainda arrasta a dependência de `xml.etree.ElementTree`. |
| `atualizar_foto_perfil()` | Sustenta o atributo `foto_perfil_url`, desnecessário. |
| `atualizar_dados_profissionais()` | Sustenta empresa, cargo e departamento, dados que não fazem parte do cadastro. |

### 2.2 Classe `GerenciadorUsuarios`

| Método / estrutura | Por que viola YAGNI |
|--------------------|---------------------|
| `cache` e `_atualizar_cache()` | Otimização prematura: para o volume atual, uma lista simples resolve. Cache duplica estado e cria risco de inconsistência sem ganho mensurável. |
| `indice_email` | Também é otimização prematura de busca; a verificação de email duplicado e o login funcionam percorrendo a lista de usuários. |
| `buscar_por_id()` | Não há requisito de busca por id; depende do cache e do atributo `id`, ambos desnecessários. |
| `buscar_por_perfil()` | Depende do atributo `perfil`, que não é requisito. |
| `buscar_por_permissao()` | Depende do sistema de permissões, que não é requisito. |
| `exportar_todos_json()` | Não há requisito de exportação; além disso, está incorreto (serializa strings JSON dentro de JSON). |
| `importar_usuarios_json()` | Método vazio (`pass`): funcionalidade puramente especulativa, nem sequer implementada. |
| `gerar_relatorio_atividade()` | Não há requisito de relatórios; retorna valores fixos e falsos (zeros), confirmando que é código morto. |

## 3. O que é mantido e por quê

- **`Usuario` com `nome`, `email` e `senha` (com hash)**: atendem exatamente ao requisito de cadastro. O hash da senha (`_hash_senha` e `validar_senha`) é mantido por ser segurança básica, conforme autorizado no enunciado.
- **`GerenciadorUsuarios.cadastrar()`** com validação de email duplicado: requisito explícito.
- **`GerenciadorUsuarios.fazer_login()`**: requisito explícito (validar email e senha).
- **`GerenciadorUsuarios.listar_todos()`**: requisito explícito.

## 4. Síntese

O código original antecipa pelo menos cinco subsistemas inteiros que não foram pedidos: identificação por UUID, autorização por permissões, auditoria de acessos, perfil estendido (foto, contato, dados profissionais) e importação/exportação de dados, além de duas otimizações prematuras (cache e índice por email). O custo dessas antecipações é concreto: mais código para ler, testar e manter, mais dependências (`json`, `xml`, `uuid`, `datetime`) e maior superfície para defeitos, como demonstram os métodos vazios ou com valores falsos. A versão refatorada em `src/usuario_simples.py` mantém somente o necessário para cadastrar, fazer login e listar usuários.
