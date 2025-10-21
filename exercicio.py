class Animal:
    def __init__(self, nome: str, idade:  int):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "O animal emite um som." 

    def apresentar(self):
        return f"Olá sou {self.nome} e tenho {self.idade} anos." 

class Cachorro(Animal): #Subclasse Cachorro
    def __init__(self, nome: str, idade: int, raca: str):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        return "Au! Au!"


class Gato(Animal): #Subclasse Gato
    def __init__(self, nome: str, idade: int, cor_pelo: str):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        return "Miau!"

class Vaca(Animal): #Subclasse Vaca
    def __init__(self, nome: str, idade: int, producao_leite_litros: float):
        super().__init__(nome, idade)
        self.__producao_leite_litros = producao_leite_litros

    def emitir_som(self):
        return "Muuu!"
    
    def apresentar(self):
        return (f"Olá, meu nome é {self.nome}, tenho {self.idade} anos "
                f"e produzo {self.__producao_leite_litros} litros de leite por dia.")
        
    #Método getter
    def obter_producao_leite(self):
        return (self.__producao_leite_litros)
    
    #Método setter
    def registrar_ordenha(self, litros):
        self.__producao_leite_litros = litros
        print(f"A nova produção de leite foi de {self.__producao_leite_litros}")



cachorro = Cachorro("Toddy",4, "Lulu da Pomerania")
gato = Gato("Banguela",2, "Preto")
vaca = Vaca("Tessy", 4, 12.5)

animais = [cachorro, gato, vaca]
    
for animal in animais:
    print(animal.apresentar())
    print(animal.emitir_som())
    if isinstance(animal, Cachorro):
        print(f"Minha raça é: {animal.raca}")
    if isinstance(animal, Gato):
        print (f"O meu pelo é: {animal.cor_pelo}")
    if isinstance(animal, Vaca):
        print (f"A minha produção de leite é: {animal.obter_producao_leite()}")