import mysql.connector
import pandas as pd



def abrir_banco():
    try:
        global conexao
        conexao = mysql.connector.Connect(host='localhost', database='alb_copa', user='root', password='')
        if conexao.is_connected():
            print('Conexão ok!')
            global comandos
            comandos = conexao.cursor()
            comandos.execute('select database()')
            nome_banco = comandos.fetchone()
            print("*"*50)
            print(f'Banco de dados acessado = {nome_banco}')
            print("*" * 50)
            return 1
        else:
            print("*" * 50)
            print('Erro na conexão')
            print("*" * 50)

    except Exception as erro:
        print("*" * 50)
        print(f'Ocorreu o seguinte erro: {erro}')
        print("*" * 50)
        return 0


def cadastrar(resp):
    try:
        if resp == 1:
            while True:
                pais = input('Digite a sigla do pais: ')
                num = int(input('Digite o numero da figurinha do jogador: '))
                nome = input('Digite o nome e sobrenome do jogador: ')
                comandos.execute(f"select * from figurinhas where num_fig = {num} and nome_abreviado = '{pais}';")
                tabela_teste = comandos.fetchall()
                if comandos.rowcount > 0:
                    print("Esse registro ja existe na tabela!!")
                    for r in tabela_teste:
                        print(f"a sigla da seleção e: {r[0]}, o nome da figurinha e: {r[1]}, o numero e {r[2]}")
                elif comandos.rowcount <= 0:
                    comandos.execute(f'insert into figurinhas values ("{pais}",{num},"{nome}");')
                    conexao.commit()
                    print('Cadastro realizado com sucesso!!')
                desejo = input('Deseja criar mais registros? (S/N)').split()
                while desejo[0] != 's' and desejo[0] != 'n':
                    desejo = input('Digite um valor valido: ').split()
                if desejo[0] == 's':
                    continue
                elif desejo[0] == 'n':
                    break
        elif resp == 0:
            while True:
                nome_especial = input('Digite o nome da figurinha especial: ')
                raridade = input('Digite a raridade da figurinha: ')
                comandos.execute(f'insert into especiais values("{nome_especial}","{raridade}");')
                conexao.commit()
                print('Cadastro realizado com sucesso!!')
                desejo2 = input('Deseja criar mais registros? ').split()
                while desejo2[0] != 's' and desejo2[0] != 'n':
                    desejo2 = input('Digite um valor valido: ').split()
                if desejo2[0] == 's':
                    continue
                elif desejo2[0] == 'n':
                    break

        comandos.close()
        conexao.close()
    except Exception as erro:
        print("*" * 50)
        print(f'Ocorreu o seguinte erro: {erro}')
        print("*" * 50)

def consutarEspecifico(resp):
    try:
        if resp == 1:
            while True:
                nome_fig = input('Digite o nome da figurinha: ')
                num_fig = int(input("Digite o numero da figurinha: "))
                comandos.execute(f'select * from figurinhas where nome_fig = "{nome_fig}" and num_fig = {num_fig};')
                table = comandos.fetchall()
                if comandos.rowcount > 0:
                    for r in table:
                        print(f'A sigla e: {r[0]}, O numero e: {r[1]} e O nome e: {r[2]}')
                elif comandos.rowcount <=0:
                    print("o jogador nao existe na tabela")
                    rep = int(input("Deseja adicionar o jogador? (1-SIM!!!!/ 2-NAO!!!!!) "))
                    while rep != 1 and rep != 2:
                        rep = int(input('Digite um valor valido! '))
                    if rep == 1:
                        cadastrar(rep)
                    elif rep == 2:
                        break
                desejo1 = input('Deseja continuar: (s/n) ').split()
                while desejo1[0] != 's' and desejo1[0] != 'n':
                    desejo1 = input('Digite um valor valido: ').split()
                if desejo1[0] == 's':
                    continue
                elif desejo1[0] == 'n':
                    break
        conexao.close()
        comandos.close()
    except Exception as erro:
        print("*" * 50)
        print(f'Ocorreu o seguinte erro: {erro}')
        print("*" * 50)

