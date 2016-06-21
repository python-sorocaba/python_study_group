# -*- coding: utf-8 -*-
import random
from numbers import Integral


class Tamagochi:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.fome = random.randint(1, 100)
        self.saude = random.randint(1, 100)

    def __repr__(self):
        return (u"Tamagochi(nome={0}, idade={1}, saude={2}, "
                u"fome={3}, humor={4})").format(
            self.nome, self.idade, self.saude, self.fome, self.humor)

    @property
    def nome(self):
        print("Call method nome with decorator @property")
        return self.__nome

    @nome.setter
    def nome(self, nome):
        print("Call method nome with decorator @nome.setter")
        self.__nome = nome

    @property
    def fome(self):
        return self.__fome

    @fome.setter
    def fome(self, fome):
        if not isinstance(fome, Integral):
            raise ValueError('Fome deve ser um número inteiro!')

        if fome > 0 and fome < 100:
            self.__fome = fome
        else:
            raise ValueError('Fome deve ser entre 0 e 100!')

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if not isinstance(idade, Integral):
            raise ValueError('Idade deve ser um número inteiro!')

        if idade >= 1 and idade <= 50:
            self.__idade = idade
        else:
            raise ValueError('Idade deve ser entre 1 e 50!')

    @property
    def humor(self):
        """This method dont have setter then read-only"""
        if self.fome <= 10 and self.saude <= 10:
            return u"CUIDE DA SUA VIDA! TO PUTO!"
        elif self.fome <= 20 and self.saude <= 20:
            return u"NÃO TO FELIZ!"
        elif self.fome <= 30 and self.saude <= 30:
            return u"NÃO TEM O QUE FAZER!?"
        elif self.fome <= 40 and self.saude <= 40:
            return u"O QUE VC QUER?"
        elif self.fome <= 50 and self.saude <= 50:
            return u"NEM FELIZ NEM TRISTE"
        elif self.fome <= 60 and self.saude <= 60:
            return u"FELIZ"
        elif self.fome <= 80 and self.saude <= 80:
            return u"MAOMENOS FELIZ"
        elif self.fome > 80 and self.saude > 80:
            return u"FELIZÃO"

    def metodo_callable():
        return "oi"
