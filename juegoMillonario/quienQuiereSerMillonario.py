import random
import uuid

from juegoMillonario.Dominio.amigo import Amigo
from juegoMillonario.Dominio.especificacion import Especificacion
from juegoMillonario.Dominio.historial import Historial
from juegoMillonario.Dominio.jugador import Jugador
from juegoMillonario.Dominio.partida import Partida
from juegoMillonario.Infraestructura.persistenciaJugador import Persistencia
from juegoMillonario.Dominio.pregunta import Pregunta
from juegoMillonario.Dominio.registro import Registro
from juegoMillonario.Dominio.categoria import Categoria
import os
saver= Persistencia()
saver.connect()
def generarRegistros():
  registro= Registro()
  jugadores= saver.consultar_tabla_jugador()
  for jugador in jugadores:
       registro.agregar_jugador(jugador)
  for file in os.listdir("./files"):
              if '.jsonPregunta' in file:
                 registro.preguntas.append(Persistencia.load_json_pregunta(file))
              elif '.jsonPartida' in file:
                 registro.partidas.append(Persistencia.load_json_partida(file))
              elif '.jsonHistorial' in file:
                  registro.agregar_historial(Persistencia.load_json_historial(file))
              elif '.jsonAmigo' in file:
                  registro.agregar_amigo(Persistencia.load_json_amigo(file))
  return registro

def registrarse(registro):
 print("BIENVENIDO A NUESTRO FORMULARIO DE REGISTRO, PORFAVOR DILIGENCIA LOS SIGUIENTES DATOS"
       "PARA EMPEZAR LA EXPERIENCIA DE JUEGO Y QUE PODAMOS LLEVAR UN REGISTRO DE TUS PARTIDAS")
 codigoJugador= uuid.uuid4()
 cedula= str(input("Ingrese su cedula:"))
 nombre= str(input("Ingrese su nombre:"))
 apellido= str(input("Ingrese su apellido:"))
 edad= int(input("Ingrese su edad:"))
 correo= str(input("Ingrese su correo:"))
 usuario= str(input("Ingrese su usuario:"))
 contrasena= str(input("Ingrese su contrasena"))
 jugador= Jugador(codigoJugador,cedula,nombre,apellido,edad,correo,usuario,contrasena)
 try:
  registro.agregar_jugador(jugador)
  saver.guardar_jugador(jugador)
  print("Se registro con exito")
 except Exception as ex:
     print(ex)


def iniciarSesion(registro):
    print("INGRESE SU USUARIO Y CONTRASEÑA PARA COMENZAR A JUGAR!!")
    espc= Especificacion()
    usuario= str(input("Usuario:"))
    contrasena= str(input("contrasena:"))
    espc.agregar_parametro("usuario",usuario)
    espc.agregar_parametro("contrasena",contrasena)
    jugadores=list(registro.buscar_jugador(espc))
    if len(jugadores)!=0:
        jugador= jugadores[0]
        sesionIniciada= True
        while sesionIniciada:
          print("Bienvenido "+" "+jugador.nombre)
          print("""Elige la opcion que deseas:
                   1.Jugar nueva partida
                   2.Jugar partida ya iniciada
                   3.Hitorial de partidas
                   4.Registrar amigo
                   5.Salir""")
          sesionIniciada= input("Ingrese la opcion que quiere:")
          if sesionIniciada== "1":
            responderPreguntas(registro,jugador,"no hay")
          elif sesionIniciada == "2":
            partidaElegida=mostrarPartidasGuardadas(registro,jugador.cedula)
            if partidaElegida == "salir":
                print("Menu inicial:"+"\n")
            else:
               responderPreguntas(registro,jugador,partidaElegida)
          elif sesionIniciada== "3":
              mostrarHistorialPartidas(registro,jugador.cedula)
          elif sesionIniciada == "4":
              registrarAmigo(registro,jugador)
          elif sesionIniciada == "5":
              sesionIniciada= False
          elif sesionIniciada != "":
              print("Opcion invalida")
    else:
        print("No se encontro el usuario, porfavor verifica tu usuario y contraseña")

