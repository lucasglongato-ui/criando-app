import sqlite3

#Função para conectar ao banco de dados e criar a tabela de usuários, se ela não existir

def conectar():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

conectar()

#Função de registrar usuário

def registrar_usuario(nome,email,senha):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
            (nome, email, senha)
        )
        conn.commit()
        return True
    except:
        return False
    
    finally:
        conn.close()

#Função de verificar login

def verificar_login(email, senha):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE email=? AND senha=?",
        (email, senha)
    )

    usuario = cursor.fetchone()
    conn.close()

    if usuario:
        return True
    else:
        return False
    
    