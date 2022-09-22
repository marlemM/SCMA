# Documento de Visão

Documento construído a partido do **Modelo BSI - Doc 001 - Documento de Visão** que pode ser encontrado no
link: https://docs.google.com/document/d/1DPBcyGHgflmz5RDsZQ2X8KVBPoEF5PdAz9BBNFyLa6A/edit?usp=sharing

## Equipe e Definição de Papéis

Membro     |     Papel   |   E-mail   |
---------  | ----------- | ---------- |
Ana Paula  | testador    | paulinha.texx@gmail.com
Hiago      | Desenvolvedor, Analista | medeiroshiago70@gmail.com
Márlem      | Gerente, Desenvolvedor | marlem.magno@gmail.com

### Matriz de Competências

Membro     |     Competências   |
---------  | ----------- |
Ana Paula  | Desenvolvedor Java, Junit, Eclipse, JSP, JSF, Hibernate, Matemática, Latex, etc |
Hiago      | Gestão, Geográfa |
Márlem     | Analista de redes, cursando graduação em Sistema de informação |

## Perfis dos Usuários

O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:

Perfil                                 | Descrição   |
---------                              | ----------- |
Administrador | Este usuário realiza os cadastros base e pode realizar qualquer função.
Docentes | Este usuário pode retirar kit de apoio e realizar a devolução,etc.

## Lista de Requisitos Funcionais

Requisito                                 | Descrição   | Ator |
---------                                 | ----------- | ---------- |
RF001 - Manter um cadastro de Centros     | Um centro representa uma unidade administrativa da Universidade. Um centro tem código, nome, sigla, endereço e site. | Administrador |
RF002 - Manter um cadastro de kit de apoio | Um kit de apoio tem código e descrição. | Administrador |

### Modelo Conceitual

Abaixo apresentamos o modelo conceitual usando o **YUML**.

 ![Modelo UML](yuml/monitoria-modelo.png)

O código que gera o diagrama está [Aqui!](yuml/monitoria-yuml.md). O detalhamento dos modelos conceitual e de dados do projeto estão no [Documento de Modelos](doc-modelos.md).

#### Descrição das Entidades

## Lista de Requisitos Não-Funcionais

Requisito                                 | Descrição   |
---------                                 | ----------- |
RNF001 - Deve ser acessível via navegador | Deve abrir perfeitamento no Firefox e no Chrome. |
RNF002 - Consultas deve ser eficiente | O sistema deve executar as consultas em milessegundos |
RNF003 - Log e histórico de acesso e funções | Deve manter um log de todos os acessos e das funções executadas pelo usuário |

## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

Data | Risco | Prioridade | Responsável | Status | Providência/Solução |
------ | ------ | ------ | ------ | ------ | ------ |
10/10/2022 | Não aprendizado das ferramentas utilizadas pelos componentes do grupo | Alta | Todos | Vigente | Reforçar estudos sobre as ferramentas e aulas com a integrante que conhece a ferramenta |
15/10/2022 | Ausência por qualquer motivo do grupo | Média | Gerente | Vigente | Planejar o cronograma tendo em base a agenda do cliente |
30/10/2022 | Divisão de tarefas mal sucedida | Baixa | Gerente | Vigente | Acompanhar de perto o desenvolvimento de cada membro da equipe |
05/11/2022 | Implementação de protótipo com as tecnologias | Alto | Todos | Resolvido | Encontrar tutorial com a maioria da tecnologia e implementar um caso base do sistema |

### Referências