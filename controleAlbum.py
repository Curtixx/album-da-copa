import mysql.connector

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
            print(f'Banco de dados acessado = {nome_banco}')
            return 1
        else:
            print('Erro na conexão')

    except Exception as erro:
        print(f'ocorreu o seguinte erro: {erro}')
        return 0


def cadastrar(resp):
    try:
        if resp == 1:
            while True:
                pais = input('digite a sigla do pais: ')
                num = int(input('digite o numero da figurinha do jogador: '))
                nome = input('digite o nome e sobrenome do jogador: ')
                comandos.execute(f'insert into figurinhas values ("{pais}",{num},"{nome}");')
                conexao.commit()
                print('Cadastro realizado com sucesso!!')
                desejo = input('deseja criar mais registros? ').split()
                while desejo[0] != 's' and desejo[0] != 'n':
                    desejo = input('digite um valor valido: ').split()
                if desejo[0] == 's':
                    continue
                elif desejo[0] == 'n':
                    break
        elif resp == 0:
            while True:
                nome_especial = input('digite o nome da figurinha especial: ')
                raridade = input('digite a raridade da figurinha: ')
                comandos.execute(f'insert into especiais values("{nome_especial}","{raridade}");')
                conexao.commit()
                print('Cadastro realizado com sucesso!!')
                desejo2 = input('deseja criar mais registros? ').split()
                while desejo2[0] != 's' and desejo2[0] != 'n':
                    desejo2 = input('digite um valor valido: ').split()
                if desejo2[0] == 's':
                    continue
                elif desejo2[0] == 'n':
                    break

        comandos.close()
        conexao.close()
    except Exception as erro:
        print(f'ocorreu o seguinte erro: {erro}')

def consutarEspecifico(resp):
    try:
        if resp == 1:
            while True:
                nome_fig = input('digite o nome do jogador: ')
                comandos.execute(f'select * from figurinhas where nome_fig = "{nome_fig}"')
                table = comandos.fetchall()
                if comandos.rowcount > 0:
                    for r in table:
                        print(f'A sigla e: {r[0]}, O numero e: {r[1]} e O nome e: {r[2]}')
                elif comandos.rowcount <=0:
                    rep = input("Deseja adicionar o jogador? (sim/nao) ").split()
                    while rep[0] != "s" and rep[0] != "n":
                        rep = int(input('Digite um valor valido! '))
                    if rep[0] == "s":
                        cadastrar(rep)
                    elif rep[0] == "n":
                        break
                desejo1 = input('deseja continuar: (s/n) ').split()
                while desejo1[0] != 's' and desejo1[0] != 'n':
                    desejo1 = input('digite um valor valido: ').split()
                if desejo1[0] == 's':
                    continue
                elif desejo1[0] == 'n':
                    break
    except Exception as erro:
        print(f'ocorreu o seguinte erro: {erro}')

def consultar(resp):
    try:
        if resp == 1:
            while True:
                sigla = input('digite a sigla da seleção: ')
                comandos.execute(f'select * from figurinhas where nome_abreviado = "{sigla}";')
                tabela = comandos.fetchall()
                if comandos.rowcount > 0:
                    for r in tabela:
                        print(f'A sigla da seleção e: {r[0]}, o numero da figurinha e: {r[1]} e o nome e: {r[2]}')

                    desejo = input('deseja continuar a consulta? ').split()
                    while desejo[0] != 's' and desejo[0] != 'n':
                        desejo = input('digite um valor valido: ').split()
                    if desejo[0] == 's':
                        continue
                    elif desejo[0] == 'n':
                        break
                    return 1
        if resp == 0:
            while True:
                raridade = input('digite o nome da figurinha: ')
                comandos.execute(f'select * from especiais where nome_especial = "{raridade}";')
                tabela1 = comandos.fetchall()
                if comandos.rowcount > 0:
                    for r in tabela1:
                        print(f'O nome e: {r[0]}, a raridade e: {r[1]}')
                    desejo2 = input('deseja continuar a consulta? ').split()
                    while desejo2[0] != 's' and desejo2[0] != 'n':
                        desejo2 = input('digite um valor valido: ').split()
                    if desejo2[0] == 's':
                        continue
                    elif desejo2[0] == 'n':
                        break
                    return 1
        comandos.close()
        conexao.close()
    except Exception as erro:
        print(f'ocorreu o seguinte erro: {erro}')
        return 0


