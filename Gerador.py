import random
import string

letras = string.ascii_letters
numeros = string.digits
acentos = ['!','@','#','%','&','*','?','$','°','º','§','_','|','-','~']



# formato da senha
def config():
    caracteres = str(input("Voce prefere uma senha forte, normal ou fraca?: \n"))
    tamanho = int(input("Digite o maximo de caracteres que sua senha deve conter:\n"))
    return caracteres, tamanho

def Senha():
    caracteres, tamanho = config()

    # Definindo se a senha vai ter caracteres especiais
    
    if caracteres == 'Forte' or caracteres == 'forte':

        if tamanho <= 15:
            print("Sua senha é:")

            for Gerador in range(1,tamanho+1):
                senha = [letras,numeros,acentos]
                lista = random.choice(senha)
                valor = random.choice(lista)

                print(valor, end='')
        else:
            print("Invalido.O numero maximo de caracteres é 15")
        
    elif caracteres == 'Normal' or caracteres == 'normal':
        
        if tamanho < 15:
            print("Sua senha é:")

            for Gerador in range(1,tamanho+1):
                senha = [letras,numeros]
                lista = random.choice(senha)
                valor = random.choice(lista)

                print(valor, end='')
        
        else:
            print("Invalido.O numero maximo de caracteres é 15")

    elif caracteres == 'Fraca' or caracteres == 'fraca':
        
        if tamanho <= 15:
            print("Sua senha é:")

            for Gerador in range(1,tamanho+1):
                senha = [letras]
                lista = random.choice(senha)
                valor = random.choice(lista)

                print(valor, end='')
        else:
            print("Invalido.O numero maximo de caracteres é 15")


Senha()

    

    
