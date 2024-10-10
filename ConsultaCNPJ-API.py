import requests
import re

def ConsultarCNPJ(cnpj):
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"

    r = requests.get(url)    
    if (r.status_code == 200):
        print(
            f'\n'
            f'Nome Fantasia: {r.json()["nome_fantasia"]} \n'
            f'Razão Social: {r.json()["razao_social"]} \n'
            f'Rua: {r.json()["logradouro"]} \n'
        )
    else:
        if(r.status_code >= 400) and (r.status_code <= 499):
            print(f'{r.status_code} - Error related with client error responses')
        elif(r.status_code >= 500) and (r.status_code <= 599):
            print(f'{r.status_code} - Error related with server error responses')
        else:
            print(f'Error: {r.status_code}')
            
########################################################################################

condition = False
print("############## CONSULTADOR DE CNPJ ##############")
while(condition == False):
    input_cnpj = input("Digite o CNPJ:")
    if(len(input_cnpj) == 14):
      condition = True
      ConsultarCNPJ(input_cnpj)
    elif(len(input_cnpj) > 14) and (re.search(".",input_cnpj)) or (re.search("/",input_cnpj)) or (re.search("-",input_cnpj)):
      input_new = input_cnpj.replace(".","").replace("/","").replace("-","")
      condition = True
      ConsultarCNPJ(input_new)
    else:
      print(
            f'\n'
            f'Alguma coisa deu errado...\n'
            f'Tente novamente'
        )
      


