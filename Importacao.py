# -*- coding: latin-1 -*-
from Funcoes.Funcoes_Arquivos import *
from datetime import datetime, date

lcont = int(0)
LCPF = int(0)
LPRIVATE = int(0)
LINCOMPLETO = int(0)
LDTULTCOMPRA = datetime
LTICKET_MEDIO = int(0)
LTICKET_ULT_COMPRA = int(0)
LLOJA_MAIS_FREQ = int(0)
LLOJA_ULT_COMPRA = int(0)
LCPFVALIDO = str
LCNPJ1VALIDO = str
LCNPJ2VALIDO = str
LDT_ATUALIZACAO = date
LCONECTA = int(0)

conn = None

print("inicio: ", datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

resultado = importar()
for linha in resultado:
    lcont = lcont + 1
    if lcont > 1:
        if lcont == 2:
            conn = ConectaBD();
        linha = " ".join(linha.split())
        lista = linha.split(" ")
        LCPF = lista[0].replace(".", "").replace("-", "").replace("/", "")
        LPRIVATE = lista[1]
        LINCOMPLETO = lista[2]

        if lista[3] == 'NULL':
            LDTULTCOMPRA = None
        else:
            LDTULTCOMPRA = datetime.strptime(lista[3], '%Y-%m-%d').date()
            LDTULTCOMPRA = LDTULTCOMPRA.strftime('%d/%m/%Y')

        if lista[4] == 'NULL':
            LTICKET_MEDIO = None
        else:
            LTICKET_MEDIO = lista[4].replace(",", ".")

        if lista[5] == 'NULL':
            LTICKET_ULT_COMPRA = None
        else:
            LTICKET_ULT_COMPRA = lista[5].replace(",", ".")

        if lista[6] == 'NULL':
            LLOJA_MAIS_FREQ = None
        else:
            LLOJA_MAIS_FREQ = lista[6].replace(".", "").replace("-", "").replace("/", "")

        if lista[7] == 'NULL':
            LLOJA_ULT_COMPRA = None
        else:
            LLOJA_ULT_COMPRA = lista[7].replace(".", "").replace("-", "").replace("/", "")

        LCPFVALIDO = 'N'
        if cpf_validate(LCPF):
            LCPFVALIDO = 'S'

        LCNPJ1VALIDO = 'N'
        if LLOJA_MAIS_FREQ and cnpj_validate(LLOJA_MAIS_FREQ):
            LCNPJ1VALIDO = 'S'

        LCNPJ2VALIDO = 'N'
        if LLOJA_ULT_COMPRA and cnpj_validate(LLOJA_ULT_COMPRA):
            LCNPJ2VALIDO = 'S'

        LDT_ATUALIZACAO =date.today().strftime('%d/%m/%Y')

        Insert_reg(conn, LCPF, LPRIVATE, LINCOMPLETO, LDTULTCOMPRA,
                   LTICKET_MEDIO, LTICKET_ULT_COMPRA, LLOJA_MAIS_FREQ,
                   LLOJA_ULT_COMPRA, LCPFVALIDO, LCNPJ1VALIDO, LCNPJ2VALIDO, LDT_ATUALIZACAO)

DesconectaBD(conn)

print("fim..: ", datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
