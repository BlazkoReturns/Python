def verificar_tipo_numero(numero):
    if numero > 0:
       return "maior que"
    elif numero < 0:
        return "menor que"
    else:
        return "igual a"

numero = int(input("Informe um número inteiro."))
print(f"O número informado é {verificar_tipo_numero(numero)} zero.") 