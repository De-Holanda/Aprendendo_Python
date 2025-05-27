contador = 0
while contador < 10:
    print(contador)
    contador += 1
    
    
lista_frutas = ['banana', 'uva', 'abacaxi', 'pera', 'laranja']

indice = 0 
print("percorrer a lista de frutas com while e indice; ")

while indice < len(lista_frutas):
    fruta_atual = lista_frutas[indice]
    print(f"- indice {indice}: {fruta_atual}")
    indice += 1 
    