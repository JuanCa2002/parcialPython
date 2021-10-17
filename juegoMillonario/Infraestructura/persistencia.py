import jsonpickle
import sqlite3
from juegoMillonario.Dominio.jugador import Jugador
class Persistencia():

  def __init__(self):
    self.con = sqlite3.connect("quien_quiere_ser_millonario.sqlite")

  def connect(self):
     self.crear_tabla_jugador()



  def crear_tabla_jugador(self):
      try:
        cursor = self.con.cursor()
        query = "CREATE TABLE JUGADOR(codigoJugador text primary key, cedula text," \
                    " nombre text, apellido text,edad int," \
                    " correo float,usuario text,contrasena text) "
        cursor.execute(query)
      except sqlite3.OperationalError as ex:
            pass

  def guardar_jugador(self, jugador: Jugador):
        cursor = self.con.cursor()
        query = "insert into JUGADOR(codigoJugador , cedula ," \
                " nombre , apellido ,edad," \
                " correo,usuario,contrasena) values(" \
                f" ?,?,?,?,?,?,?,?)"
        cursor.execute(query, (str(jugador.codigoJugador),jugador.cedula,jugador.nombre,
                               jugador.apellido,jugador.edad,jugador.correo,jugador.usuario,jugador.contrasena))
        self.con.commit()

  def consultar_tabla_jugador(self):
        cursor = self.con.cursor()
        query= "SELECT * FROM JUGADOR"
        cursor.execute(query)
        rows= cursor.fetchall()
        return [Jugador(*row) for row in rows]

  @classmethod
  def save_json_pregunta(cls, pregunta):
        text_open = open("files/" + str(pregunta.codigoPregunta) + '.jsonPregunta', mode='w')
        json_gui = jsonpickle.encode(pregunta)
        text_open.write(json_gui)
        text_open.close()

  @classmethod
  def load_json_pregunta(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        pregunta = jsonpickle.decode(json_gui)
        text_open.close()
        return pregunta

  @classmethod
  def save_json_partida(cls, partida):
        text_open = open("files/" + str(partida.codigoPartida) + '.jsonPartida', mode='w')
        json_gui = jsonpickle.encode(partida)
        text_open.write(json_gui)
        text_open.close()

  @classmethod
  def load_json_partida(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        partida = jsonpickle.decode(json_gui)
        text_open.close()
        return partida

  @classmethod
  def save_json_historial(cls, historial):
        text_open = open("files/" + str(historial.codigoHistorial) + '.jsonHistorial', mode='w')
        json_gui = jsonpickle.encode(historial)
        text_open.write(json_gui)
        text_open.close()

  @classmethod
  def load_json_historial(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        historial = jsonpickle.decode(json_gui)
        text_open.close()
        return historial

  @classmethod
  def save_json_amigo(cls, amigo):
        text_open = open("files/" + str(amigo.codigoAmigo) + '.jsonAmigo', mode='w')
        json_gui = jsonpickle.encode(amigo)
        text_open.write(json_gui)
        text_open.close()

  @classmethod
  def load_json_amigo(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        amigo = jsonpickle.decode(json_gui)
        text_open.close()
        return amigo