def responderPreguntas(registro,jugador,partida):
    b=["a","b","c","d"]
    preguntas=" "
    puntaje=0
    historiales= registro.historiales
    for historial in historiales:
        if historial.codigoHistorial== jugador.cedula:
            historialActual= historial
        else:
          historialActual= Historial(jugador.cedula)
    contador= 0
    perdido= False
    ganado= False
    pausa= False
    if type(partida)!= Partida:
        codigoPartida= uuid.uuid4()
        partida= Partida(codigoPartida,puntaje,jugador)
        preguntas= registro.preguntas
        random.shuffle(preguntas)
    else:
        preguntas=cargarPartida(registro,partida)
        puntaje=partida.puntaje
        contador=len(partida.preguntasAcertadas)
    random.shuffle(preguntas)
    opciones= dict()
    for pregunta in preguntas:
        print(pregunta.textoPregunta)
        opcionesRevueltas= pregunta.opcionesPregunta
        random.shuffle(opcionesRevueltas)
        for i in range(0,4):
         print(b[i]+" "+opcionesRevueltas[i])
         opciones[b[i]]=opcionesRevueltas[i]
        print("1. Guardar partida   2.Salir   3.Ayuda del publico  4. 50/50  5. llamar un amigo"+"\n")
        respuesta= input("Ingrese la respuesta correcta o la opcion de ayuda:"+"\n")
        ayuda=True
        while ayuda:
            if respuesta == "1":
                Persistencia.save_json_partida(partida)
                print("Partida guardada")
                ayuda= False
                pausa= True
            elif respuesta == "2":
                ayuda= False
                perdido= True
            elif respuesta == "3":

                if partida.ayudaPublico== False:
                  votacionesErradas=[]
                  votacionAcertada= random.randint(50,100)
                  resultado1=100-votacionAcertada
                  votacion1=random.randint(0,resultado1)
                  votacionesErradas.append(votacion1)
                  resultado2= resultado1-votacion1
                  votacion2= random.randint(0,resultado2)
                  votacionesErradas.append(votacion2)
                  resultado3= resultado2-votacion2
                  votacion3= random.randint(0,resultado3)
                  votacionesErradas.append(votacion3)
                  partida.utilizarAyudaPublico()
                  print(pregunta.textoPregunta)
                  j=0
                  for i in range(0,4):
                      print(b[i]+" "+opcionesRevueltas[i])
                      opciones[b[i]]=opcionesRevueltas[i]
                  for i in range(0,len(opciones)):
                        if opciones[b[i]]== pregunta.opcionCorrecta:
                             print(b[i]+" "+"votacion del publico de :"+str(votacionAcertada))
                        else:
                            votacion= votacionesErradas[j]
                            j=j+1
                            print(b[i]+" "+"votacion del publico de :"+str(votacion))
                  print("1. Guardar partida   2.Salir   3.Ayuda del publico  4. 50/50  5. llamar un amigo"+"\n")
                  respuesta= input("Ingrese la respuesta correcta o la opcion de ayuda:"+"\n")
                else:
                    print("Ya utilizaste este comodin")
                    print(pregunta.textoPregunta)
                    for i in range(0,4):
                      print(b[i]+" "+opcionesRevueltas[i])
                      opciones[b[i]]=opcionesRevueltas[i]
                    print("1. Guardar partida   2.Salir   3.Ayuda del publico  4. 50/50  5. llamar un amigo"+"\n")
                    respuesta= input("Ingrese la respuesta correcta o la opcion de ayuda:"+"\n")
            elif respuesta == "4":
                if partida.ayudaMitad== False:
                     partida.utilizarAyudaMitad()
                     print(pregunta.textoPregunta)
                     for i in range(0,len(opciones)):
                         if opciones[b[i]]== pregunta.opcionCorrecta:
                             print(b[i]+" "+pregunta.opcionCorrecta)
                         else:
                             opcionIncorrecta= opciones[b[i]]
                             opcion= b[i]
                     print(opcion+" "+opcionIncorrecta)
                     print("1. Guardar partida   2.Salir   3.Ayuda del publico  4. 50/50  5. llamar un amigo"+"\n")
                     respuesta= input("Ingrese la respuesta correcta o la opcion de ayuda:"+"\n")
                else:
                    print("Ya utilizaste este comodin")
                    print(pregunta.textoPregunta)
                    for i in range(0,4):
                      print(b[i]+" "+opcionesRevueltas[i])
                      opciones[b[i]]=opcionesRevueltas[i]
                    print("1. Guardar partida   2.Salir   3.Ayuda del publico  4. 50/50  5. llamar un amigo"+"\n")
                    respuesta= input("Ingrese la respuesta correcta o la opcion de ayuda:"+"\n")

            elif respuesta == "5":
                if partida.ayudaAmigo== False:
                   partida.utilizarAyudaAmigo()
                   respuestaAmigo= ayudaAmigo(registro,pregunta,jugador.cedula)
                   print(pregunta.textoPregunta)
                   for i in range(0,4):
                      print(b[i]+" "+opcionesRevueltas[i])
                      opciones[b[i]]=opcionesRevueltas[i]
                   print(respuestaAmigo)
                   print("1. Guardar partida   2.Salir   3.Ayuda del publico  4. 50/50  5. llamar un amigo"+"\n")
                   respuesta= input("Ingrese la respuesta correcta o la opcion de ayuda:"+"\n")
                else:
                    print("Ya utilizaste este comodin")
                    print(pregunta.textoPregunta)
                    for i in range(0,4):
                      print(b[i]+" "+opcionesRevueltas[i])
                      opciones[b[i]]=opcionesRevueltas[i]
                    print("1. Guardar partida   2.Salir   3.Ayuda del publico  4. 50/50  5. llamar un amigo"+"\n")
                    respuesta= input("Ingrese la respuesta correcta o la opcion de ayuda:"+"\n")

            else:
                if opciones[respuesta] == pregunta.opcionCorrecta:
                   contador= contador+1
                   puntaje= puntaje+100
                   partida.nuevaPuntuacion(puntaje)
                   partida.agregarPreguntaAcertada(pregunta)
                   if contador == 3 or contador== 6 or contador==9:
                      print("Acertaste¡,el dinero acumulado es de:"+" "+str(partida.puntaje)+" "+"y estas en seguro")
                   else:
                      print("Acertaste¡,el dinero acumulado es de:"+" "+str(partida.puntaje))
                   if len(partida.preguntasAcertadas)== 10:
                       print("Felicidades ganaste!")
                       partida.partidaTerminada()
                       partida.estado=False
                       Persistencia.save_json_partida(partida)
                       historialActual.agregarPartida(partida)
                       saver.save_json_historial(historialActual)
                       ganado= True
                   ayuda=False
                else:
                    if contador == 3 or contador== 6 or contador==9 :
                        print("Lo sentimos, no es la respuesta correcta, el dinero obtenido es de:"+" "+str(partida.puntaje))
                        partida.partidaTerminada()
                        historialActual.agregarPartida(partida)
                        saver.save_json_historial(historialActual)
                    else:
                        if contador==1 or contador==2:
                         partida.nuevaPuntuacion(0)
                        elif contador ==4 or contador==5:
                         partida.nuevaPuntuacion(300)
                        elif contador ==7 or contador==8:
                         partida.nuevaPuntuacion(600)
                        print("Lo sentimos, no es la respuesta correcta, el dinero obtenido es de:"+" "+str(partida.puntaje))
                        partida.partidaTerminada()
                        historialActual.agregarPartida(partida)
                        saver.save_json_historial(historialActual)
                    ayuda= False
                    perdido= True
        if perdido== True or ganado==True or pausa==True:
         break
