import random
import string

letras = string.ascii_letters
numeros = string.digits
acentos = ['!','@','#','%','&','*','?','$','°','º','§','_','|','-','~']



# formato da senha
def config():
    # tamanho = int(input("Digite a quantidade de caracteres que você deseja que sua senha tenha:\n"));
    caracteres = str(input("Sua senha terá caracteres especiais? Digite 'sim' ou 'não': \n"))
    tamanho = int(input("Digite o maximo de caracteres que sua senha deve conter:\n"))
    return caracteres, tamanho

def Senha():
    caracteres, tamanho = config()

    # Definindo se a senha vai ter caracteres especiais
    
    if caracteres == 'sim':
        for Gerador in range(1,tamanho+1):
            senha = [letras,numeros,acentos]
            lista = random.choice(senha)
            valor = random.choice(lista)

            print(f"{valor}", end='')
    else:
        senha = [letras,numeros]
        lista = random.choice(senha)

Senha()

    
