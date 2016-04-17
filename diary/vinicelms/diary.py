import os
import time
import sqlite3

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class diary():

    def __init__(self):
        return

    def get_list_field(self):
        fields = []
        db = database().get_connection()
        for row in db.execute("SELECT field_name FROM field"):
            fields.append(row)
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
        db.execute("SELECT id_field FROM field WHERE field_name = ?", (field,))
        db.close()

class database():
    
    def __init__(self):
        self.database_file = '/home/vinicius/Desktop/diary.db'

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
                value_field        INTEGER        NULL,
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

    fields = diary().get_list_field()

    if len(fields) == 0:
        message = """
            Esta é a primeira vez que a aplicação está sendo executada. Favor informar os campos desejados.

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
            diary().add_field(field)

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
            *     3 - Sair                                          *
            *                                                       *
            *********************************************************
        """

        print(message)

        op = input("Digite a opção desejada: ")

        if op == "1":
            fields = diary().get_list_field()
