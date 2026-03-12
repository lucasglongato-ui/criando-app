from doctest import master

import customtkinter as ctk

#Função de login

def login():
    login = login_entry.get()
    password = password_entry.get()
    if login in contas and contas[login] == password:
        pagina_login.pack_forget()
        pagina_sistema.pack(fill='both', expand=True)
    else:
        print('Login ou senha incorretos!')

contas = { contas.split(':')[0]: contas.split(':')[1] for contas in open('contas.txt').read().splitlines() }

#Função para salvar os dados do registro em um arquivo

def salvar_dados():
    with open('contas.txt', 'w') as f:
        for login, password in contas.items():
            f.write(f'{login}:{password}\n')   
salvar_dados()

#Dando cores e tema para a interface

ctk.set_appearance_mode('dark')

#Dando forma para a inteface

app = ctk.CTk()
app.title('Login Page')
app.geometry('400x500')

pagina_login = ctk.CTkFrame(app)
pagina_login.pack(fill='both', expand=True)

#Criando o frame para o login e senha

frame = ctk.CTkFrame(pagina_login)
frame.pack(pady=20, padx=60, fill='both', expand=True)

#Criando o título do frame

title = ctk.CTkLabel(master=frame, text='Login', font=('Arial', 24))
title.pack(pady=12, padx=10)

#Criando o campo de login

login_entry = ctk.CTkEntry(master=frame, placeholder_text='Login')
login_entry.pack(pady=12, padx=10)

#Criando o campo de senha

password_entry = ctk.CTkEntry(master=frame, placeholder_text='Senha', show='*')
password_entry.pack(pady=12, padx=10)

#Criando o botão de login

login_button = ctk.CTkButton(master=frame, text='Login', command=login)
login_button.pack(pady=12, padx=10)

#Criando botão de registro

register_button = ctk.CTkButton(master=frame, text='Registrar')
register_button.pack(pady=12, padx=10)

#Criando página de registro

pagina_registro = ctk.CTkFrame(app)
ctk.CTkLabel(pagina_registro, text='Página de registro').pack(pady=20, padx=20)
register_button.configure(command=lambda: [pagina_login.pack_forget(), pagina_registro.pack(fill='both', expand=True)])

#Criação dos campos de registro

def register():
    login = register_login_entry.get()
    password = register_password_entry.get()
    password_confirm = register_password_entry_confirm_entry.get()
    if password == password_confirm:
        contas.update({login: password})
        print('Registro bem-sucedido!')
    if password != password_confirm:
        print('As senhas não coincidem!')
    if len(register_password_entry.get()) < 8 or len(register_password_entry_confirm_entry.get()) < 8:
        print('A senha deve ter pelo menos 8 caracteres!')
    if len(register_password_entry.get()) == 0 or len(register_password_entry_confirm_entry.get()) == 0:
        print('Por favor, preencha todos os campos!')
    if len(register_login_entry.get()) == 0:
        print('Por favor, preencha o campo de login!')
    if len(register_login_entry.get()) != 0 and len(register_password_entry.get()) != 0 and len(register_password_entry_confirm_entry.get()) != 0 and password == password_confirm and len(password) >= 8 and login not in contas:
        contas.update({login: password})
        salvar_dados('contas.txt')
        print('Registro bem-sucedido!')


register_login_entry = ctk.CTkEntry(master=pagina_registro, placeholder_text='Login')
register_login_entry.pack(pady=12, padx=10)
register_password_entry = ctk.CTkEntry(master=pagina_registro, placeholder_text='Senha', show='*')
register_password_entry.pack(pady=12, padx=10)
register_password_entry_confirm_entry = ctk.CTkEntry(master=pagina_registro, placeholder_text='Confirmar senha', show='*')
register_password_entry_confirm_entry.pack(pady=12, padx=10)

register_button = ctk.CTkButton(master=pagina_registro, text='Registrar', command=register)
register_button.pack(pady=12, padx=10)




#Criação do botão de voltar para a página de login

back_button = ctk.CTkButton(master=pagina_registro, text='Voltar', command=lambda: [pagina_registro.pack_forget(), pagina_login.pack(fill='both', expand=True)])
back_button.pack(pady=12, padx=10)



#Página do sistema

pagina_sistema = ctk.CTkFrame(app)
ctk.CTkLabel(pagina_sistema, text='Bem-vindo ao sistema!').pack(pady=20, padx=20)
ctk.CTkButton(pagina_sistema, text='Sair', command=lambda: [pagina_sistema.pack_forget(), pagina_login.pack(fill='both', expand=True)]).pack(pady=12, padx=10)


#Iniciando a interface
app.mainloop()