def mostrarPartidasGuardadas(registro,cedula):
    partidaElegida=""
    partidas= registro.partidas
    opcionesPartidas= dict()
    print("Estas son tus partidas guardadas:")
    for i in range(0,len(partidas)):
        if partidas[i].jugador.cedula == cedula and partidas[i].estado== True :
          print(str(i+1)+"."+"partida:"+" "+str(partidas[i].codigoPartida)+" "+"puntaje hasta el momento:"+" "+str(partidas[i].puntaje))
          opcionesPartidas[i+1]=partidas[i]
    opcion=int(input("Ingrese el numero de la partida que quiere continuar o un cero para salir:"))
    if opcion== 0:
        partidaElegida= "salir"
    else:
        partidaElegida= opcionesPartidas[opcion]
    return partidaElegida

def mostrarHistorialPartidas(registro,cedula):
    historiales= registro.historiales
    contador= 0
    print("Estas son tus ultimas 10 partidas jugadas:")
    for historial in historiales:
        if historial.codigoHistorial == cedula:
           partidasJugadas= historial.partidas
           if contador<10:
               for partida in partidasJugadas:
                   if len(partida.preguntasAcertadas)== 10:
                        resultado= "ganada"
                   else:
                       resultado= "perdida"
                   print(str(contador+1)+" . "+"Partida "+resultado+" "+"con una ganancia de: "+str(partida.puntaje ))
                   contador=contador+1

