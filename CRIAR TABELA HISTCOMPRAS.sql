-- TABELA POSTGRESQL

DROP TABLE HISTCOMPRAS;

CREATE TABLE HISTCOMPRAS
(
  CPF                   bigint      NOT NULL,         
  PRIVATEX              INTEGER       NOT NULL,
  INCOMPLETO            INTEGER       NOT NULL,
  DT_ULT_COMPRA         DATE,            
  TICKET_MEDIO          DECIMAL,
  TICKET_ULT_COMPRA     DECIMAL,
  LOJA_MAIS_FREQ        bigint,
  LOJA_ULT_COMPRA       bigint,
  CPF_VALIDO            CHAR(1),
  CNJP_FREQ_VALIDO      CHAR(1),
  CNJP_ULT_VALIDO       CHAR(1),
  DT_ATUALIZACAO        DATE,
	PRIMARY KEY (CPF)
);  
