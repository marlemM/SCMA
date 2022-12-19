# Documento de Visão

Documento construído a partir do do **Modelo BSI - Doc 001 - Documento de Visão** que pode ser encontrado no
link: https://docs.google.com/document/d/1DPBcyGHgflmz5RDsZQ2X8KVBPoEF5PdAz9BBNFyLa6A/edit?usp=sharing


## Histórico de Revisões 

Data       |    Versão   |   Descrição        |  Autor
---------  | ----------- | ------------------ | ---------
21/09/2022 | 1.0         | Documento inicial  |  Marlem
22/09/2022 | 1.1         | Formatação do texto |  Ana Paula
29/09/2022 | 1.2         | Adição de requisitos | Hiago

## Equipe e Definição de Papéis

Membro     |     Papel   |   E-mail   |
---------  | ----------- | ---------- |
Taciano    | Cliente     | taciano@bsi.ufrn.br
Ana Paula  | testador    | paulinha.texx@gmail.com
Hiago      | Desenvolvedor, Analista | medeiroshiago70@gmail.com
Márlem     | Gerente, Desenvolvedor | marlem.magno@gmail.com

### Matriz de Competências

Membro     |     Competências   |
---------  | ------------------ |
Ana Paula  | Gestão de RH, Desenvolvedor Python, Administração |
Hiago      | Desenvolvedor Java,cursando graduação em Sistema de informação  |
Márlem     | Analista de redes, cursando graduação em Sistema de informação |


## Descrição do Projeto

O SCMA, é um sistema de controle que é responsável por gerenciar todo o material de apoio utilizados pelos docentes do Ceres Caicó, a fim de eliminar o controle destes materiais através de planilhas em papel , reduzindo o consumo de material , agilizando o processo e permitindo um maior controle do patrimônio.


## Perfis dos Usuários

O sistema poderá ser utilizado por três tipos de usuários. Temos os seguintes perfis/atores:

Perfil                                 | Descrição   |
---------                              | ----------- |
Administrador | Este usuário realiza os cadastros base e pode realizar qualquer função.
Secretário | Este usuário realiza empréstimos , reserva de kit ou item , verifica disponibilidade de material e necessidade de aquisição de materiais.
Docentes | Este usuário pode retirar kit de apoio e realizar a devolução,verificar disponibilidade de kit, etc.

## Lista de Requisitos Funcionais

Requisito                                 | Descrição   | Ator |
---------                                 | ----------- | ---------- |
| RF001 - Cadastrar usuário | O usuário possui os atributos nome, email e senha. | Administrador |
| RF002 - Buscar usuário | A busca deve ser feita a partir do nome do usuário . | Administrador |
| RF003 - Alterar usuário | A alteração permite editar informações cadastradas do usuário. | Administrador |
| RF004 - Deletar usuário | Deve ser possível apagar um usuário cadastrado. | Administrador |
| RF005 - Cadastrar item | O cadastroé feito a partir das informações do item como código  e descrição e tipo. | Secretário |
| RF006 - Tipo do item | Durante o cadastro do item, deve ser possível escolher o tipo do item. | Secretário |
| RF007 - Buscar item | Deve ser possível fazer uma busca entre os itens cadastrados no sistema. | Secretário, Docente |
| RF008 - Alterar item | Deve ser possível alterar o as informações do item cadastrado. | Secretário |
| RF009 - Excluir item | Deve ser possível excluir o item do sistema caso ele não esteja mais em posse do apoio pedagógico. | Secretário |
| RF010 - Disponibilidade do item | Após o determinado item ser encontrado, o sistema deve exibir se eles está disponível para a reserva ou não. | Secretário, Docente |
| RF011 - Reserva de item | A reserva é feita mediante a disponibilidade do item . | Docente |
| RF012 - Kit padrão | O sistema deve possuir um kit pré-cadastrado. exemplo: kit básico. | Administrador, Secretário |
| RF013 - Cadastrar kit | Deve ser possível fazer o cadastro de novos kits. que atenda as necessidades de determinado evento ou aula. | Secretário |
| RF014 - Alterar kit | Deve ser possível alterar as informações de um kit já cadastrado. com a exceção do pré-cadastrado. | Secretário |
| RF015 - Excluir kit | Deve ser possível excluir um kit antes cadastrado. | Secretário |
| RF016 - Buscar kit | Deve ser possível pesquisar se determinado kit no sistema. Exemplo: kit aula. | Secretário, Docente |
| RF017 - Disponibilidade do kit | Após a busca de determinado kit, o sistema deve exibir se o mesmo está disponível ou não | Secretário, Docente |
| RF018 - Reserva de kit | A reserva de determinado kit é feita caso o mesmo esteja disponível. | Docente |

### Modelo Conceitual

Abaixo apresentamos o modelo conceitual usando o **YUML**.

 ![Modelo UML](yuml/monitoria-modelo.png)

O código que gera o diagrama está [Aqui!](yuml/monitoria-yuml.md). O detalhamento dos modelos conceitual e de dados do projeto estão no [Documento de Modelos](Modelo de Dados.md).

#### Descrição das Entidades

## Lista de Requisitos Não-Funcionais

Requisito                                 | Descrição   |
---------                                 | ----------- |
RNF001 - Deve ser acessível via navegador | Deve abrir perfeitamento no Firefox e no Chrome. |
RNF002 - Consultas deve ser eficiente | O sistema deve executar as consultas em milessegundos |
RNF003 - Log e histórico de acesso e funções | Deve manter um log de todos os acessos e das funções executadas pelo usuário |
RNF004 - O Sistema deve ser limpo | Deve ser intuitivo e possuir um fácil manuseio. |

## Riscos

Tabela com o mapeamento dos riscos do projeto, as possíveis soluções e os responsáveis.

Data | Risco | Prioridade | Responsável | Status | Providência/Solução |
------ | ------ | ------ | ------ | ------ | ------ |
10/10/2022 | Não aprendizado das ferramentas utilizadas pelos componentes do grupo | Alta | Todos | Vigente | Reforçar estudos sobre as ferramentas e aulas com a integrante que conhece a ferramenta |
15/10/2022 | Ausência por qualquer motivo do grupo | Média | Gerente | Vigente | Planejar o cronograma tendo em base a agenda do cliente |
30/10/2022 | Divisão de tarefas mal sucedida | Baixa | Gerente | Vigente | Acompanhar de perto o desenvolvimento de cada membro da equipe |
05/11/2022 | Implementação de protótipo com as tecnologias | Alto | Todos | Resolvido | Encontrar tutorial com a maioria da tecnologia e implementar um caso base do sistema |

### Referências

https://github.com/tacianosilva/eng-software-2/blob/master/docs/doc-visao.md