def registrarAmigo(registro,jugador):
    cantidadAmigos= int(input("Elija la cantidad de amigos que quiere registrar:"))
    for i in range(0,cantidadAmigos):
        codigoAmigo= uuid.uuid4()
        cedula= str(input("Ingrese la cedula de su amigo:"))
        nombre= str(input("Ingrese el nombre de su amigo:"))
        apellido= str(input("Ingrese el apellido de su amigo:"))
        edad= int(input("Ingrese la edad de su amigo:"))
        correo= str(input("Ingrese el correo de su amigo:"))
        numeroTelefono= str(input("Ingrese el telefono de su amigo:"))
        nivelConocimiento=[]
        print("""Ingrese el nivel de conocimiento de su amigo en cada categoria
                 1. Alto
                 2. Medio
                 3. Bajo""")
        for i in range(0,5):
            categorias= ['Arte','Deportes','Ciencia','Ciencia ficcion y fantasia','Historia']
            conocimiento=input("el nivel de conocimiento de su amigo en la categoria "+categorias[i]+" "+"es de:")
            if conocimiento== "1":
               nivelConocimiento.append("Alto")
            elif conocimiento== "2":
                nivelConocimiento.append("Medio")
            elif conocimiento == "3":
                nivelConocimiento.append("Bajo")
        amigo= Amigo(codigoAmigo,cedula,nombre,apellido,edad,correo,numeroTelefono,nivelConocimiento,jugador)
        try:
          registro.agregar_amigo(amigo)
          saver.save_json_amigo(amigo)
          print("Se agrego tu amigo con exito")
        except Exception as ex:
           print(ex)