def consultar(resp):
    try:
        if resp == 1:
            while True:
                sigla = input('Digite a sigla da seleção: ')
                comandos.execute(f'select * from figurinhas where nome_abreviado = "{sigla}";')
                tabela = comandos.fetchall()
                if comandos.rowcount > 0:
                    for r in tabela:
                        print(f'A sigla da seleção e: {r[0]}, o numero da figurinha e: {r[1]} e o nome e: {r[2]}')

                    desejo = input('Deseja continuar a consulta? ').split()
                    while desejo[0] != 's' and desejo[0] != 'n':
                        desejo = input('Digite um valor valido: ').split()
                    if desejo[0] == 's':
                        continue
                    elif desejo[0] == 'n':
                        break
                    return 1
        if resp == 0:
            while True:
                raridade = input('Digite o nome da figurinha: ')
                comandos.execute(f'select * from especiais where nome_especial = "{raridade}";')
                tabela1 = comandos.fetchall()
                if comandos.rowcount > 0:
                    for r in tabela1:
                        print(f'O nome e: {r[0]}, a raridade e: {r[1]}')
                    desejo2 = input('Deseja continuar a consulta? ').split()
                    while desejo2[0] != 's' and desejo2[0] != 'n':
                        desejo2 = input('Digite um valor valido: ').split()
                    if desejo2[0] == 's':
                        continue
                    elif desejo2[0] == 'n':
                        break
                    return 1
        comandos.close()
        conexao.close()
    except Exception as erro:
        print("*" * 50)
        print(f'Ocorreu o seguinte erro: {erro}')
        print("*" * 50)
        return 0


def alterar(resp):
    try:
        if resp == 1:
            while True:
                desejo = int(input('O que vc deseja alterar: (1) - SIGLA SELEÇÃO// (2) - NUMERO DA FIG// (3) - NOME// (4) - ENCERRAR '))
                if desejo == 1:
                    nome1 = input('Digite o nome da figurinha: ')
                    comandos.execute(f'select * from figurinhas where nome_fig = "{nome1}";')
                    tabela = comandos.fetchall()
                    if comandos.rowcount > 0:
                        for r in tabela:
                            print(f'Sigla: {r[0]}, O numero: {r[1]}, O nome: {r[2]}')
                    nn = input('Digite uma nova sigla: ')
                    comandos.execute(f'update figurinhas set nome_abreviado = "{nn}" where nome_fig = "{nome1}";')
                    conexao.commit()
                    print('Alterado com sucesso!!!')

                if desejo == 2:
                    nome2 = input('Digite o nome da figurinha: ')
                    comandos.execute(f'select * from figurinhas where nome_fig = "{nome2}";')
                    tabela1 = comandos.fetchall()
                    if comandos.rowcount > 0:
                        for r in tabela1:
                            print(f'Sigla: {r[0]}, O numero: {r[1]}, O nome: {r[2]}')
                    nnum = int(input('Digite um novo numero: '))
                    comandos.execute(f'update figurinhas set num_fig = {nnum} where nome_fig = "{nome2}";')
                    conexao.commit()
                    print('Alterado com sucesso!!!')

                if desejo == 3:
                    nome = input('Digite o nome da figurinha: ')
                    comandos.execute(f'select * from figurinhas where nome_fig = "{nome}";')
                    tabela2 = comandos.fetchall()
                    if comandos.rowcount > 0:
                        for r in tabela2:
                            print(f'A sigla da seleção: {r[0]}, O numero da fig: {r[1]}, O nome: {r[2]}')
                    nn1 = input('Digite um novo nome: ')
                    comandos.execute(f'update figurinhas set nome_fig = "{nn1}" where nome_fig = "{nome}";')
                    conexao.commit()
                    print('Alterado com sucesso!!!')

                if desejo == 4:
                    break
        if resp == 0:
            while True:
                desejo2 = int(input('O que deseja alterar: (1) - NOME// (2) - RARIDADE// (3) - ENCERRAR '))
                if desejo2 == 1:
                    nome3 = input('Digite o nome da figurinha: ')
                    comandos.execute(f'select * from especiais where nome_especial = "{nome3}";')
                    tabela3 = comandos.fetchall()
                    if comandos.rowcount > 0:
                        for r in tabela3:
                            print(f'O nome: {r[0]} e a raridade: {r[1]}')
                    nn2 = input('Digite o novo nome: ')
                    comandos.execute(f'update especiais set nome_especial = "{nn2}" where nome_especial = "{nome3}";')
                    conexao.commit()
                    print('Alterado com sucesso!!!')
                if desejo2 == 2:
                    nome4 = input('Digite o nome da figurinha: ')
                    comandos.execute(f'select * from especiais where nome_especial = "{nome4}";')
                    tabela4 = comandos.fetchall()
                    if comandos.rowcount > 0:
                        for r in tabela4:
                            print(f'O nome: {r[0]} e raridade: {r[1]}')
                    nr = input('Digite a nova raridade: ')
                    comandos.execute(f'update especiais set raridade = "{nr}" where nome_especial = "{nome4}";')
                    conexao.commit()
                    print('Alteração realizada com sucesso!!')


                if desejo2 == 3:
                    break
        comandos.close()
        conexao.close()
    except Exception as erro:
        print("*" * 50)
        print(f'Ocorreu o seguinte erro: {erro}')
        print("*" * 50)

