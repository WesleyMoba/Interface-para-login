from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import main

class interface:
    def __init__(self):
        
        #Caracteristicas da interface
        janela = Tk()
        janela.title('Mobben - Sistema Login')
        janela.geometry('300x200')
        janela.resizable(width=False, height=False)
        #Widgets
        self.fazer_registro = ttk.Button(text='Register', width=10, command=lambda:self.registrar_front_end())
        self.fazer_registro.place(x=130, y=50)

        self.fazer_login = ttk.Button(text='Login', width=10, command=lambda:self.logar_front_end(self.fazer_registro, self.fazer_login))
        self.fazer_login.place(x=130, y=90)
        janela.mainloop()

    def voltar(self, *arguments):   #*arguments recebe parametros ilimitados
        
        for itens in arguments:     #arguments retorna uma tupla e entao criei essa laco
            itens.destroy()         # para excluir tudo de uma vez
        
        #adicionando os botoes denovo
        self.fazer_registro = ttk.Button(text='Register', width=10, command=lambda:self.registrar_front_end())
        self.fazer_registro.place(x=130, y=50)

        self.fazer_login = ttk.Button(text='Login', width=10, command=lambda:self.logar_front_end(self.fazer_registro, self.fazer_login))
        self.fazer_login.place(x=130, y=90)
        
    def registrar_front_end(self):
        
        #Remover os botões.
        self.fazer_login.destroy()
        self.fazer_registro.destroy()
        #Adicionar novos botões e adicioanr entradas
        self.label_email = ttk.Label(text='Email:')
        self.label_email.place(x=90, y=31)

        self.label_senha = ttk.Label(text='Senha: ')
        self.label_senha.place(x=90, y=71)

        self.entrada_email = ttk.Entry(width=25)
        self.entrada_email.place(x=130, y=30)

        self.entrada_senha = ttk.Entry(width=25)
        self.entrada_senha.place(x=130, y=70)
        
        self.botao_registrar = ttk.Button(text='Registrar', width=10, command=self.registrarPessoa)
        self.botao_registrar.place(x=130, y=130)

        self.botao_voltar = ttk.Button(text='Voltar', width=10, command=lambda:self.voltar(
            self.label_email, self.label_senha, self.entrada_email, self.entrada_senha, self.botao_registrar, self.botao_voltar
            ))
        self.botao_voltar.place(x=200, y=130)

    def registrarPessoa(self): 

        #Capturar as informacoes digitidas
        email_usuario = self.entrada_email.get()       
        senha_usuario = self.entrada_senha.get()
        if '@' and '.com' in email_usuario and not len(senha_usuario) < 5 and not len(senha_usuario) > 13: #Caso o email contenha @ e .com
            main.registrar_dados(email=email_usuario, senha=senha_usuario)                                 #E caso a senha nao for menor que 5 nem maiorq que 13 
            messagebox.showinfo('Registrado', 'Conta Criada com sucesso')
            self.voltar(self.label_email, self.label_senha, self.entrada_email, self.entrada_senha, self.botao_registrar, self.botao_voltar)
        else:   
            messagebox.showwarning('Falha', 'Digite um email valido e uma senha valida')    
            
    def logar_front_end(self, *arguments):
        for itens in arguments:
            itens.destroy() #Apagar isso
        #Organizar os botoes    
        self.email_login = ttk.Entry(width=25)
        self.email_login.place(x=130, y=30)

        self.senha_login = ttk.Entry(width=25)
        self.senha_login.place(x=130, y=70)

        self.label_email2 = Label(text='Email')
        self.label_email2.place(x=90, y=31)

        self.label_senha2 = ttk.Label(text='Senha: ')
        self.label_senha2.place(x=90, y=71)
    
        self.botao_login = ttk.Button(text='Logar', width=10, command=lambda:self.login())
        self.botao_login.place(x=130, y=130)

        self.botao_voltar = ttk.Button(text='Voltar', width=10, command=lambda:self.voltar(
            self.label_email2, self.label_senha2, self.botao_login, self.email_login, self.senha_login, self.botao_voltar
            ))
        self.botao_voltar.place(x=200, y=130)

    def login(self):
        email = self.email_login.get()
        senha = self.senha_login.get()
        print(f'{email}\n{senha}')
        main.login(senha, email)

if __name__ == '__main__':
    app = interface()
