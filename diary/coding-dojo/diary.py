import json

new_dict = {}


def receive_field(data):
    new_dict[data] = None
    return new_dict


def insert_arq(dicio):
    with open("task.txt", 'w') as fp:
        fp.write(json.dumps(dicio))


def import_arq():
    with open("task.txt", 'r') as fp:
        dict_returned = json.loads(fp.read())
    return dict_returned


def receive_multiple_fields(fieldlist):
    dicio = {}
    for field in fieldlist:
        new_dict = receive_field(field)
        dicio.update(new_dict)
    return dicio

if __name__ == "__main__":
    field = receive_field({"nome": None, "idade": None})
    fieldlist = []
    while True:
        field = input("Digite um campo [c=cancelar]:")
        if field == "c":
            break
        fieldlist.append(field)
    receive_multiple_fields(fieldlist)
    insert_arq()
