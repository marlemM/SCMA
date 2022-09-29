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

O sistema poderá ser utilizado por dois tipos de usuários. Temos os seguintes perfis/atores:

Perfil                                 | Descrição   |
---------                              | ----------- |
Administrador | Este usuário realiza os cadastros base e pode realizar qualquer função.
Docentes | Este usuário pode retirar kit de apoio e realizar a devolução,verificar disponibilidade de kit, etc.

## Lista de Requisitos Funcionais

Requisito                                 | Descrição   | Ator |
---------                                 | ----------- | ---------- |
RF001 - Manter um cadastro de Centros | Um centro representa uma unidade administrativa da Universidade. Um centro tem código, nome, sigla, endereço e site. | Administrador |
RF002 - Manter um cadastro de kit de apoio | Um kit de apoio tem código e descrição. | Administrador |
RF003 - Realizar emprestimo de kit de apoio | Um emprestimo tem login. código, data de emprestimo | Docente |
RF004 - Devolução kit de apoio | Uma devolução  tem código e data de devolução. | Docente |
RF005 - Realizar cadastro, alteração e exclusão de itens | Um objeto deve possuir cadastro com código próprio. | Administrador |
RF006 - Realizar uma reserva do item ou kit | O docente deve ser capaz de reservar itens e kits. | Docente |
RF007 - Deve haver um perfil com todas as informções sobre o usuário | deve preencher com dados importantes como matricula, nome, email, telefone e departamento (docente). | Todos |
RF008 - O sistema deve possuir a escolha de login, o usuário deve se identificar como adminastrador, secretário ou docente | O administrador é unico que pode interagir com o banco de dados, sendo um super-usuário; O secretário pode cadastrar e editar itens e kits; O Docente pode somente procurar, reservar e pegar um item ou kit emprestado. | Todos |
RF009 - Deve haver uma multa de três dias para cada dia de atraso na devolução | A multa é acumulativa, o docente não pode realizar emprestimos ou reservar enquanto estiver penalizado. | Docente |

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
