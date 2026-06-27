class Notificador:
    """Cuida apenas de enviar notificações ao aluno."""

    def enviar(self, destinatario, mensagem):
        # Mostra a notificação no formato exato que o professor pediu:
        print(f"[WhatsApp para {destinatario}] {mensagem}")