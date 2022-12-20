# Diagrama de Classes usando YUML - SCMA

Abaixo apresentamos o modelo conceitual usando o **YUML**.

 ![Modelo UML](digrama_scma.png)

## Código do Modelo do Sistema SCMA

O código que gera o diagrama é apresentado abaixo.
```
[Kit]
[Item]
[Usuário]
[Reserva]
[Usuário]<>->[Docente]
[Usuário]<>->[Secretário]
[Usuário]<>->[Administrador]
[Usuário]<>-[Reserva]
[Kit]<>-[Reserva]
[Kit|itens]++-itens*>[Item]
[Empréstimo]<>->[Usuário]
[Empréstimo]++->[Kit]
[Empréstimo]<>[Reserva]
```
