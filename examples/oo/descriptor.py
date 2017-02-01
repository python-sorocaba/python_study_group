
#
# This script show how descriptor dont "freeze" 
# state of an atributte
#


from datetime import datetime
from time import sleep

class MyDescriptor:
    def __get__(self, obj, objtype):
        return datetime.now()

class Account:

    TESTE = MyDescriptor()

print(Account.TESTE)
sleep(1)
print(Account.TESTE)
sleep(1)
print(Account.TESTE)
sleep(1)
