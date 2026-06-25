# Diagnóstico do Sistema de Empréstimo — Alberto gilson de oliveira pereira 

## Problema 1

- O que a documentação diz:
  A regra RN02 informa que o prazo mínimo de empréstimo é de 1 dia.
- O que o código faz:
  O método `registrar()` não verifica se a quantidade de dias é maior que zero e aceita qualquer valor informado.
- Por que é um problema:
  O sistema pode registrar empréstimos com prazo inválido, como 0 ou dias negativos.
- Já documentado? Não.

---

## Problema 2

- O que a documentação diz:
  O caso de uso UC03 informa que, quando não houver empréstimos em atraso, o sistema deve exibir a mensagem "Nenhum empréstimo em atraso".
- O que o código faz:
  O método `listar_atrasados()` simplesmente termina sem mostrar nenhuma mensagem quando não encontra empréstimos atrasados.
- Por que é um problema:
  O usuário pode pensar que o sistema travou ou que ocorreu algum erro.
- Já documentado? Não.

---

## Problema 3

- O que a documentação diz:
  O requisito RI02 informa que toda operação concluída com sucesso deve exibir uma mensagem de confirmação ao usuário.
- O que o código faz:
  O método `registrar()` apenas imprime uma mensagem simulando um e-mail e retorna `True`, sem confirmar claramente que o empréstimo foi registrado.
- Por que é um problema:
  O usuário não recebe uma confirmação explícita de que a operação foi realizada com sucesso.
- Já documentado? Não.

---

## Problema 4

- O que a documentação diz:
  O requisito RI03 informa que toda operação inválida deve exibir uma mensagem de erro descritiva.
- O que o código faz:
  No menu principal (`main()`), quando o usuário informa uma opção inválida, nada acontece e o menu apenas é exibido novamente.
- Por que é um problema:
  O usuário não sabe que digitou uma opção incorreta e pode ficar confuso.
- Já documentado? Não.

---

## Problema 5

- O que a documentação diz:
  A Tabela de Dívida Técnica (DT04) informa que o cálculo da multa está duplicado em dois métodos e deve ser corrigido futuramente.
- O que o código faz:
  O mesmo cálculo de multa aparece tanto no método `devolver()` quanto em `listar_atrasados()`.
- Por que é um problema:
  Se a regra da multa mudar, será necessário alterar os dois trechos do código, aumentando a chance de erros.
- Já documentado? Sim.
