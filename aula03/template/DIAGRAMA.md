# Diagrama de classes — Academia FitPará (depois do SRP)

```mermaid
classDiagram
    %% ===== EXEMPLO JÁ RESOLVIDO — imite este padrão nas classes de baixo =====
    class Aluno {
        -id: int
        -nome: str
        -plano: str
        -checkins: int
    }

    %% ===== AGORA VOCÊ: troque os ... pelos atributos/métodos de cada classe =====
    %% (use - para privado e + para público, como no exemplo do Aluno)
    class AlunoRepo {
        -_alunos: list
        +salvar(aluno)
        +buscar_por_nome(nome)
        +proximo_id()
    }

    class Notificador {
        +enviar(destinatario, mensagem)
    }

    class AcademiaService {
        -repo: AlunoRepo
        -notificador: Notificador
        +matricular(nome, plano)
        +check_in(nome)
    }

    %% Ligações (quem usa quem). As 3 já estão prontas — não precisa mexer.
    AcademiaService ..> Aluno : cria
    AcademiaService ..> AlunoRepo : usa
    AcademiaService ..> Notificador : usa