def deletar(resp):
    try:
        if resp == 1:
            while True:
                nome = input('Digite o nome da figurinha: ')
                comandos.execute(f'select * from figurinhas where nome_fig = "{nome}";')
                tabela = comandos.fetchall()
                if comandos.rowcount > 0:
                    for r in tabela:
                        print(f'A sigla: {r[0]}, o numero: {r[1]} e nome: {r[2]}')

                    comandos.execute(f'delete from figurinhas where nome_fig = "{nome}"')
                    conexao.commit()
                    print('Excluido com sucesso!!')
                    desejo = input('Deseja continuar a exclusão?').split()
                    while desejo[0] != 's' and desejo[0] != 'n':
                        desejo = input('Digite um valor valido: ').split()
                    if desejo[0] == 's':
                        continue
                    elif desejo[0] == 'n':
                        break
        if resp == 0:
            while True:
                nome_especial = input('Digite o nome da figurinha: ')
                comandos.execute(f'select * from especiais where nome_especial = "{nome_especial}"')
                tabela2 = comandos.fetchall()
                if comandos.rowcount > 0:
                    for r in tabela2:
                        print(f'O nome: {r[0]} e a raridade: {r[1]}')
                    comandos.execute(f'delete from especiais where nome_especial = "{nome_especial}"')
                    conexao.commit()
                    print('Deletado com sucesso!!')
                desejo2 = input('Deseja continuar a exclusão?').split()
                while desejo2[0] != 's' and desejo2[0] != 'n':
                    desejo2 = input('Digite um valor valido: ').split()
                if desejo2[0] == 's':
                    continue
                elif desejo2[0] == 'n':
                    break
        comandos.close()
        conexao.close()
    except Exception as erro:
        print("*" * 50)
        print(f'Ocorreu o seguinte erro: {erro}')
        print("*" * 50)
def finalizar():
    comandos.close()
    conexao.close()

def TotalRegistros(resp):
    try:
        if resp == 1:
            comandos.execute(f'select count(*) from figurinhas;')
            table = comandos.fetchall()
            if comandos.rowcount > 0:
                for r in table:
                    print(f'Total de registro: {r[0]}')

        if resp == 0:
            comandos.execute(f'select count(*) from especiais')
            table2 = comandos.fetchall()
            if comandos.rowcount > 0:
                for r in table2:
                    print(f'Total de registro: {r[0]}')
    except Exception as erro:
        print("*" * 50)
        print(f"Ocorreu o seguinte erro: {erro}")
        print("*" * 50)

def consultarTudo(resp):
    try:
        if resp == 1:
            comandos.execute(f'select * from figurinhas order by nome_abreviado ASC;')
            table3 = comandos.fetchall()
            if comandos.rowcount > 0:
                for r in table3:
                    print(f'Sigla: {r[0]}, Numero: {r[1]}, Nome: {r[2]}')

        if resp == 0:
            comandos.execute(f'select * from especiais order by nome_especial ASC;')
            table3 = comandos.fetchall()
            if comandos.rowcount > 0:
                for r in table3:
                    print(f'Nome: {r[0]}, Raridade: {r[1]}')
    except Exception as erro:
        print("*" * 50)
        print(f"Ocorreu o seguinte erro: {erro}")
        print("*" * 50)

