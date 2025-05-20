def somar(numero1, numero2):
    resultado_soma = numero1 + numero2
    return resultado_soma # A função "devolve" o valor de resultado

somar(2, 3) # Chamada da função somar com os parâmetros
resultado_da_soma = somar(2, 3) # Atribuição do resultado à variável
print(resultado_da_soma) # Impressão do valor de "resultado_da_soma"
# A função "somar" recebe dois números como parâmetros e retorna a soma dele.

print(f"Somando 7 e 2 diretamente: {somar(7, 2)}")