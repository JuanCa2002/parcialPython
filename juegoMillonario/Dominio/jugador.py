from juegoMillonario.Dominio.persona import Persona
class Jugador(Persona):

    def __init__(self,codigoJugador,cedula,nombre,apellido,edad,correo,usuario,contrasena):

        super().__init__(cedula,nombre,apellido,edad,correo)
        self.codigoJugador= codigoJugador
        self.usuario= usuario
        self.contrasena= contrasena



    def __repr__(self):
       repre= "Jugador con nombre de usuario:"+" "+self.usuario
       return repre

    def cumple(self, especificacion):
        dict_jugador = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_jugador or dict_jugador[k] != especificacion.get_value(k):
                return False
        return True

    def cambioUsuario(self,nuevoUsuario):
        self.usuario= nuevoUsuario

    def cambioContrasena(self,nuevaContrasena):
        self.contrasena= nuevaContrasena


