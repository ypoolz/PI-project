import tkinter as tk
import sqlite3
import pandas as pd


def menu_clientes():
    # #Criando DB:
    conexao = sqlite3.connect('DBdoAPP.db')

    # #Criação do cursor:
    c = conexao.cursor()

    # #Criação da tabela no DB:

    c.execute(''' CREATE TABLE IF NOT EXISTS clientes(
           nome char,
           sobrenome char,
           email char,
           telefone char
            )
            ''')

    # #Commit as mudanças:
    conexao.commit()

    # #Fechar DB
    conexao.close()

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
    
    # Funções na janela de cadastro:

    def cadastrar_clientes():
        try:
            conexao = sqlite3.connect('DBdoAPP.db')
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
        try:
            conexao = sqlite3.connect('DBdoAPP.db')
            c = conexao.cursor()

            # Inserir dados na tabela:
            c.execute(" SELECT *, oid FROM clientes")
            clientes_cadastrados = c.fetchall()

            # Criar estrutura de dados para ser vizualizado no terminal:
            clientes_cadastrados = pd.DataFrame(clientes_cadastrados,
                                                columns=['Nome', 'Sobrenome', 'E-mail', 'Telefone', 'Id'])

            print(clientes_cadastrados)

            # Criar arquivo com dados em csv
            clientes_cadastrados.to_csv('clientes_cadastro.csv')

            conexao.commit()

            conexao.close()
            
            print('Consulta Realizada')
        except:
            print('Erro ao consultar informações')

    def deletar_clientes():
        try:
            conexao = sqlite3.connect('DBdoAPP.db')

            # Criação do cursor:
            c = conexao.cursor()

            # Criação da tabela no DB:
            c.execute('DELETE FROM clientes')

            # Commit as mudanças:
            conexao.commit()

            # Fechar DB
            conexao.close()
            print('Dados deletados com sucesso')
        except:
            print('Ocorreu algum erro. Tente Novamente!')


    # Botões

    # Cadastrar:
    botao_cadastrar = tk.Button(janela, text='Cadastrar Clientes', command=cadastrar_clientes)
    botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    # Exportar
    entry_expotar = tk.Button(janela, text='Consultar informações', command=exportar_clientes)
    entry_expotar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    # Deletar
    entry_deletar = tk.Button(janela, text='Deletar informações', command=deletar_clientes)
    entry_deletar.grid(row=6, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    janela.mainloop()


def menu_restaurantes():
    # #Criando DB:
    conexao = sqlite3.connect('DBdoAPP.db')

    # #Criação do cursor:
    c = conexao.cursor()

    # #Criação da tabela no DB:

    c.execute(''' CREATE TABLE IF NOT EXISTS restaurantes(
           Nome char,
           CNPJ char,
           Email char,
           Telefone char
            )
            ''')

    # #Commit as mudanças:
    conexao.commit()

    # #Fechar DB
    conexao.close()

    # Criação da janela:

    janela = tk.Tk()
    janela.title('Cadastro de Restaurante')

    # Nome das entradas:

    label_Nome = tk.Label(janela, text='Nome do restaurante')
    label_Nome.grid(row=0, column=0, padx=10, pady=10)

    label_CNPJ = tk.Label(janela, text='CNPJ')
    label_CNPJ.grid(row=1, column=0, padx=10, pady=10)

    label_Email = tk.Label(janela, text='E-mail')
    label_Email.grid(row=2, column=0, padx=10, pady=10)

    label_Telefone = tk.Label(janela, text='Telefone')
    label_Telefone.grid(row=3, column=0, padx=10, pady=10)

    # Caixas de entradas:

    entry_nome = tk.Entry(janela, width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)

    entry_cnpj = tk.Entry(janela, width=30)
    entry_cnpj.grid(row=1, column=1, padx=10, pady=10)

    entry_email = tk.Entry(janela, width=30)
    entry_email.grid(row=2, column=1, padx=10, pady=10)

    entry_telefone = tk.Entry(janela, width=30)
    entry_telefone.grid(row=3, column=1, padx=10, pady=10)
    
    # Funções na janela de cadastro:

    def cadastrar_restaurente():
        try:
            # Conexão com DB
            conexao = sqlite3.connect('DBdoAPP.db')
            c = conexao.cursor()

            # Inserir dados na tabela DB:
            c.execute(" INSERT INTO restaurantes VALUES (:Nome, :CNPJ, :Email, :Telefone)",
                      {
                          'Nome': entry_nome.get(),
                          'CNPJ': entry_cnpj.get(),
                          'Email': entry_email.get(),
                          'Telefone': entry_telefone.get()
                      }
                      )

            conexao.commit()

            conexao.close()

            # Apagar os valores das caixas de entrada:
            entry_nome.delete(0, 'end')
            entry_cnpj.delete(0, 'end')
            entry_email.delete(0, 'end')
            entry_telefone.delete(0, 'end')
            print('Cadastrado com sucesso!')
        except:
            print('Ocorreu algum erro. Tente Novamente!')

    def exportar_restaurante():
        try:
            conexao = sqlite3.connect('DBdoAPP.db')
            c = conexao.cursor()

            # Inserir dados na tabela:
            c.execute(" SELECT *, oid FROM restaurantes")
            restaurantes_cadastrados = c.fetchall()

            # Criar estrutura de dados para ser vizualizado no terminal:
            restaurantes_cadastrados = pd.DataFrame(restaurantes_cadastrados,
                                                columns=['Nome', 'CNPJ', 'E-mail', 'Telefone', 'Id'])

            print(restaurantes_cadastrados)

            # Criar arquivos com dados em csv
            restaurantes_cadastrados.to_csv('restaurantes_cadastrados.csv')

            conexao.commit()

            conexao.close()
            print('Consulta Realizada')
        except:
            print('Erro ao consultar informações')
        
    def deletar_restaurante():
        try:
            conexao = sqlite3.connect('DBdoAPP.db')

            # Criação do cursor:
            c = conexao.cursor()

            # Deletar informações no DB:
            c.execute('DELETE FROM clientes')

            # Commit as mudanças:
            conexao.commit()

            # Fechar DB
            conexao.close()
            print('Dados deletados com sucesso')
        except:
            print('Ocorreu algum erro. Tente Novamente!')

    # Botões

    # Cadastrar:
    botao_cadastrar = tk.Button(janela, text='Cadastrar Restaurante', command=cadastrar_restaurente)
    botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    # Exportar
    entry_expotar = tk.Button(janela, text='Consultar informações', command=exportar_restaurante)
    entry_expotar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    # Deletar
    entry_deletar = tk.Button(janela, text='Deletar informações', command=deletar_restaurante)
    entry_deletar.grid(row=6, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    janela.mainloop()


def menu_entregador():
    # #Criando DB:
    conexao = sqlite3.connect('DBdoAPP.db')

    # #Criação do cursor:
    c = conexao.cursor()

    # #Criação da tabela no DB:

    c.execute(''' CREATE TABLE IF NOT EXISTS entregadores(
           NOME char,
           CPF char,
           EMAIL char,
           TELEFONE char
            )
            ''')

    # #Commit as mudanças:
    conexao.commit()

    # #Fechar DB
    conexao.close()

    # Criação da janela:

    janela = tk.Tk()
    janela.title('Cadastro de Entregadores')

    # Nome das entradas:

    label_nome = tk.Label(janela, text='Nome Completo')
    label_nome.grid(row=0, column=0, padx=10, pady=10)

    label_sobrenome = tk.Label(janela, text='CPF')
    label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

    label_email = tk.Label(janela, text='E-mail')
    label_email.grid(row=2, column=0, padx=10, pady=10)

    label_telefone = tk.Label(janela, text='Telefone')
    label_telefone.grid(row=3, column=0, padx=10, pady=10)

    # Caixas de entradas:

    entry_nome = tk.Entry(janela, width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)

    entry_cpf = tk.Entry(janela, width=30)
    entry_cpf.grid(row=1, column=1, padx=10, pady=10)

    entry_email = tk.Entry(janela, width=30)
    entry_email.grid(row=2, column=1, padx=10, pady=10)

    entry_telefone = tk.Entry(janela, width=30)
    entry_telefone.grid(row=3, column=1, padx=10, pady=10)
    
    # Funções na janela de cadastro:

    def cadastrar_entregadores():
        try:
            conexao = sqlite3.connect('DBdoAPP.db')
            c = conexao.cursor()

            # Inserir dados na tabela DB:
            c.execute(" INSERT INTO entregadores VALUES (:NOME, :CPF, :EMAIL, :TELEFONE)",
                      {
                          'NOME': entry_nome.get(),
                          'CPF': entry_cpf.get(),
                          'EMAIL': entry_email.get(),
                          'TELEFONE': entry_telefone.get()
                      }
                      )

            conexao.commit()

            conexao.close()

            # Apagar os valores das caixas de entrada:
            entry_nome.delete(0, 'end')
            entry_cpf.delete(0, 'end')
            entry_email.delete(0, 'end')
            entry_telefone.delete(0, 'end')
            print('Cadastrado com sucesso!')
        except:
            print('Ocorreu algum erro. Tente Novamente!')

    def exportar_entregadores():
        try:
            conexao = sqlite3.connect('DBdoAPP.db')
            c = conexao.cursor()

            # Selecionar dados na tabela:
            c.execute(" SELECT *, oid FROM entregadores")
            cadastro_entregadores = c.fetchall()

            # Criar estrutura de dados para ser vizualizado no terminal:
            cadastro_entregadores = pd.DataFrame(cadastro_entregadores,
                                                columns=['Nome' , 'CPF', 'E-mail', 'Telefone', 'Id'])

            print(cadastro_entregadores)

            # Criação de arquivo csv com dados 
            cadastro_entregadores.to_csv('entregadores_cadastrados.csv')

            conexao.commit()

            conexao.close()
            
            print('Consulta Realizada')
        except:
            print('Erro ao consultar informações')    
            
    def deletar_entregadores():
        try:
            conexao = sqlite3.connect('DBdoAPP.db')

            # Criação do cursor:
            c = conexao.cursor()

            # Deletando informações no DB:
            c.execute('DELETE FROM entregadores')

            # Commit as mudanças:
            conexao.commit()

            # Fechar DB
            conexao.close()
            print('Dados deletados com sucesso!')
        except:
            print('Ocorreu algum erro. Tente Novamente!')

    # Botões

    # Cadastrar:
    botao_cadastrar = tk.Button(janela, text='Cadastrar Entregador', command=cadastrar_entregadores)
    botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    # Exportar
    entry_expotar = tk.Button(janela, text='Consultar informações', command=exportar_entregadores)
    entry_expotar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    # Deletar
    entry_deletar = tk.Button(janela, text='Deletar informações', command=deletar_entregadores)
    entry_deletar.grid(row=6, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    janela.mainloop()


# ===============MENU============ #

# Criação de janela

janela = tk.Tk()
janela.title('Como deseja se cadastrar: ')

# Cadastro de Clientes
botao_menuclientes = tk.Button(janela, text='Cliente', command=menu_clientes)
botao_menuclientes.grid(row=0, column=0, padx=10, pady=10, columnspan=1, ipadx=100)

# Cadastro de Restaurantes
botao_menuresturante = tk.Button(janela, text='Restaurante', command=menu_restaurantes)
botao_menuresturante.grid(row=1, column=0, padx=10, pady=10, columnspan=1, ipadx=100)

# Cadastro de Entregador
botao_menuentregador = tk.Button(janela, text='Entregador', command=menu_entregador)
botao_menuentregador.grid(row=2, column=0, padx=10, pady=10, columnspan=1, ipadx=100)

janela.mainloop()