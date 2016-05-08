class Animal(object):
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def identificao(self):
        print("Nome: {} | Cor: {}".format(self.nome, self.cor))


class Cao(Animal):
    def __init__(self, raca, *args, **kwargs):
        super(Cao, self).__init__(*args, **kwargs)
        self.raca = raca

    def identificao(self):
        print("Nome: {} | Cor: {} | Raça {}".format(
            self.nome, self.cor, self.raca))


if __name__ == "__main__":
    animal = Animal(nome="Macaco", cor="Marrom")
    animal.identificao()

    cao = Cao(nome="Rex", cor="Preto", raca="Rotweiler")
    cao.identificao()
