import sqlite3
from pathlib import Path

class BaseDAL:
    def __init__(self):
        self.__conexao = None
        self.__cursor = None

    def __enter__(self):
        BASE_DADOS = Path(__file__).parent / "data_base_page.sqlite3"

        self.__conexao = sqlite3.connect(BASE_DADOS)
        self.__cursor = self.__conexao.cursor()
        self.__conexao.commit()
        self.__criarBanco()

        return self.__cursor
    
    def __exit__(self, excessaoClasse, excessao, retornoErro):
        self.__cursor.close()
        self.__conexao.commit()
        self.__conexao.close()

        if excessaoClasse:
            print(excessaoClasse)

        if excessao:
            print(excessao)

        if retornoErro:
            print(retornoErro)

    def __criarBanco(self):
        self.__cursor.execute(
            "create table if not exists clientes"
            "("
            "id                            integer primary key autoincrement,"
            "nome                          text not null,"
            "email                         text not null,"
            "numero_celular                text not null,"
            "assunto                       text,"
            "solicitacao                   text"
            ");"
        )