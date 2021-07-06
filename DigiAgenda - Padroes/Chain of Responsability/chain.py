from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    # a interface Handler declara um método para construir a cadeia de handlers
    # ela também declara o método para executar uma solicitação

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    # o comportamento padrão da cadeia pode ser implementado dentro da classe
    # handler
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler

        # retornar o handler daqui vai nos permitir lincar handlers
        # de um jeito conveniente, como se fosse uma lista encadeada
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

# Todos os handlers concretos vão fazer uma solicitação ou passar para o próximo handler
# na cadeia


class SpamHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "SPAM":
            return f"O tipo do e-mail é {request}"
        else:
            return super().handle(request)


class FanHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "FanMail":
            return f"O tipo do e-mail é {request}"
        else:
            return super().handle(request)


class ComplaintHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Reclamação":
            return f"O tipo do e-mail é {request}"
        else:
            return super().handle(request)

class NewLockHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Solicitação":
            return f"O tipo do e-mail é {request}"
        else:
            return super().handle(request)

def codigo_cliente(handler: Handler) -> None:
    for email in ["Reclamação", "Solicitação", "SPAM"]:
        print(f"\n-> Cliente: qual o tipo de e-mail para '{email}'?")
        result = handler.handle(email)
        if result:
            print(f"{result}", end="\n")
        else:
            print(f"{email} não foi encontrado.", end="\n")


if __name__ == "__main__":
    fan_mail = FanHandler()
    new_lock = NewLockHandler()
    reclamacao = ComplaintHandler()

    fan_mail.set_next(new_lock).set_next(reclamacao)
    # o cliente deve ser capaz de mandar uma solicitação para qualquer handler
    #  não somente o primeiro na cadeia
    print("Chain: FanMail > NewLock > Reclamação")
    codigo_cliente(fan_mail)
    print("\n")