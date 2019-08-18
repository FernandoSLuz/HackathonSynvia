#!/usr/bin/python3

import MySQLdb

try:
    con = MySQLdb.connect(host='localhost', user='admin', passwd='4linux', db='projeto')

    cur = con.cursor()
except Exception as e:
    print('Erro: {}'.format(e))

try:
    # nome = input('Digite o nome: ')
    # id = input("Digite o ID do campo a ser atualizado: ")
    # kill = int(input('Digite o número de kills: '))
    cur.execute("select * from npc;")
    print(cur.fetchall())
except Exception as e:
    con.rollback()
    print('Erro: {}'.format(e))
finally:
    cur.close()
    con.close()
