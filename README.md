# Sistema Bancário Simples em Python

Sistema de gerenciamento financeiro simples, implementado em Python, que permite realizar depósitos, saques e verificar o extrato da conta. O sistema possui limitações, como um valor máximo por saque, um limite de saques permitidos por sessão e o gerenciamento de contas e usuários.

## Funcionalidades

- **Depositar**: Realiza o depósito de um valor informado pelo usuário.
- **Sacar**: Permite que o usuário faça saques, com as seguintes limitações:
  - Valor máximo de saque: R$ 500.
  - Número máximo de saques: 3 por sessão.
  - Limite de saldo: Não é permitido sacar um valor superior ao saldo disponível.
- **Extrato**: Exibe um extrato das movimentações realizadas (depósitos e saques), junto com o saldo atual da conta.
- **Limite de Saques**: O sistema permite no máximo 3 saques por sessão. Se o usuário atingir esse limite, não será possível realizar mais saques até o reinício da sessão.
- **Gerenciamento de Usuários**: O sistema permite o cadastro de usuários, identificados pelo CPF, com informações como nome, data de nascimento e endereço.
- **Gerenciamento de Contas**: O sistema permite a criação de contas bancárias associadas aos usuários, com uma agência e número de conta.

## Fluxo de Operações

1. **Cadastro de Usuário**: O usuário pode ser registrado informando o CPF, nome, data de nascimento e endereço.
2. **Criação de Conta**: O usuário pode criar uma conta informando o CPF associado, sendo necessário que o CPF já esteja cadastrado.
3. **Operações Bancárias**: Após criar uma conta, o usuário pode realizar depósitos, saques e consultar seu extrato bancário.

---



Este projeto foi desenvolvido durante o **Bootcamp da Trilha de Python** da **DIO**. Através deste curso, aprendi conceitos importantes sobre Python, lógica de programação, controle de fluxo e manipulação de dados, aplicados diretamente neste projeto de sistema bancário.
