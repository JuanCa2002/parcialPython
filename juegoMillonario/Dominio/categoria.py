class Categoria():

    def __init__(self, codigoCategoria, nombreCategoria):

        self.codigoCategoria = codigoCategoria
        self.nombreCategoria = nombreCategoria

    def __repr__(self):
        repre = "Categoria:" + " " + self.nombreCategoria
        return repre

    def cumple(self, especificacion):
        dict_category = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_category or dict_category[k] != especificacion.get_value(k):
                return False
        return True
