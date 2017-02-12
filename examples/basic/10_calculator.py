while True:
    try:
        control = input("Para sair digite q, para continuar digite c: ")

        if control == 'q':
            break
        elif control == 'c':
            pass
        else:
            print("Opção inválida!")
            continue

        x = float(input("Digite primeiro operador: "))
        y = float(input("Digite segundo operador: "))
        operation = input("Digite a operação [+ - / *]: ")

        if operation == "+":
            print("{} + {} = {}".format(x, y, x + y))
        elif operation == "-":
            print("{} - {} = {}".format(x, y, x - y))
        elif operation == "*":
            print("{} * {} = {}".format(x, y, x * y))
        elif operation == "/":
            print("{} / {} = {}".format(x, y, x / y))
        else:
            print("Operação não suportada!")
            continue

    except ValueError:
        print("Digite somente números reais!")
    except ZeroDivisionError:
        print("Impossível dividir por 0! Informe outro número!")
    except KeyboardInterrupt:
        print("Não vai sair não cuzão!")
    except:
        print("Erro bizarro!")
