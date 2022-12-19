# Contagem de Pontos de Função

A contagem em **Pontos de Função (PF)** permite a determinação do **Tamanho Funcional** do projeto de software.
A análise de ponto de função (APF) é um processo para a identificação e contagem das funcionalidades baseadas nos conceitos 
de **Funções de Dados** e **Funções de Transação**. 

Os conceitos relacionados com dados são os **Arquivos de Lógica Interna (ALI)** e os **Arquivos de Interface Externa (AIE)**, 
e os conceitos relacionados com operações externas a fronteira do sistema são: 
**Entrada Externa (EE)**, **Consulta Externa (CE)** e **Saída Externa (SE)**.

Existem várias práticas de contagem, cada uma com suas especificidades.

## Contagem Indicativa

Na contagem indicativa (Ci) só é necessário conhecer e analisar as **Funções de Dados**. Desta forma, 
os **ALI**s (Arquivos Lógicos Internos) com o valor de *35 PF* cada e os **AIE**s (Arquivos de Interface Externa) com o valor de *15 PF* cada.

### Modelo de Dados 

```mermaiderDiagram
    Usuario }o--|{ Cadastro : login
    Usuario ||--|| Item : Reserva
    Usuario }|--o{ Kit : Reserva
    Usuario }o--o{ Reserva : Devolução
```

### Contagem Indicativa

| Função de Dado  | Entidades Relacionadas | Tamanho em PF |
| --------------- | ---------------------- | :-----------: |
| ALI Usuário     | Tipos de Usuários      | 45 PF         |
| ALI Projeto     | Projeto                | 50 PF         |
| ALI Laboratorio | Laboratorio            | 35 PF         |
| AIE Endereço    | Endereço               | 15 PF         |
| **Total**       | **Ci**                 | **120 PF**    |

### Duração e custo considerando produtividade 8h/PF e Ci = 120 PF 
120 PF * 8h/PF= 960H
960h/8h = 120 Dias

### Duração e custo considerando produtividade 1h/PF e Ci = 84 PF

| Entidades Relacionadas     |  PF  | Duração | Custo para o projeto| 
|--------------------------- |------| ------- | --------------------|
| Administrador              |  15  |   15h   |       R$ 81         |
| Usuário                    |  45  |   35h   |       R$ 189        |
| Projeto                    |  50  |   42h   |       R$ 501        |
| Laboratório                |  10  |   15h   |       R$ 81         |
| Total                      |  120 |   107h  |       R$ 852        |

## Contagem Estimativa (Ce)

Na Ce todas as funções de dados são classificados como baixa complexidade.

| ALI/AIE           | Entidades Relacionadas     | PF |
|------------------ |--------------------------- |----|
| AIE Administrador | Administrador              | 5  |
| ALI Usuário       | Usuário                    | 7  |
| ALI Projeto       | Projeto                    | 7  |
| ALI Laboratório   | Laboratório                | 7  |
| ALI Endereço      | Endereço                   | 7  |
|                   | Total de Dados             | 33 |


Na Ce todas as operações elementares são classificadas como de média complexidade: 
**EE** tem 4 PF e **SE** tem 5 PF.


| Operação                | Tipo | Complexidade    |  PF  |
|-------------------------|------|-----------------|------|
| Cadastrar Usuário       |  EE  | Média           |  4   |
| Deletar Usúario         |  EE  | Média           |  4   |
| Editar Usúario          |  EE  | Média           |  4   |
| Cadastrar Item          |  EE  | Média           |  4   |
| Deletar Item            |  EE  | Média           |  4   |
| Editar Item             |  EE  | Média           |  4   |
| Cadastrar Kit           |  EE  | Média           |  4   |
| Deletar Kit             |  EE  | Média           |  4   |
| Editar Kit              |  EE  | Média           |  4   |
| Reservar Item           |  SE  | Média           |  5   |
| Reservar Kit            |  SE  | Média           |  5   |
|                         |      | Total           |  46  |

Tamanho Funcional: Dados + Operações

__Ce__ = 33 PF + 46 PF = 79 PF
