from juegoMillonario.Dominio.persona import Persona
class Amigo(Persona):

    def __init__(self,codigoAmigo,cedula,nombre,apellido,edad,correo,numeroTelefono,nivelConocimientoCategorias,jugador):

        super().__init__(cedula,nombre,apellido,edad,correo)
        self.codigoAmigo= codigoAmigo
        self.nivelConocimientoCategorias= nivelConocimientoCategorias
        self.jugador= jugador
        self.numeroTelefono= numeroTelefono

    def __repr__(self):
        repre= "Nombre:"+" "+self.nombre+" "+"Amigo de :"+" "+self.jugador.nombre
        return repre

    def cumple(self, especificacion):
        dict_amigo = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_amigo or dict_amigo[k] != especificacion.get_value(k):
                return False
        return True



