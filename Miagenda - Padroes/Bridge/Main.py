from abc import ABC, abstractmethod

#Implementação da classe hierárquica TV
class Implementation_TV(ABC): 
    @abstractmethod  
    def on_tv (self) -> str:
      pass

    @abstractmethod
    def off_tv (self) -> str:
      pass

    def tune_Channel(self, channel) -> str:
      self.channel = channel

class Sony (Implementation_TV): 
    def operation_implementation(self) -> str:
      return "Dispositivo Sony da superclasse TV"
    
    def on_tv (self) -> str:
      return (f"{self.Implementation_TV.on_tv()}")
    
    def off_tv (self) -> str:
      return (f"{self.Implementation_TV.off_tv()}")

    def tune_Channel(self):
      print("Sintonizar canal")

class RCA (Implementation_TV):  
   def operation_implementation(self) -> str:
     return "Dispositivo RCA da superclasse TV"

   def on_tv (self) -> str:
     return "TV Ligada!"
    
   def off_tv (self) -> str:
     return "TV Desligada!"
    
   def tune_Channel(self, channel) -> str:
     return "Sintonizar canal"

#Classe de Abstração para Controle Remoto 
class RemoteControl (Implementation_TV):
    
    #Argumento como o atributo "implementor"
    
    def __init__(self, implementor: Implementation_TV) -> None:
      self.implementor = implementor

    #metodos do Controle Remoto
    def on_tv (self) -> str:
      implementor.on_tv

    def off_tv (self) -> str:
      implementor.off_tv
    
    def set_Channel(chanel) -> str:
      implementor.tune_Channel(channel)

#classe concreta para o Controle (interface)
class ConcreteRemote(RemoteControl): 
    currentStation = 0
    def __init__(self, implementor, currentStation: RemoteControl) -> None:
        self.implementor = implementor
        self.currentStation = currentStation

    def on_tv (self) -> str:
      return "TV Ligada!"

    def off_tv (self) -> str:
      return "TV Desligada"

    def next_Channel () -> None:
      currentStation +=1
      set_Channel(currentStation);

    def previous_Channel () -> None:
      currentStation -=1
      set_Channel(currentStation)

#----------------------------- Interação do Usuário-----------------------------
def user_televisao(tv_abstracao: Sony) -> None:
   print("Ligar: ")
   print(tv_abstracao.on_tv(), "\n")
   print("Desligar: ")
   print(tv_abstracao.off_tv(), "\n")
   
if __name__ == "__main__":

    currentStation1 = 2
    print("-----Televisao 1-----")
    implementation = Sony()    
    controle = ConcreteRemote(implementation, currentStation1)
    user_televisao(controle)
    
    currentStation2 = 5
    print("-----Televisao 2-----")
    implementation = RCA()    
    controle = ConcreteRemote(implementation, currentStation2)
    user_televisao(controle)
