class Categoria():

    def __init__(self,codigoCategoria,nombreCategoria):

       self.codigoCategoria= codigoCategoria
       self.nombreCategoria= nombreCategoria


    def __repr__(self):
        repre= "Categoria:"+" "+self.nombreCategoria
        return repre

