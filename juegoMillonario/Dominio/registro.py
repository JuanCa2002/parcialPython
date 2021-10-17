from juegoMillonario.Dominio.amigo import Amigo
from juegoMillonario.Dominio.especificacion import Especificacion
from juegoMillonario.Dominio.historial import Historial
from juegoMillonario.Dominio.jugador import Jugador


class Registro():

    def __init__(self):
        self.jugadores= []
        self.preguntas= []
        self.amigos= []
        self.historiales= []
        self.partidas= []

    def agregar_jugador(self,jugador):
        if type(jugador) == Jugador:
            especUsuario = Especificacion()
            especCedula= Especificacion()
            especCedula.agregar_parametro('cedula', jugador.cedula)
            especUsuario.agregar_parametro('usuario', jugador.usuario)
            if len(list(self.buscar_jugador(especUsuario))) == 0 and len(list(self.buscar_jugador(especCedula)))==0:
                self.jugadores.append(jugador)
            else:
                raise Exception('el jugador ya existe en el sistema, verifique su cedula o usuario')

    def buscar_jugador(self,especificacion):
        for g in self.jugadores:
            if g.cumple(especificacion):
                yield g

    def agregar_historial(self,historial):
        if type(historial) == Historial:
            espec = Especificacion()
            espec.agregar_parametro('codigoHistorial', historial.codigoHistorial)
            if len(list(self.buscar_historial(espec))) == 0:
                self.historiales.append(historial)
            else:
                raise Exception('el historial ya existe en el sistema, verifique el codigo')

    def buscar_historial(self,especificacion):
        for g in self.historiales:
            if g.cumple(especificacion):
                yield g

    def agregar_amigo(self,amigo):
        if type(amigo) == Amigo:
            especCodigo = Especificacion()
            especCedula= Especificacion()
            especCodigo.agregar_parametro('codigoAmigo', amigo.codigoAmigo)
            especCedula.agregar_parametro('cedula', amigo.cedula)
            if len(list(self.buscar_amigo(especCodigo))) == 0 and len(list(self.buscar_amigo(especCedula)))==0:
                self.amigos.append(amigo)
            else:
                raise Exception('esta amigo ya existe en el sistema , verifique su cedula o usuario')

    def buscar_amigo(self,especificacion):
        for g in self.amigos:
            if g.cumple(especificacion):
                yield g
