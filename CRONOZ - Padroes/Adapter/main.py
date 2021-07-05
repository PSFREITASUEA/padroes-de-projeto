# o que queremos (alvo)
class Duck:

	def quack(self) -> str:
		return "Quack!"

	def fly(self) -> str:
		return "I'm flying!"


# o que temos (serviço)
class Turkey:

	def gobble(self) -> str:
		return "Gooble gooble"

	def fly_short(self) -> str:
		return "I'm flying a short distance"


# adaptador de herança múltipla: serviço -> alvo
class Adapter(Turkey, Duck):

	def quack(self) -> str:
		return Turkey.gobble()
	
	def fly(self) -> str:
		return (Turkey.fly_short()+"\n")*5


if __name__ == "__main__":
	Duck = Duck()
	print(f"The Duck says:\n{Duck.quack()}\n{Duck.fly()}\n")

	Turkey = Turkey()
	print(f"The Turkey says:\n{Turkey.gobble()}\n{Turkey.fly_short()}\n")

	Adapter = Adapter()
	print(f"The TurkeyAdapter says:\n{Adapter.quack()}\n{Adapter.fly()}")
