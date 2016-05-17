import json
import os
import sys


def create_tags():
    """This function create tags to your calendar"""
    print("Please input the tags do you want [Press c - to cancel operation]: ")
    list_tags = []
    for tag in range(sys.maxsize):
        tags = input("{} - Tag: ".format(tag+1))
        if tags == 'c':
            break
        list_tags.append(tags)
    structure = {tags : None for tags in list_tags}
    return structure

def create_json(structure):
    """This function create a json file with the tags"""
    with open("structure.json", "w", encoding="utf-8") as fp:
        fp.write(json.dumps(structure))
    return True

def read_tasks():
    """
    This function check if the file tasks.json exist.
    If exist, then return the load in a list format
    """
    if os.path.isfile("tasks.json"):
        with open("tasks.json", "r", encoding="utf-8") as fp:
            tasks = json.loads(fp.read())
        return tasks
    return []

def create_task(structure):
    """
    This function create tasks to your calendar.
    Rewrite the tasks,json file with a new tasks
    """
    new_task = {key :input("Input a new value for the tag {}: ".format(key)) for key in structure}
    all_tasks = read_tasks() + [new_task]
    with open("tasks.json", "w", encoding="utf-8") as fp:
        fp.write(json.dumps(all_tasks))

    return True

def show_tasks(structure):
    """Show to user all the tasks created"""
    for key in structure:
        for i in key:
            print("{}: {}".format(i, key[i]))
        print('>'*25)

    return True

if __name__ == '__main__':
    structure = create_tags()
    while True:
        choice = int(input('''
         What do you want to do?

         1 - Add event
         2 - Read events
         3 - Exit

         '''))

        if choice not in (1, 2, 3):
            print('Invalid option - Try again')
            continue

        elif choice == 1:
            create_task(structure)
        elif choice == 2:
            show_tasks(read_tasks())
        elif choice == 3:
            exit(0)

