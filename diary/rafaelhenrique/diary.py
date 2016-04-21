# -*- coding: utf-8 -*-
import json
import os
from collections import OrderedDict


def create_structure(msg="Digite um campo novo [c=cancelar]: "):
    """Create structure.json with our model of diary"""
    structure = {}
    while True:
        key = input(msg)
        if key == "c":
            break
        structure.update({key: None})

    with open("structure.json", "w", encoding="utf-8") as fp:
        fp.write(json.dumps(structure))

    return True


def read_structure():
    """Read created structure.json with our model of diary"""
    if os.path.isfile("structure.json"):
        with open("structure.json", "r", encoding="utf-8") as fp:
            # get ordered structure
            structure = OrderedDict(
                json.loads(fp.read(), object_pairs_hook=sorted))
        return structure
    return None


def read_tasks():
    """Read tasks.json"""
    if os.path.isfile("tasks.json"):
        with open("tasks.json", "r", encoding="utf-8") as fp:
            tasks = json.loads(fp.read())
        return tasks
    return []


def write_task(structure):
    """Write task based on structure"""
    new_task = {}
    for key in structure:
        value = input("Digite um novo valor para {}: ".format(key))
        new_task.update({key: value})

    all_tasks = read_tasks() + [new_task]
    with open("tasks.json", "w", encoding="utf-8") as fp:
        fp.write(json.dumps(all_tasks))

    return True


def show_tasks(tasks):
    """Print our tasks"""
    for task in tasks:
        for key, value in task.items():
            print("{}: {}".format(key, value))
        print("-~"*20)


if __name__ == "__main__":
    if not os.path.isfile("structure.json"):
        create_structure()

    structure = read_structure()
    while True:
        menu = ("O que deseja fazer?\n"
                "1. Acrescentar compromissos\n"
                "2. Ler compromissos\n"
                "3. Sair\n")
        option = input(menu)
        if option not in ("1", "2", "3"):
            print("Opção inválida! Digite 1, 2 ou 3")
            continue
        elif option == "1":
            write_task(structure)
        elif option == "2":
            tasks = read_tasks()
            if tasks:
                show_tasks(tasks)
            else:
                print("Nenhum compromisso cadastrado!")
        elif option == "3":
            break

print("Até a próxima :P")
