from operator import index
import tkinter as tk
import sqlite3
import pandas as pd

# #Criando DB:
# conexao = sqlite3.connect('clientes_cadastro.db')

# #Criação do cursor:
# c = conexao.cursor()

# #Criação da tabela no DB:
# c.execute(''' CREATE TABLE clientes (
#   nome text,
#   sobrenome text,
#   email text,
#   telefone text
#    )
# ''')

# #Commit as mudanças:
# conexao.commit()

# #Fechar DB
# conexao.close()

def cadastrar_clientes():
    try:
        conexao = sqlite3.connect('clientes_cadastro.db')
        c = conexao.cursor()

        # Inserir dados na tabela DB:
        c.execute(" INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)",
                      {
                          'nome': entry_nome.get(),
                          'sobrenome': entry_sobrenome.get(),
                          'email': entry_email.get(),
                          'telefone': entry_telefone.get()
                      }
                      )

        conexao.commit()

        conexao.close()

        # Apagar os valores das caixas de entrada:
        entry_nome.delete(0, 'end')
        entry_sobrenome.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        print('Cadastrado com sucesso!')
    except:
        print('Ocorreu algum erro. Tente Novamente!')
    

def exportar_clientes():
    conexao = sqlite3.connect('clientes_cadastro.db')
    c = conexao.cursor()
    
    # Inserir dados na tabela:
    c.execute(" SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    
    # Criar arquivo de planilha do excel:
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, 
                                        columns=['Nome', 'Sobrenome', 'E-mail', 'Telefone', 'Id'])
    print(clientes_cadastrados)
    # clientes_cadastrados.to_csv('clientes_cadastro.csv') 
    
    conexao.commit()

    conexao.close()

def deletar_clientes():
    try:
        conexao = sqlite3.connect('clientes_cadastro.db')

        #Criação do cursor:
        c = conexao.cursor()

        #Criação da tabela no DB:
        c.execute('DELETE FROM clientes')

        #Commit as mudanças:
        conexao.commit()

        #Fechar DB
        conexao.close()
        print('Dados de cadastros deletados')
    except:
        print('Ocorreu algum erro. Tente Novamente!')
    
# Criação da janela:

janela = tk.Tk()
janela.title('Cadastro de clientes')

# Nome das entradas:

label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

# Caixas de entradas:

entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width=30)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, width=30)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

# Botões

# Cadastrar:
botao_cadastrar = tk.Button(janela, text='Cadastrar Clientes', command=cadastrar_clientes)
botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

# Exportar
entry_expotar = tk.Button(janela, text='Ver informações', command=exportar_clientes)
entry_expotar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

# Deletar
entry_deletar = tk.Button(janela, text='Deletar informações', command=deletar_clientes)
entry_deletar.grid(row=6, column=0, padx=10, pady=10, columnspan=2, ipadx=80)


janela.mainloop()