def alterar(resp):
    try:
        if resp == 1:
            while True:
                desejo = int(input('o que vc deseja alterar: (1) - SIGLA SELEÇÃO// (2) - NUMERO DA FIG// (3) - NOME// (4) - ENCERRAR '))
                if desejo == 1:
                    nome1 = input('digite o nome da figurinha: ')
                    comandos.execute(f'select * from figurinhas where nome_fig = "{nome1}";')
                    tabela = comandos.fetchall()
                    if comandos.rowcount > 0:
                        for r in tabela:
                            print(f'Sigla: {r[0]}, O numero: {r[1]}, O nome: {r[2]}')
                    nn = input('digite uma nova sigla: ')
                    comandos.execute(f'update figurinhas set nome_abreviado = "{nn}" where nome_fig = "{nome1}";')
                    conexao.commit()
                    print('Alterado com sucesso!!!')

                if desejo == 2:
                    nome2 = input('digite o nome da figurinha: ')
                    comandos.execute(f'select * from figurinhas where nome_fig = "{nome2}";')
                    tabela1 = comandos.fetchall()
                    if comandos.rowcount > 0:
                        for r in tabela1:
                            print(f'Sigla: {r[0]}, O numero: {r[1]}, O nome: {r[2]}')
                    nnum = int(input('digite um novo numero: '))
                    comandos.execute(f'update figurinhas set num_fig = {nnum} where nome_fig = "{nome2}";')
                    conexao.commit()
                    print('Alterado com sucesso!!!')

                if desejo == 3:
                    nome = input('digite o nome da figurinha: ')
                    comandos.execute(f'select * from figurinhas where nome_fig = "{nome}";')
                    tabela2 = comandos.fetchall()
                    if comandos.rowcount > 0:
                        for r in tabela2:
                            print(f'A sigla da seleção: {r[0]}, O numero da fig: {r[1]}, O nome: {r[2]}')
                    nn1 = input('digite um novo nome: ')
                    comandos.execute(f'update figurinhas set nome_fig = "{nn1}" where nome_fig = "{nome}";')
                    conexao.commit()
                    print('Alterado com sucesso!!!')

                if desejo == 4:
                    break
        if resp == 0:
            while True:
                desejo2 = int(input('o que deseja alterar: (1) - NOME// (2) - RARIDADE// (3) - ENCERRAR '))
                if desejo2 == 1:
                    nome3 = input('digite o nome da figurinha: ')
                    comandos.execute(f'select * from especiais where nome_especial = "{nome3}";')
                    tabela3 = comandos.fetchall()
                    if comandos.rowcount > 0:
                        for r in tabela3:
                            print(f'O nome: {r[0]} e a raridade: {r[1]}')
                    nn2 = input('digite o novo nome: ')
                    comandos.execute(f'update especiais set nome_especial = "{nn2}" where nome_especial = "{nome3}";')
                    conexao.commit()
                    print('Alterado com sucesso!!!')
                if desejo2 == 2:
                    nome4 = input('digite o nome da figurinha: ')
                    comandos.execute(f'select * from especiais where nome_especial = "{nome4}";')
                    tabela4 = comandos.fetchall()
                    if comandos.rowcount > 0:
                        for r in tabela4:
                            print(f'O nome: {r[0]} e raridade: {r[1]}')
                    nr = input('digite a nova raridade: ')
                    comandos.execute(f'update especiais set raridade = "{nr}" where nome_especial = "{nome4}";')
                    conexao.commit()
                    print('Alteração realizada com sucesso!!')


                if desejo2 == 3:
                    break
        comandos.close()
        conexao.close()
    except Exception as erro:
        print(f'ocorreu o seguinte erro: {erro}')

