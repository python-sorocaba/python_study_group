import os
import time
import sqlite3
from terminaltables import AsciiTable

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def add_field():
    message = """
        Favor informar os campos desejados.

        Ao deixar um campo vazio a inclusão será finalizada.
    """
    print(message)

    get_user_fields = True
    fields = []
    while get_user_fields:
        field = input("Informe um novo campo: ")
        if not field:
            if len(fields) > 1:
                print("\nForam digitados {} campos. Deseja informar mais campos?".format(len(fields)))
            else:
                print("\nFoi digitado {} campo. Deseja informar mais campos?".format(len(fields)))

            for i, field in enumerate(fields):
                print("Campo {}: {}".format(i+1, field))

            confirm = None

            while(True):

                if not confirm:
                    confirm = input("\n[M = Mais campos] | [C = Continuar com a execução] | [R = Remover campo]: ")
                elif confirm.upper() == "M":
                    confirm = None
                    break
                elif confirm.upper() == "C":
                    get_user_fields = False
                    break
                elif confirm.upper() == "R":
                    try:
                        field_remove = input("\nInforme o número do campo que deseja remover | [S = Sair]: ")
                        if field_remove.upper() != "S":
                            field_remove = int(field_remove)-1
                            fields.remove(fields[field_remove])
                        else:
                            confirm = None
                    except Exception as e:
                        print('\n\n>>>>>>>>>> Digite apenas números válidos! <<<<<<<<<<')
                else:
                    print('\n\n>>>>>>>>>> Digite uma das informações disponíveis acima <<<<<<<<<<')
                    confirm = None

        else:
            fields.append(field)
    
    for field in fields:
        diary().add_field(field.lower())


class diary():

    def __init__(self):
        return

    def get_list_field(self):
        fields = []
        db = database().get_connection()
        for row in db.execute("SELECT field_name FROM field ORDER BY id_field"):
            for item in row:
                fields.append(item)
        db.close()

        return fields

    def add_field(self, field):
        db = database().get_connection()
        try:
            db.execute("INSERT INTO field (field_name) VALUES (?)", (field,))
            db.commit()
        except sqlite3.IntegrityError:
            pass
        finally:
            db.close()

    def get_id_field(self, field):
        db = database().get_connection()
        id_field = db.execute("SELECT id_field FROM field WHERE field_name = ?", (field,))
        for row in id_field:
            for item in row:
                id_field = item
        db.close()
        return id_field

    def add_event(self, date, dict_field_values):
        db = database().get_connection()
        id_event_reg = self.register_event(date)
        for field_values in dict_field_values:
            id_field = self.get_id_field(field_values)
            db.execute("INSERT INTO event (id_event_reg, id_field, value_field) VALUES (?, ?, ?)", 
                (id_event_reg, id_field, dict_field_values[field_values],))
        db.commit()
        db.close()

    def register_event(self, date):
        db = database().get_connection()
        db.execute("INSERT INTO event_register (date_event) VALUES (?)", (date,))
        db.commit()
        id_event_reg = db.execute("SELECT id_event_reg FROM event_register WHERE date_event = ?", (date,))
        for row in id_event_reg:
            for item in row:
                id_event_reg = item
        db.close()
        return id_event_reg

    def get_list_event_register(self):
        db = database().get_connection()
        event_register = db.execute("""
            SELECT id_event_reg, STRFTIME("%d/%m/%Y %H:%M", date_event) as date_event FROM event_register
        """)
        return event_register

    def get_event(self, id_event_register):
        db = database().get_connection()
        event = db.execute("""
            SELECT
                ev.value_field as Event
            FROM event ev
            LEFT JOIN event_register AS ev_reg ON ev_reg.id_event_reg = ev.id_event_reg
            LEFT JOIN field AS f ON f.id_field = ev.id_field
            WHERE ev.id_event_reg = ?
            ORDER BY f.id_field
        """, (id_event_register,))
        return event


class database():
    
    def __init__(self):
        self.database_file = 'diary.db'

    
    def get_connection(self):
        """Verify existence of database_file"""
        if not os.path.isfile(self.database_file):
            self.conn = None
        else:
            self.conn = sqlite3.connect(self.database_file)
        return self.conn

    
    """Execute when database not exist"""
    def first_execution(self):
        """Create database_file"""
        self.conn = sqlite3.connect(self.database_file)
        
        """Create tables in database"""
        self.conn.execute(
            """CREATE TABLE field (
                id_field INTEGER PRIMARY KEY ASC AUTOINCREMENT NOT NULL,
                field_name VARCHAR(30) UNIQUE NOT NULL)"""
        )

        self.conn.execute(
            """CREATE TABLE event_register (
                id_event_reg INTEGER PRIMARY KEY ASC AUTOINCREMENT NOT NULL,
                date_event DATETIME NOT NULL)"""
            )

        self.conn.execute(
            """CREATE TABLE event (
                id_event         INTEGER        PRIMARY KEY        ASC AUTOINCREMENT    NOT NULL,
                id_event_reg    INTEGER        NOT NULL,
                id_field        INTEGER        NOT NULL,
                value_field        VARCHAR(120)        NULL,
                FOREIGN KEY (id_event_reg)    REFERENCES event_register (id_event_reg),
                FOREIGN KEY (id_field)        REFERENCES field (id_field)
            )"""
        )

        self.conn.close()


if __name__ == "__main__":
    
    db = None

    """Get connection database"""
    while True:
        db = database().get_connection()
        
        """Verify return of get_connection method. If None, create a new structure in database"""
        if not db:
            database().first_execution()
        else:
            db.close()
            break

    if len(diary().get_list_field()) == 0:
        add_field()

    while(True):
        clear_screen()

        message = """
            *********************************************************
            *                                                       *
            *                      Bem-Vindo!                       *
            *                 O que deseja fazer?                   *
            *                                                       *
            *     1 - Analisar compromissos                         *
            *     2 - Adicionar compromissos                        *
            *     3 - Adicionar campos                              *
            *     4 - Sair                                          *
            *                                                       *
            *********************************************************
        """

        print(message)

        op = input("Digite a opção desejada: ")

        if op == "1":
            fields = diary().get_list_field()
            events_register = diary().get_list_event_register()
            
            table_data = []
            header = ["ID", "Data de Registro"]
            
            for field in fields:
                header.append("{}{}".format(field[0:1].upper(), field[1:]))
            table_data.append(header)

            for event_register in events_register:
                content = []
                for item in event_register:
                    content.append(str(item))

                events = diary().get_event(event_register[0])

                for event in events:
                    for item in event:
                        content.append(item)

                table_data.append(content)

            table = AsciiTable(table_data, "Compromissos")
            print("\n\n{}\n\n".format(table.table))
            input("Pressione qualquer tecla para continuar... ")
        elif op == "2":
            print("\nAdicionar compromisso:")
            fields = diary().get_list_field()

            field_value = {}
            for field in fields:
                value = input("{}{} do evento: ".format(field[0:1].upper(), field[1:]))
                field_value[field] = value
            
            date = time.strftime("%Y-%m-%d %H:%M:%S")
            diary().add_event(date, field_value)

            input("Evento adicionado! Pressione qualquer tecla para continuar...")
        elif op == "3":
            add_field()
        elif op == "4":
            exit(0)
