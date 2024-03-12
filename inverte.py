def inverte_string(string):
    caracteres = list(string)
    inicio = 0
    fim = len(caracteres) - 1
    
    while inicio < fim:
       
        caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
     
        inicio += 1
        fim -= 1
    
    string_invertida = ''.join(caracteres) 
    return string_invertida

string_original = input("Digite uma string para inverter: ")
string_invertida = inverte_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
