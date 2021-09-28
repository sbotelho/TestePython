#!/usr/bin/python
# -*- coding: latin-1 -*-
from itertools import cycle
import psycopg2

def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    #if cpf == cpf[::-1]:
    #    return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

def cnpj_validate(cnpj: str) -> bool:
    if len(cnpj) != 14:
        return False

    if cnpj in (c * 14 for c in "1234567890"):
        return False

    cnpj_r = cnpj[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False

    return True

def importar():
    with open("base_teste.txt", "r") as inv:
        linhas = inv.readlines()
    return linhas

def Insert_reg(conn, LCPF, LPRIVATE, LINCOMPLETO, LDTULTCOMPRA,
                   LTICKET_MEDIO, LTICKET_ULT_COMPRA, LLOJA_MAIS_FREQ,
                   LLOJA_ULT_COMPRA, LCPFVALIDO, LCNPJ1VALIDO, LCNPJ2VALIDO,
                   LDT_ATUALIZACAO):

    sql = """INSERT INTO HISTCOMPRAS (CPF, PRIVATEX, INCOMPLETO, DT_ULT_COMPRA, 
                    TICKET_MEDIO, TICKET_ULT_COMPRA,
				   LOJA_MAIS_FREQ, LOJA_ULT_COMPRA, CPF_VALIDO, CNJP_FREQ_VALIDO, CNJP_ULT_VALIDO,
				   DT_ATUALIZACAO
                   ) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    dados = (LCPF, LPRIVATE, LINCOMPLETO, LDTULTCOMPRA,
                   LTICKET_MEDIO, LTICKET_ULT_COMPRA, LLOJA_MAIS_FREQ,
                   LLOJA_ULT_COMPRA, LCPFVALIDO, LCNPJ1VALIDO, LCNPJ2VALIDO,
                   LDT_ATUALIZACAO
                   )

    try:
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, dados)
        # commit the changes to the database
        #conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def ConectaBD():

    conn = None

    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=TESTENEOWAY user=postgres password=ikocaio")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn


def DesconectaBD(conn):

    try:
        if conn is not None:
            # commit the changes to the database
            conn.commit()
            conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn