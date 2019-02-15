# -*- coding: utf-8 -*-
import os
import re
import sys
from random import shuffle

numeros = ["A", "2", "3", "4", "5",
           "6", "7", "8", "9", "10",
           "Q", "J", "K"]
naipes = ["♣", "♦", "♥", "♠"]
baralho = [numero+naipe for numero in numeros for naipe in naipes]


def cabecalho(saldo, mao_jogador, mao_dealer, aposta_atual):
    status = os.system('cls')  # windows
    if status != 0:
        os.system('clear')  # linux
    pontos_jogador = contar_pontuacao(mao_jogador)
    print(
        "{0}BLACKJACK{1} Saldo: {2} "
        "| Aposta Atual: {3} "
        "| Seus pontos: {4}".format(
            "-~"*20, "-~"*20, saldo, aposta_atual, pontos_jogador))
    mostrar_cartas(mao=mao_dealer, jogador="Dealer", ocultar_uma=True)
    mostrar_cartas(mao=minha_mao, jogador="Rafael", ocultar_uma=False)
    print("{0}-~-~-~-~-{1}\n".format("-~"*20, "-~"*20))


def mostrar_cartas(mao, jogador, ocultar_uma=True):
    if ocultar_uma:
        oculta = mao[:-1] + ["XX"]
        print("Cartas do {0}: {1}".format(jogador, ", ".join(oculta)))
    else:
        print("Cartas do {0}: {1}".format(jogador, ", ".join(mao)))


def comprar(baralho, qtde=1):
    """
    Comprar cartas do baralho

    Args:
        baralho (list): baralho composto por lista
        qtde (int): quantidade de cartas para comprar
    """
    if not baralho:
        return []
    shuffle(baralho)
    return [baralho.pop() for i in range(qtde)]


def apostar(saldo=None, aposta=None, dobrada=False):
    """
    Apostar fichas e remover saldo

    Args:
        saldo (int): saldo do jogador
        aposta (int): ficha que deseja apostar
        dobrada (boolean): aposta dobrada
    """
    try:
        aposta = int(aposta)
        saldo = int(saldo)

        if aposta > 200:
            raise Exception('Aposta', 'A aposta máxima é de 200 por turno')

        if (saldo - aposta) < 0:
            raise Exception('Saldo', 'Saldo insuficiente')

        if not ((aposta % 1 == 0 or
                 aposta % 5 == 0 or
                 aposta % 25 == 0 or
                 aposta % 100 == 0)):
            return [saldo, aposta]

        if dobrada:
            return [saldo - (aposta*2), aposta*2]

        return [saldo - aposta, aposta]

    except ValueError:
        print(
            "ValueError: Valores aceitos são multiplos "
            "1, 5, 25 e 100 e abaixo de 200")
        return [saldo, 0]

    except Exception as ex:
        tipo, msg = ex.args
        print("Erro {0}: {1}".format(tipo, msg))
        if tipo == "Aposta":
            return [saldo, 0]
        return [saldo, aposta]


def contar_pontuacao(mao=None):
    """
    Conta a pontuação atual da mão

    Args:
        mao (list): lista de cartas na mão
    """
    pontos = 0
    for carta in mao:
        if re.search("A.*", carta):
            pontos += 1
        elif re.search("2.*", carta):
            pontos += 2
        elif re.search("3.*", carta):
            pontos += 3
        elif re.search("4.*", carta):
            pontos += 4
        elif re.search("5.*", carta):
            pontos += 5
        elif re.search("6.*", carta):
            pontos += 6
        elif re.search("7.*", carta):
            pontos += 7
        elif re.search("8.*", carta):
            pontos += 8
        elif re.search("9.*", carta):
            pontos += 9
        elif re.search("10.*", carta):
            pontos += 10
        elif re.search("[QJK].*", carta):
            pontos += 10
    return pontos


def chorar_pra_mamae():
    """
    Surrender!!
    """
    print("Você se rendeu :-o")
    sys.exit(0)


def menu():
    """
    Cria um menu de opções
    """
    msg = ("Jogar: O que gostaria de fazer?\n"
           "\t1. Apostar\n"
           "\t2. Comprar carta\n"
           "\t3. Dobrar aposta\n"
           "\t4. Parar/Finalizar jogada\n"
           "\t5. Chorar pra mãe\n"
           "Digite número desejado: ")
    return msg

