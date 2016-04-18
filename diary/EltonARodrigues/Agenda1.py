# -*- coding: utf-8 -*-

"""
Doctest Agenda

>>> type(field('Nome'))
<class 'dict'>
>>> key_out(field('Nome'))
>>> key_up = {}
>>> key_up[0] = 'Teste'
>>> key_out((key_up))
   for k, v in key_in().items():
"""

import json 
import os

dic_data = {}
def field(nome):
	
	dic_data[nome] = None
	return dic_data

def key_out(keys): #keys
	with open('content.json', 'w') as f:
		json.dump(keys, f)

def key_in():
	try:
		with open('Agenda.json', 'r') as f:
			data = json.load(f)
		return data

	except FileNotFoundError:
		return 1


if __name__ =="__main__":

	

	if key_in() == 1:

		while 1:
			new_fild = input("Digite um novo campo(/ = parar): ")

			if new_fild == '/':
				break

			key_out(field(new_fild))
				
	else:
		while 1:
				
			m = """
				
           		 Escolha:						                        
           		                			                            
          	                                                       
                 0 - Excluir   // N funciona                                    
                 1 - Adicionar compromissos
                 3 - Adicionar Campo/Remover campo // n funciona                        
                 2 - Ler compromissos  
                 4 - Sair                                          
            """
			
			print(m)
			choise = input(": ")


			if choise == 0:
				#Apagar arquivo 
				pass
			elif choise == '1':


				key_up = {}

				for k in key_in().keys():
					
					new_dado = input("Digite um novo valor para {}: ".format(k))
					key_up[k] = new_dado
				
				key_out((key_up))
				os.system('clear')

			elif choise == '2':

				c = 0
				for k, v in key_in().items():
					if v ==  None:
						c = 1
					else:
						print('{0}: {1}'.format(k,v))
				if c != 0:
					print('Nenhum compromisso cadastrado!')
				input('')
				os.system('clear')
			else:
				break
			