def deletar(resp):
    try:
        if resp == 1:
            while True:
                nome = input('digite o nome da figurinha: ')
                comandos.execute(f'select * from figurinhas where nome_fig = "{nome}";')
                tabela = comandos.fetchall()
                if comandos.rowcount > 0:
                    for r in tabela:
                        print(f'A sigla: {r[0]}, o numero: {r[1]} e nome: {r[2]}')

                    comandos.execute(f'delete from figurinhas where nome_fig = "{nome}"')
                    conexao.commit()
                    print('Excluido com sucesso!!')
                    desejo = input('deseja continuar a exclusão?').split()
                    while desejo[0] != 's' and desejo[0] != 'n':
                        desejo = input('digite um valor valido: ').split()
                    if desejo[0] == 's':
                        continue
                    elif desejo[0] == 'n':
                        break
        if resp == 0:
            while True:
                nome_especial = input('digite o nome da figurinha: ')
                comandos.execute(f'select * from especiais where nome_especial = "{nome_especial}"')
                tabela2 = comandos.fetchall()
                if comandos.rowcount > 0:
                    for r in tabela2:
                        print(f'o nome: {r[0]} e a raridade: {r[1]}')
                    comandos.execute(f'delete from especiais where nome_especial = "{nome_especial}"')
                    conexao.commit()
                    print('Deletado com sucesso!!')
                desejo2 = input('deseja continuar a exclusão?').split()
                while desejo2[0] != 's' and desejo2[0] != 'n':
                    desejo2 = input('digite um valor valido: ').split()
                if desejo2[0] == 's':
                    continue
                elif desejo2[0] == 'n':
                    break
        comandos.close()
        conexao.close()
    except Exception as erro:
        print(f'ocorreu o seguinte erro: {erro}')
def finalizar():
    comandos.close()
    conexao.close()

def TotalRegistros(resp):
    if resp == 1:
        comandos.execute(f'select count(*) from figurinhas;')
        table = comandos.fetchall()
        if comandos.rowcount > 0:
            for r in table:
                print(f'total de registro: {r[0]}')

    if resp == 0:
        comandos.execute(f'select count(*) from especiais')
        table2 = comandos.fetchall()
        if comandos.rowcount > 0:
            for r in table2:
                print(f'total de registro: {r[0]}')

def consultarTudo(resp):
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

#FAZER UM READ APENAS PARA O NOME OU NUMERO DO JOGADOR
#FAZER UMA FUNÇÃO PARA ENVIAR A PLANILHA POR EMAIL

##################################################  MODULO PRINCIPAL  #################################################
if abrir_banco() == 1:
    print('''
    --------------------
    C - CREATE
    R - READ
    U - UPDATE
    D - DELETE
    S - SAIR
    T - TOTAL DE REGISTROS
    V - VER TODOS OS REGISTROS
    E - CONSUTAR RESGISTRO PELO NOME
    --------------------
    QUAL FUNÇÃO DESEJA REALIZAR?  
        ''')
    resp = input('digite a inicial da função que deseja realizar: ')
    while resp != 'c' and resp != 'r' and resp != 'u' and resp != 'd' and resp != 's' and resp != 't' and resp != 'v' and resp != 'e':
        resp = input('digite um valor valido: ')
    if resp == 'c':

        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('digite o numero equivalente a tabela que deseja fazer o cadastro: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('digite um valor valido: '))
        cadastrar(tabela)

    if resp == 'r':
        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('digite o numero equivalente a tabela que deseja fazer a consulta: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('digite um valor valido: '))
        consultar(tabela)

    if resp == 'u':
        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('digite o numero equivalente a tabela que deseja fazer a alteração: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('digite um valor valido: '))
        alterar(tabela)

    if resp == 'd':
        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('digite o numero equivalente a tabela que deseja fazer a exclusão: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('digite um valor valido: '))
        deletar(tabela)

    if resp == 's':
        finalizar()

    if resp == 't':
        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('digite o numero equivalente a tabela que deseja fazer a soma de registros: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('digite um valor valido: '))
        TotalRegistros(tabela)

    if resp == 'v':
        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('digite o numero equivalente a tabela que deseja fazer a soma de registros: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('digite um valor valido: '))
        consultarTudo(tabela)

    if resp == 'e':
        print('''
                1 - TABELA FIGURINHAS
                0- TABELA ESPECIAIS''')

        tabela = int(input('digite o numero equivalente a tabela que deseja fazer a soma de registros: '))
        while tabela != 1 and tabela != 0:
            tabela = int(input('digite um valor valido: '))
        consutarEspecifico(tabela)
