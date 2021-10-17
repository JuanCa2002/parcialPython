class Historial():

    def __init__(self,codigoHistorial):
        self.codigoHistorial= codigoHistorial
        self.partidas= []

    def cumple(self, especificacion):
        dict_historial = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_historial or dict_historial[k] != especificacion.get_value(k):
                return False
        return True

    def agregarPartida(self,partida):
        self.partidas.append(partida)



