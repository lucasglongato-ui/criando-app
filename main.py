from database import registrar_usuario, verificar_login

import customtkinter as ctk

import database

#Função de login

def login():
    email = email_entry.get()
    password = password_entry.get()
    if verificar_login(email, password):
        pagina_login.pack_forget()
        pagina_sistema.pack(fill='both', expand=True)
    else:
        print('Login ou senha incorretos!')

#Função de registro

def register():
    login = register_login_entry.get()
    email = register_email_entry.get()
    password = register_password_entry.get()
    password_confirm = register_password_entry_confirm_entry.get()
    if password == password_confirm:
        if registrar_usuario(login, email, password):
            print('Registro bem-sucedido!')
        else:
            print('Erro ao registrar usuário! Verifique se o email já está em uso.')
    else:
        print('As senhas não coincidem!')
    if len(password) < 8:
        print('A senha deve ter pelo menos 8 caracteres!')
    if len(login) == 0 or len(email) == 0 or len(password) == 0 or len(password_confirm) == 0:
        print('Por favor, preencha todos os campos!')


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

#Criando o campo de email
email_entry = ctk.CTkEntry(master=frame, placeholder_text='Email')
email_entry.pack(pady=12, padx=10)

#Criando o campo de senha
password_entry = ctk.CTkEntry(master=frame, placeholder_text='Senha', show='*')
password_entry.pack(pady=12, padx=10)  

#Criando o botão de login
login_button = ctk.CTkButton(master=frame, text='Login', command=login)
login_button.pack(pady=12, padx=10)

#Criando botão de registro
register_button = ctk.CTkButton(master=frame, text='Registrar', command=register)
register_button.pack(pady=12, padx=10)

#Criando página de registro
pagina_registro = ctk.CTkFrame(app)
ctk.CTkLabel(pagina_registro, text='Página de registro').pack(pady=20, padx=20)
register_button.configure(command=lambda: [pagina_login.pack_forget(), pagina_registro.pack(fill='both', expand=True)])

#Criação dos campos de registro
register_login_entry = ctk.CTkEntry(master=pagina_registro, placeholder_text='Login')
register_login_entry.pack(pady=12, padx=10)
register_email_entry = ctk.CTkEntry(master=pagina_registro, placeholder_text='Email')
register_email_entry.pack(pady=12, padx=10)
register_password_entry = ctk.CTkEntry(master=pagina_registro, placeholder_text='Senha', show='*')
register_password_entry.pack(pady=12, padx=10)
register_password_entry_confirm_entry = ctk.CTkEntry(master=pagina_registro, placeholder_text='Confirmar senha', show='*')
register_password_entry_confirm_entry.pack(pady=12, padx=10)

#Criando botão de registro na página de registro
register_button_registro = ctk.CTkButton(master=pagina_registro, text='Registrar', command=register)
register_button_registro.pack(pady=12, padx=10)

#Criando a página do sistema
pagina_sistema = ctk.CTkFrame(app)
pagina_sistema.pack(fill='both', expand=True)
sistema_title = ctk.CTkLabel(master=pagina_sistema, text='Bem-vindo ao sistema!', font=('Arial', 24))
sistema_title.pack(pady=12, padx=10)

#Criando o botão de logout
def logout():
    pagina_sistema.pack_forget()
    pagina_login.pack(fill='both', expand=True)

logout_button = ctk.CTkButton(master=pagina_sistema, text='Logout', command=logout)
logout_button.pack(pady=12, padx=10)


#Iniciando a interface
app.mainloop()