def gerar_excel(resp):
    try:
        dicionario = {}
        listaSigla = []
        listaNum = []
        listaNome= []
        listaRaridade =[]
        if resp == 1:
            comandos.execute(f'select * from figurinhas order by nome_abreviado ASC;')
            tabela4 = comandos.fetchall()
            print(type(tabela4))
            if comandos.rowcount > 0:
                for r in tabela4:
                    listaSigla.append(r[0])
                    listaNum.append(r[1])
                    listaNome.append(r[2])
                dicionario['Sigla'] = listaSigla
                dicionario['Numero'] = listaNum
                dicionario['Nome'] = listaNome
                df = pd.DataFrame(dicionario)
                print(df)
                df.to_excel(r"E:\Desktop\figurinhas.xlsx", sheet_name="Planilha1", header=True, index=False)
        if resp == 0:
            comandos.execute(f'select * from especiais order by nome_especial asc;')
            tabela4 = comandos.fetchall()
            if comandos.rowcount > 0:
                listaNome = []
                for r in tabela4:
                    listaNome.append(r[0])
                    listaRaridade.append(r[1])
                dicionario = {}
                dicionario['Nome'] = listaNome
                dicionario['Raridade'] = listaRaridade
                df = pd.DataFrame(dicionario)
                df.to_excel(r"E:\Desktop\figurinhasEspeciais.xlsx", sheet_name="Planilha1", header=True, index=False)
    except Exception as erro:
        print("*" * 50)
        print(f"Ocorreu o seguinte erro: {erro}")
        print("*" * 50)

#FAZER UM READ APENAS PARA O NOME OU NUMERO DO JOGADOR
#FAZER UMA FUNÇÃO PARA ENVIAR A PLANILHA POR EMAIL

##################################################  MODULO PRINCIPAL  #################################################
if abrir_banco() == 1:
    print('''
    --------------------
    BEM-VINDO AO CONTROLE DO ALBUM DA COPA
    --------------------
    C - CREATE
    R - READ
    U - UPDATE
    D - DELETE
    S - SAIR
    T - TOTAL DE REGISTROS
    V - VER TODOS OS REGISTROS
    E - CONSUTAR RESGISTRO PELO NOME
    G - GERAR EXCEL
    --------------------
    QUAL FUNÇÃO DESEJA REALIZAR?  
        ''')
    resp = input('Digite a inicial da função que deseja realizar: ').lower()
    while resp != 'c' and resp != 'r' and resp != 'u' and resp != 'd' and resp != 's' and resp != 't' and resp != 'v' and resp != 'e' and resp != 'g':
        resp = input('Digite um valor valido: ')
    if resp == 'c':

        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('Digite o numero equivalente a tabela que deseja fazer o cadastro: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('Digite um valor valido: '))
        cadastrar(tabela)

    if resp == 'r':
        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('Digite o numero equivalente a tabela que deseja fazer a consulta: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('Digite um valor valido: '))
        consultar(tabela)

    if resp == 'u':
        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('Digite o numero equivalente a tabela que deseja fazer a alteração: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('Digite um valor valido: '))
        alterar(tabela)

    if resp == 'd':
        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('Digite o numero equivalente a tabela que deseja fazer a exclusão: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('Digite um valor valido: '))
        deletar(tabela)

    if resp == 's':
        finalizar()

    if resp == 't':
        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('Digite o numero equivalente a tabela que deseja fazer a soma de registros: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('Digite um valor valido: '))
        TotalRegistros(tabela)

    if resp == 'v':
        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('Digite o numero equivalente a tabela que deseja mostrar todos os registros: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('Digite um valor valido: '))
        consultarTudo(tabela)

    if resp == 'e':
        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('Digite o numero equivalente a tabela que deseja fazer a ação: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('Digite um valor valido: '))
        consutarEspecifico(tabela)

    if resp == 'g':
        print('''
                        1 - TABELA FIGURINHAS
                        0- TABELA ESPECIAIS''')
        tabela = int(input("Digite o numero equivalente a tabela que deseja fazer a ação: "))
        while tabela != 1 and tabela != 0:
            tabela = int(input('Digite um valor valido: '))
        gerar_excel(tabela)
else:
    print("Ocorreu algum erro ao se conectar com o banco!!!")