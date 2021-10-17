class Pregunta():

     def __init__(self,codigoPregunta,textoPregunta,opcionesPregunta,opcionCorrecta,dificultad,categoria):
         self.codigoPregunta= codigoPregunta
         self.textoPregunta= textoPregunta
         self.opcionesPregunta= opcionesPregunta
         self.opcionCorrecta= opcionCorrecta
         self.dificultad= dificultad
         self.categoria= categoria

     def __repr__(self):
         repre= "Pregunta:"+" "+self.textoPregunta+" "+"con una dificultad:"+" "+self.dificultad+" "+"De categoria:"+" "+self.categoria.nombreCategoria
         return repre

     def cumple(self, especificacion):
        dict_pregunta = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_pregunta  or dict_pregunta[k] != especificacion.get_value(k):
                return False
        return True



