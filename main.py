from front import *
from tkinter import *
from tkinter import messagebox
import json

def registrar_dados(email, senha):
    with open('dados.json', 'r') as arqv:    #Abrir arquivos jason e ler
        dados = json.load(arqv)              #Transforma o arquivo json em um dicionario
    for emails in dados: #Iterar sobre as chave
        if emails == email:    #Caso uma chave for igual ao email deixar a variavel true e exibir mensagem de erro
            ja_existe = True    
            messagebox.showwarning('Falha', 'já existe uma conta com esse email') 
            continue
        else:
            ja_existe = False #Caso nao deixar a variavel false
            pass
    if ja_existe == False:
        dados[email] = {       #Adiciona a senha e o email no dicionario
            'email': email,
            'senha': senha
        }
        with open('dados.json', 'w') as arquivo: #Abre o arquivo json para digitar
            json.dump(dados, arquivo, indent=4)  #Envia o mesmo dicionario para ele
        messagebox.showinfo('Conta criada com sucesso')
    else:
        messagebox.showwarning('Falha ao criar conta')
        pass

def login(senhadigitada, emaildigitado):
    email = False
    senha = False 
    with open('dados.json', 'r') as arquivo: #Abrir o arquvivo para leitura
        informacoes = json.load(arquivo) #Deixar em um dicionario
    for chave, valor in informacoes.items():
        print(emaildigitado, chave)
        if chave == emaildigitado: #Caso alguma chave seja igual a o email
            for chav, valor in valor.items(): #Ai explorar os itens
                if chav == 'email':
                    if valor == emaildigitado: #Se o email for igual o email digitado deixar marcar o email como True
                        email = True
                elif chav == 'senha': #Mesma coisa com a senha
                    if valor == senhadigitada:
                        senha = True
        else: 
            pass
    if senha == True and email == True:       #Caso os dois sejam True
        messagebox.showinfo('Sucesso', 'Login efetuado com sucesso') #Logar
        #Aqui pode colocar outro modulo para dar uma funçãoa  esse sistema
    else:
        messagebox.showwarning('Falha', 'Revise sua senha e seu email') #Caso os dois nao sejam True exibir uma falha
if __name__ == '__main__':
    print(21.90 + 52.90 +84.90 +141)
    print(27.80 + 17.70 +39.90 +56)
    print(141 +141)