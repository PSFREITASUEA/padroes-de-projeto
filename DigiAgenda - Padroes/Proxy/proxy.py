from abc import ABC, abstractmethod


class Assunto(ABC):
    # A interface do Assunto declara operações comuns para o AssuntoReal e
    # o Proxy. Desde que o cliente trabalhe com a AssuntoReal usando esta
    # interface, vamos poder passar para ela um proxy em vez de um Assunto real.
    @abstractmethod
    def solicitacao(self) -> None:
        pass


class AssuntoReal(Assunto):
    # O AssuntoReal contém algumas lógicas de negócios centrais. Normalmente, AssuntosReais são
    # capazes de fazer algum trabalho útil que também pode ser muito lento ou sensível -
    # por exemplo, corrigindo dados de entrada. Um proxy pode resolver esses problemas sem qualquer
    # alterações no código de AssuntoReal.

    def solicitacao(self) -> None:
        print("AssuntoReal: manuseando solicitacao.")


class Proxy(Assunto):
    # O Proxy tem uma interface identica a AssuntoReal.

    def __init__(self, assunto_real: AssuntoReal) -> None:
        self._assunto_real = assunto_real

    def solicitacao(self) -> None:
        # Os aplicativos mais comuns do padrão Proxy são o carregamento lento,
        # cache, controle de acesso, registro, etc. Um Proxy pode realizar um
        # dessas coisas e depois, dependendo do resultado, passar a execução para
        # o mesmo método em um objeto AssuntoReal vinculado.

        if self.checar_acesso():
            self._assunto_real.solicitacao()
            self.logar_acesso()

    def checar_acesso(self) -> bool:
        print("Proxy: Verificando o acesso antes de disparar uma solicitação real.")
        return True

    def logar_acesso(self) -> None:
        print("Proxy: Registrando o tempo de solicitação.", end="")


def cliente(Assunto: Assunto) -> None:
    # O código do cliente deve funcionar com todos os objetos (assuntos e
    # proxies) através da interface Assunto para suportar ambos os assuntos reais
    # e proxies. 

    Assunto.solicitacao()


if __name__ == "__main__":
    print("Client: Executando o código do cliente com um Assunto real:")
    assunto_real = AssuntoReal()
    cliente(assunto_real)

    print("")

    print("Client: Executando o mesmo código de cliente com um proxy:")
    proxy = Proxy(assunto_real)
    cliente(proxy)