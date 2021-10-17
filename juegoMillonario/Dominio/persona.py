class Persona():

    def __init__(self,cedula,nombre,apellido,edad,correo):
        self.cedula= cedula
        self.nombre= nombre
        self.apellido= apellido
        self.edad= edad
        self.correo= correo


    def cambioNombre(self,nuevoNombre):
        self.nombre= nuevoNombre


    def cumpleanos(self,nuevaEdad):
        self.edad= nuevaEdad

    def nuevoCorreo(self,nuevoCorreo):
        self.correo= nuevoCorreo


