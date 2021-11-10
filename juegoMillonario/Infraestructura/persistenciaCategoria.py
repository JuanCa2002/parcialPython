import sqlite3

from juegoMillonario.Dominio.categoria import Categoria


class PersistenciaCategoria():
    def __init__(self):
        self.con = sqlite3.connect("quien_quiere_ser_millonario.sqlite")

    def connect(self):
     self.crear_tabla_categoria()

    def crear_tabla_categoria(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE CATEGORIA(codigoCategoria text primary key, nombreCategoria text)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_categoria(self, categoria : Categoria):
        cursor = self.con.cursor()
        query = "INSERT INTO CATEGORIA(codigoCategoria , nombreCategoria ) VALUES(" \
                f" ?,?)"
        cursor.execute(query, (str(categoria.codigoCategoria), categoria.nombreCategoria))
        self.con.commit()

    def consultar_tabla_categoria(self):
        cursor=self.con.cursor()
        query="SELECT * FROM CATEGORIA"
        cursor.execute(query)
        rows= cursor.fetchall()
        return [Categoria(*row)for row in rows]

