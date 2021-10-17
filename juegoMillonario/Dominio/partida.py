class Partida():
    def __init__(self,codigoPartida,puntaje,jugador):
        self.codigoPartida= codigoPartida
        self.puntaje= puntaje
        self.preguntasAcertadas= []
        self.estado=True
        self.ayudaMitad= False
        self.ayudaPublico= False
        self.ayudaAmigo= False
        self.jugador= jugador


    def __repr__(self):
        repre= "Partida del jugador:"+" "+self.jugador.usuario+" "+"Puntaje:"+" "+self.puntaje
        return repre

    def nuevaPuntuacion(self,nuevaPuntuacion):
        self.puntaje= nuevaPuntuacion

    def cumple(self, especificacion):
        dict_partida = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_partida or dict_partida[k] != especificacion.get_value(k):
                return False
        return True

    def agregarPreguntaAcertada(self,preguntaAcertada):
        self.preguntasAcertadas.append(preguntaAcertada)

    def partidaTerminada(self):
        self.estado= False

    def utilizarAyudaMitad(self):
        self.ayudaMitad= True

    def utilizarAyudaPublico(self):
        self.ayudaPublico= True

    def utilizarAyudaAmigo(self):
        self.ayudaAmigo= True