def ayudaAmigo(registro,pregunta,cedula):
    amigos=registro.amigos
    porcentajeSeguro=""
    respuestaAmigo= ""
    categorias= ['Arte','Deportes','Ciencias','Fantasia y ciencia ficcion','Historia']
    for amigo in amigos:
      if amigo.jugador.cedula== cedula:
          print("Nombre: "+amigo.nombre+" "+"Telefono: "+amigo.numeroTelefono)
          for i in range(0,len(categorias)):
              if categorias[i]== pregunta.categoria.nombreCategoria:
               print("Categoria: "+categorias[i]+" "+"conocimiento: "+amigo.nivelConocimientoCategorias[i]+"\n")
    respuesta=input("Ingrese el numero del amigo elegido para llamarlo:")
    espc= Especificacion()
    espc.agregar_parametro("numeroTelefono",respuesta)
    amigob=list(registro.buscar_amigo(espc))
    amigo=amigob[0]
    for i in range(0,len(categorias)):
        if categorias[i]== pregunta.categoria.nombreCategoria:
            conocimientoCategoria=amigo.nivelConocimientoCategorias[i]
    if pregunta.dificultad== "dificil" and conocimientoCategoria== "Alto":
        respuestaAmigo=pregunta.opcionCorrecta
        numeroSeguro= random.randint(70,90)
        porcentajeSeguro= str(numeroSeguro)+"%"
    elif pregunta.dificultad== "facil" and conocimientoCategoria== "Alto":
         respuestaAmigo=pregunta.opcionCorrecta
         porcentajeSeguro= "100"+"%"
    elif pregunta.dificultad== "medio" and conocimientoCategoria== "Alto":
        respuestaAmigo=pregunta.opcionCorrecta
        numeroSeguro= random.randint(85,100)
        porcentajeSeguro= str(numeroSeguro)+"%"
    elif pregunta.dificultad== "dificil" and conocimientoCategoria== "Medio":
         opcionesRespuesta=[pregunta.opcionCorrecta]
         for opcionIncorrecta in pregunta.opcionesPregunta:
             if opcionIncorrecta!= pregunta.opcionCorrecta:
                 opcionesRespuesta.append(opcionIncorrecta)
         respuestaAmigo=random.choice(opcionesRespuesta)
         numeroSeguro= random.randint(50,70)
         porcentajeSeguro= str(numeroSeguro)+"%"
    elif pregunta.dificultad== "medio" and conocimientoCategoria== "Medio":
         opcionesRespuesta=[pregunta.opcionCorrecta]
         for opcionIncorrecta in pregunta.opcionesPregunta:
             if opcionIncorrecta!= pregunta.opcionCorrecta:
                 opcionesRespuesta.append(opcionIncorrecta)
         respuestaAmigo=random.choice(opcionesRespuesta)
         numeroSeguro= random.randint(60,75)
         porcentajeSeguro= str(numeroSeguro)+"%"

    elif pregunta.dificultad== "facil" and conocimientoCategoria== "Medio":
         respuestaAmigo=pregunta.opcionCorrecta
         numeroSeguro= random.randint(70,90)
         porcentajeSeguro= str(numeroSeguro)+"%"

    elif pregunta.dificultad== "dificil" and conocimientoCategoria== "Bajo":
        respuestaAmigo= random.choice(pregunta.opcionesPregunta)
        numeroSeguro= random.randint(10,25)
        porcentajeSeguro= str(numeroSeguro)+"%"
    elif pregunta.dificultad== "medio" and conocimientoCategoria== "Bajo":
        respuestaAmigo= random.choice(pregunta.opcionesPregunta)
        numeroSeguro= random.randint(30,45)
        porcentajeSeguro= str(numeroSeguro)+"%"
    elif pregunta.dificultad== "bajo" and conocimientoCategoria== "Bajo":
        opcionesRespuesta=[pregunta.opcionCorrecta]
        for opcionIncorrecta in pregunta.opcionesPregunta:
             if opcionIncorrecta!= pregunta.opcionCorrecta:
                 opcionesRespuesta.append(opcionIncorrecta)
        respuestaAmigo=random.choice(opcionesRespuesta)
        numeroSeguro= random.randint(50,60)
        porcentajeSeguro= str(numeroSeguro)+"%"

    respuestaFinal= "la respuesta de tu amigo es: "+ respuestaAmigo+" "+"Con un porcentaje de seguridad de un "+porcentajeSeguro
    return respuestaFinal

def cargarPartida(registro,partida):
    preguntasRestantes=[]
    preguntasExistentes= registro.preguntas
    for i in range(0,len(preguntasExistentes)):
        verificacion= False
        pregunta= preguntasExistentes[i].codigoPregunta
        for j in range(0,len(partida.preguntasAcertadas)):
            if partida.preguntasAcertadas[j].codigoPregunta== pregunta:
                verificacion= True
        if verificacion == False:
            preguntasRestantes.append(preguntasExistentes[i])



    return preguntasRestantes








if __name__== '__main__':
  resp= True
  while resp:
      registro= generarRegistros()
      print ("""
       BIENVENIDO AL JUEGO DE QUIEN QUIERE SER MILLONARIO, ELIGE ENTRE NUESTRAS OPCIONES
       Y DIVIERTETE COMO NUNCA!
        
        1.Iniciar Sesion.
        2.Registrarme.
        3.Salir y terminar
        
        """)
      resp= input("Ingrese una de las opciones que quiera:")
      if resp == "1":
        iniciarSesion(registro)
      elif resp== "2":
       registrarse(registro)
      elif resp== "3":
          resp=False
      elif resp != "":
          print("Opcion invalida")