if __name__ == "__main__":
    minha_mao = []
    mao_dealer = comprar(baralho, qtde=2)
    aposta_atual = 0
    saldo = 2000

    while True:
        if saldo == 0:
            print("Seu saldo chegou a 0 você perdeu TUDO!")
            sys.exit(0)
        if saldo >= 4000:
            print("Saia deste cassino! Você ganhou demais por HOJE!")
            sys.exit(0)

        cabecalho(saldo, minha_mao, mao_dealer, aposta_atual)
        resposta = input(menu())
        if resposta == "1":
            valor_aposta = input("Deseja apostar quanto?\n")
            saldo_anterior = saldo
            saldo, aposta = apostar(
                saldo=saldo,
                aposta=valor_aposta,
                dobrada=False)
            aposta_atual += aposta
            if aposta_atual > 200:
                print("Erro Aposta: A aposta máxima é "
                      "de 200 por turno, você tentou "
                      "apostar {0}".format(aposta_atual))
                saldo = saldo_anterior
                aposta_atual -= aposta
            input("\nPressione enter para continuar...")
        elif resposta == "2":
            if len(minha_mao) == 0:
                minha_mao += comprar(baralho, qtde=2)
            else:
                minha_mao += comprar(baralho, qtde=1)
            pontos_jogador = contar_pontuacao(minha_mao)

            if pontos_jogador > 21:
                mostrar_cartas(
                    mao=mao_dealer, jogador="Dealer", ocultar_uma=False)
                mostrar_cartas(
                    mao=minha_mao, jogador="Rafael", ocultar_uma=False)

                pontos_dealer = contar_pontuacao(mao_dealer)
                print("Você perdeu!! Você estourou pontuação!!")

                print("Sua pontuação: {}".format(pontos_jogador))
                print("Pontuação do Dealer: {}".format(pontos_dealer))

                aposta_atual = 0
                minha_mao = []
                mao_dealer = comprar(baralho, qtde=2)
                input("\nPressione enter para continuar...")

        elif resposta == "3":
            if not aposta_atual:
                print("Você ainda não apostou! Aposte primeiro depois dobre!")
                input("\nPressione enter para continuar...")
                continue
            if len(minha_mao) > 2:
                print(
                    "Você já comprou cartas! "
                    "Não pode mais dobrar a aposta!")
                input("\nPressione enter para continuar...")
                continue
            saldo_anterior = saldo
            saldo, aposta = apostar(
                saldo=saldo,
                aposta=aposta_atual,
                dobrada=False)
            aposta_atual += aposta
            if aposta_atual > 200:
                print("Erro Aposta: A aposta máxima é "
                      "de 200 por turno, você tentou "
                      "apostar {0}".format(aposta_atual))
                saldo = saldo_anterior
                aposta_atual -= aposta
            input("\nPressione enter para continuar...")
        elif resposta == "4":
            if not aposta_atual:
                print(
                    "Você ainda não apostou! Aposte primeiro finalize jogada!")
                input("\nPressione enter para continuar...")
                continue

            if len(minha_mao) == 0:
                print(
                    "Você ainda não comprou cartas! "
                    "Compre cartas primeiro depois finalize jogada!")
                input("\nPressione enter para continuar...")
                continue

            pontos_dealer = contar_pontuacao(mao_dealer)
            while not (17 <= pontos_dealer <= 21) and not (pontos_dealer > 21):
                mao_dealer += comprar(baralho, qtde=1)
                pontos_dealer = contar_pontuacao(mao_dealer)

            mostrar_cartas(mao=mao_dealer, jogador="Dealer", ocultar_uma=False)
            mostrar_cartas(mao=minha_mao, jogador="Rafael", ocultar_uma=False)

            pontos_jogador = contar_pontuacao(minha_mao)

            if pontos_jogador > 21:
                print("Você perdeu!! Você estourou pontuação!!")
            elif pontos_dealer > 21:
                print("Você ganhou!! Computador estourou pontuação!!")
                saldo += aposta_atual*2
            elif pontos_jogador < pontos_dealer:
                print("Você perdeu!!")
            elif pontos_jogador > pontos_dealer:
                print("Você ganhou!!")
                saldo += aposta_atual*2
            elif pontos_jogador == pontos_dealer:
                print("Empate!! Ninguém ganhou saldo!!")
                saldo += aposta_atual
            else:
                print("Whatever!!")

            print("Sua pontuação: {}".format(pontos_jogador))
            print("Pontuação do Dealer: {}".format(pontos_dealer))

            aposta_atual = 0
            minha_mao = []
            mao_dealer = comprar(baralho, qtde=2)
            input("\nPressione enter para continuar...")

        elif resposta == "5":
            chorar_pra_mamae()
        else:
            continue
