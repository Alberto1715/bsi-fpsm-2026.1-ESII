# Análise — as 3 responsabilidades da classe `Academia` (v1.0)

**Sua tarefa (Parte 2 da atividade, 0,3):** responder com **suas palavras**
(2–4 frases por item), olhando o arquivo `academia.py` da pasta da aula.
Substitua cada `...` pela sua resposta.

---

## 1. Quais são as 3 responsabilidades grudadas na classe `Academia`?
Escreva no formato "a classe faz **X** e **Y** e **Z**":

> A classe faz o gerenciamento das regras de negócio guardando os dados dos alunos, faz a interação de tela com o usuário através de menus e inputs, e também faz o disparo de mensagens de avisos e notificações diretamente para os matriculados.

## 2. Aponte, no código, **uma linha** de cada responsabilidade
(diga o número da linha e cole o trecho)

- **Regra de negócio** (cálculo / contagem): linha 41 — `aluno["checkins"] += 1`
- **Tela** (interface com o usuário): linha 15 — `nome = input("Nome do aluno: ")`
- **Notificação** (aviso ao aluno): linha 32 — `self.notificador.enviar(nome, "Bem-vindo à Academia FitPará!")`

## 3. Como o SRP separa essas responsabilidades?
Diga **em qual componente** cada responsabilidade passa a morar:

> O fluxo geral de execução e a interface de tela com o usuário continuam sob a responsabilidade do arquivo principal. A lógica de gerenciar dados e persistência vai para o repositório, enquanto a responsabilidade de formatar e disparar os avisos passa a morar exclusivamente no componente `Notificador`.

## 4. Por que ficou melhor? Cite **um** RNF
(manutenibilidade, testabilidade **ou** extensibilidade — veja `docs/requisitos.md`)
e explique em 1–2 frases:

> Ficou melhor para o requisito não-funcional de **manutenibilidade**. Caso o meio de comunicação mude futuramente do WhatsApp para SMS ou e-mail, modificaremos apenas o arquivo isolado do notificador, sem correr o risco de quebrar as regras de negócio centrais do sistema.