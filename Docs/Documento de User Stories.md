
# Documento Lista de User Stories

Documento construído a partido do **Modelo BSI - Doc 004 - Lista de User Stories** que pode ser encontrado no
link: https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](doc-visao.md) do Sistema de Controle de Materiais de Apoio(SCMA) detalhando como será implementada cada funcionalidade deste sistema de acordo com o usuário.
Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 21/09/2022 | 0.0.1   | Template e descrição do documento  | Márlem |
| 22/09/2022 | 0.0.2   | Detalhamento do User Story US01    | Márlem |
| 23/09/2022 | 0.0.3   | Atualização do Documento           | Ana Paula|
| 25/09/2022 | 0.0.4   | Revisão                            | Hiago  |
| 12/10/2022 | 1.0.0   | Documento completo com o detalhamento de todos os User Stories | Márlem     |
| 10/11/2022 | 1.0.1   | Correção de bugs  | Hiago |
| 20/12/2022 | 1.0.2   | Atualização e correção do documento | Ana Paula |



### User Story US01 - Manter Usuário

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve manter um cadastro de usuário que tem acesso ao sistema via login e senha. Um usuário tem os atributos nome, matrícula ,data de nascimento e mail.O usuário pode se registrar no sistema. O usuário administrador pode realizar as operações de adicionar, alterar, remover e listar os usuários comuns do sistema.|

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF001         | Cadastrar usuário	  |
| RF002         | Buscar usuário	    |
| RF003         | Alterar usuário	    |
| RF004         | Deletar usuário     |
| 

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 8 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Márlem                              | 
| **Desenvolvedor**         | Hiago                               | 
| **Revisor**               | Márlem                              | 
| **Testador**              | Ana Paula                           | 


### User Story US02 - Manter item 

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O item de kit de apoio tem código, descrição e equantidade disponível,  é cadastrado no sistema pelo usuário administrador que faz login e disponibiliza o item para emprestimo. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF005         |Cadastrar item	           |
| RF006         |Tipo do item	             |
| RF007         |Buscar item               |
| RF008         |Alterar item	             |
| RF009         |Excluir item              |
| RF010         |Disponibilidade do item   |
| RF011         | Reserva de item          | 

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 8 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Márlem                              | 
| **Desenvolvedor**         | Hiago                               | 
| **Revisor**               | Márlem                              | 
| **Testador**              | Ana Paula                           | 

### User Story US03 - Manter kit 

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O  kit de apoio tem código, descrição e equantidade disponível,  é cadastrado no sistema pelo usuário administrador que faz login e disponibiliza o kit para emprestimo. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF012         | Kit padrão                        |
| RF013         | Cadastrar kit	                    |
| RF014         | Alterar kit	                      |
| RF015         | Excluir kit	                      |
| RF016         | Buscar kit	                      |
| RF017         | Disponibilidade do kit	          |
| RF018         | Reserva de kit                    |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 8 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Márlem                              | 
| **Desenvolvedor**         | Hiago                               | 
| **Revisor**               | Márlem                              | 
| **Testador**              | Ana Paula                           | 



### User Story US04 - Manter Emprestimos

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | A partir do login e senha o usuário tem acesso ao sistema onde verifica a disponibilidade de kit ou item e efetiva o empréstimo, após a utilização , repete o processo de login e efetiva a devolução do kit emprestado.  |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF019         | Realizar emprestimo de kit de apoio     |
| RF020         | Devolução de kit de apoio               |
| RF021         | Realizar Reserva                        |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 8 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Márlem                              | 
| **Desenvolvedor**         | Hiago                               | 
| **Revisor**               | Márlem                              | 
| **Testador**              | Ana Paula                           | 





| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | Descrever o teste de aceitação 01 do US01 |
| **TA01.02** | Descrever o teste de aceitação 02 do US01 |
| **TA01.03** | Descrever o teste de aceitação 03 do US01 |

