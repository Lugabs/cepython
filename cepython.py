# -*- coding: utf-8 -*-
"""CEPython

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g67EzOoLzRY3hVd2tI0V_6g-GI8xfFKx
"""

#Como fazer função

def tijolo (valor01, valor02):
  print("Aqui é o numero: " + str(valor01) +  str(valor02))
tijolo (12,34)
tijolo (13,"Luana")
tijolo (14,56)

!pip install requests
import requests
#https://viacep.com.br/ws/09335330/json

import requests
def lala():
  print('CEPython')

  cep = input('Digite o CEP para a consulta: ')

  while len (cep) != 8:
    print("Quantidade de digitos invalida! ")
    cep = input ('Digite novamente seu CEP: ')

  caixinha = requests.get ('https://viacep.com.br/ws/{}/json/'.format(cep))
  endereco = caixinha.json()
  #print(endereco)

  if 'erro' not in endereco:
    print('~~> CEP ENCONTRADO <~~')
    print("CEP: " + endereco['cep'])
    print('Cidade: {}'.format(endereco['localidade']))
    print(f"Estado: {endereco['uf']}")
  else:
    print('{}: CEP inválido.'.format(cep))

  print('--------------------------------------------')

  def validacao():
    opcao = input("Deseja realizar outra consulta? \n 1.Sim \n 2.Sair \n ")
    if opcao == "1" or opcao =="2":
      if int(opcao) == 1:
        lala ()
      else:
        print("Até Mais!!!")
    else:
      print("Não entendi")
      validacao ()
  validacao ()

lala ()