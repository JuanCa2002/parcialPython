import sqlite3

from juegoMillonario.Dominio.historial import Historial


class PersistenciaHistorial():
    def __init__(self):
        self.con = sqlite3.connect("quien_quiere_ser_millonario.sqlite")

    def connect(self):
        self.crear_tabla_historial()


    def crear_tabla_historial(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE HISTORIAL(codigoHistorial text primary key)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_historial(self, historial: Historial):
        cursor = self.con.cursor()
        query = "INSERT INTO HISTORIAL(codigoHistorial) values(" \
                f" ?)"
        cursor.execute(query, (str(historial.codigoHistorial)))
        self.con.commit()

    def consultar_tabla_historial(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM HISTORIAL"
        cursor.execute(query)
        rows = cursor.fetchall()
        return [Historial(*row) for row in rows]
