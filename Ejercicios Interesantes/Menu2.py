import  time # para obtener la fecha y hora.

#Diccionario con los datos de asignaturas (Clave y Nombre de la asignatura. 
Asignatura = {"ISC001":"Programacion 1",
              "ICC001":"Estructura",
              "MED001":"Anatomia 1",
              "DER001":"Frances",
              "HUM059":"Ingles II",
              "CIM004":"Calculo I",
              "HUM110":"Teologia II",
              "ISC103":"Telematica I",
              "ISC095":"Base de Datos I",
              "CIM015":"Estadistica II"}

#Tuplas con las distintas area del docente
Area=("Facultad de negocios", "Facultad de las ingenierias", 
"Facultad de las ciencias humanas y sociales","Facultad de ciencias de la salud", 
"Facultad de ciencias de la salud ")

#Lista con los datos registrados del docente
DatosPrincipales=[
  ["EBD","Edward","M","40","Biologia","Facultad de ciencias de la salud"]
  ]

#Lista con los datos secundarios del docente
DatosSecundarios=[["ISC001","Programacion","Miercoles", "10", "12"]
]

#lista de Datos procesos 
DatosProcesos=[ ["EB11","ISC001","R1","Martes", "10","12","F101"]
]

#Tuplas con distintas aulas
AulasDisponbibles=("F101","A104","J202","F309","J107","A208","T105")

#Especialidades que ofrece UCATECI
Especialidades=["Administracion de la Construccion","Alta Gerencia","Gestion de Recursos Humanos",
"Gerencia Financiera","Gestion Escolar","Mercadeo","Biologia","Fisica","Informatica","Matematica" ]

#Lista de periodos
ListaPeriodo=["R1", "R2", "R3"]

#Login usando recursividad en Python
def login (intentos=1):
    print ("Intento #: ", intentos)
    usuario= input("Nombre de usuario: ").lower()
    clave= input("Digite su contraseña: ").lower()
    if usuario!= "admin" and clave != "admin":
        if intentos<3:
            intentos += 1 
            print(f"Nombre de usuario o contraseña incorrecto!, intentalo otra vez")
            login(intentos)
        else:
            print("Has agotado todos los intentos.")
            
    if usuario== "admin" and clave == "admin":
        print ("Usuario válido. Bienvenido al sistema!\n \n")
        return Menu()
#Informacion del grupo
def Info():
  print ("\nGrupo 3 \nCarga horaria docentes") 
  print("Edward Brito Diaz 2019-0823")
  print("Yessica María Villavizar Hernández 2019-1056")
  print("José Daniel Orrego 2019-0974")
  print ("\n ") 
  return Menu()

#Registrar datos principales del docente
def RegistrarDatosPrincipales():
  print ("\n")
  print (" Registrar datos principales del Docente ".center(70,"="))
  print ("\n")
  print("Por favor introducir las inciales de su nombre como ID")
  IdDocente =  input ("ID-Docente..: ").upper()
  nombre =       input("Nombre..: ").capitalize()

  #Controlando el Sexo
  while True:
    sexo = input ("Sexo..: ").capitalize()
    if sexo == "M" or sexo== "Masculino" or sexo == "F" or sexo=="Femenino":
      break
    else:
      print("Por Favor identifique su sexo")

  #Controlando la edad
  while True:
    edad = int (input( "Edad..: "))
    if edad >0 and edad <100:
      break
    else:
      print("Por Favor proporcione una edad correcta")

  #Especialidad de cada profesor
  while True:
      print ("Especialidades ".center(30,"*"))
      for i in Especialidades:
        print(i)
      print ("".center(30,"*"))
      especialidad=  input("Especialidad..: ").capitalize()
      if especialidad in Especialidades:    
          break
      elif especialidad not in Especialidades:
          print("La especialidad fue registrada con exito.")
          Especialidades.append(especialidad)
          break
  #Controlando el area de la tupla
  while True:
    print ("Areas".center(30,"*")) #Método: center(longitud[, "caracter de relleno"])
    for i in Area:
      print(i)
    print ("".center(30,"*"))

    area1= input("Area..: ").capitalize()
    if area1 in Area:
       break
    else:
       print("El area no esta registrada en nuestro sistema")

  DatosPrincipales.append([IdDocente,nombre,sexo,edad,especialidad,area1])
  return Menu()
#Registrar datos secundarios del docente
def RegistrarDatosSecundarios():
   print ("\n")
   print (" Registrar datos secundarios del Docente ".center(70,"="))
   while True:
      print ("ID de grupos ".center(30,"*"))
      for i in Asignatura.keys():
          print(i)
      print ("".center(30,"*"))
      print ("\n")
      IdGrupo=input("ID-Grupo..: ").upper()
      if IdGrupo in Asignatura.keys():
         break
      else:
         print("El ID del grupo no se encuentra en la base de datos. ")

   while True:
        #Imprimiendo las asignaturas 
       print ("Asignaturas disponibles ".center(30,"*"))
       for i in Asignatura.values():
          print(i)
       print ("".center(30,"*"))
       #Elegir asignatura
       asignatura1=input("Asignatura..: ").capitalize()
       if asignatura1 == Asignatura.get(IdGrupo):
          break
       elif asignatura1 in Asignatura.values():
          Asignatura.get(IdGrupo)
          print("La asignatura que corresponde a ese grupo es: ",Asignatura.get(IdGrupo))
          while True:
              continuar=input("Desea continuar con la materia correspondiente a el ID introducido. Si/No? ").capitalize()
              if continuar == "Si" or continuar =="S":
                print("Gracias, contienue llenando los diferentes datos")
                break
              else:
                print("Elija correctamente el ID del grupo ")
                return RegistrarDatosSecundarios()
              break
       else:
             print("La asignatura no coincide con el ID del grupo")


   print("Complete los siguientes campos para su horario")
   dia= input("Dia..:")
   print("Sistema horario de 24 horas")
   Hora=int(input("Hora incial:"))
   Hora2=int(input("Hora final:"))
   DatosSecundarios.append([IdGrupo,asignatura1,dia,Hora,Hora2]) 
   return Menu()   

#Registrar proceso de datos principales y secundarios, mas enpecifico en carga horaria de docente
def RegistrarProceso():
   while True:
      IdDocente =  input ("ID-Docente..: ").upper()
      if IdDocente in DatosPrincipales[0][0] or IdDocente in DatosPrincipales[1][0]:
        print("EL ID se encuentra registrado")
        break

      else: 
        print("El ID docente no se encuentra registrado")

   while True:
      print ("Periodo educativo".center(30,"*")) 
      for i in ListaPeriodo:
          print(i)
      Periodo= input("Periodo: ").capitalize()
      if Periodo in ListaPeriodo:
        break
      else:
          print("Valor invalo.")

   while True:
      print ("ID de grupos ".center(30,"*"))
      for i in Asignatura.keys():
          print(i)
      print ("".center(30,"*"))
      print ("\n")
      IdGrupo=input("ID-Grupo..: ").upper()
      if IdGrupo in Asignatura.keys():
         break
      else:
         print("El ID del grupo no se encuentra en la base de datos. ")
   while True:
      dia= input("Dia..:")
      print("Sistema horario de 24 horas")
      Hora=int(input("Hora incial:"))
      Hora2=int(input("Hora final:"))      
      secuencia= input("Se repite la clase en la semana Si/No:").capitalize()
      if secuencia =="No":
          break
      else:
         dia2= input("Dia..:")
         print("Sistema horario de 24 horas")
         SecuenciaHora=int(input("Hora incial:"))
         SecuenciaHora2=int(input("Hora final:"))
         break

   while True:
      print(f"Aulas disponibles:\n{AulasDisponbibles} ")    
      aula=input("Digite el aula: ").capitalize()
      if aula in AulasDisponbibles:
            break
      else:
        print("El Aula insertada no se encuentra en nuestra Universidad")

   DatosProcesos.append([IdDocente,IdGrupo,Periodo,dia,Hora,Hora2,aula])  
   return Menu()

#Consultar Datos principales
def ConsultarDatosPrincipales():   #Datos principales del docente consultar
  print ("\n")
  print ("Consulta de datos principales del docente ".center(100,"="))
  print ("ID-Docente \tNombre \t\tSexo \t\tEdad \t\tEspecialidad \t\tArea")
  print (100*"=")
  for i in DatosPrincipales:
    print (i[0],i[1],i[2],i[3],i[4],i[5], sep="\t\t")
  print ("\n \n") 
  return Menu()
#Consultar datos secundarios
def ConsultarDatosSecundarios():
  print ("\n")
  print ("Consulta de datos secunadarios del docente ".center(100,"="))
  print ("ID-Grupo \tAsignatura \t\tDia \t\t\tHora")
  print (100*"=") 
  for i in DatosSecundarios:
      print(i[0],"\t\t",i[1],"\t\t",i[2],"\t\t",i[3],("-"),i[4])
  return Menu()
def ConsultarDatosDeRelacion():
  print ("\n")
  print ("Consulta de datos por relacion ".center(100,"="))
  print ("ID-Docente \tID-Grupo \tPeriodo \tDia \t\tHora \t\tAula ")
  print (100*"=")
  for i in DatosProcesos:
    print (i[0],"\t\t",i[1],"\t",i[2],"\t\t",i[3],"\t",i[4]+ "-" +i[5],"\t\t",i[6] )
  print ("\n \n") 
  return Menu()
def Menu():
   print (40* "=")
   #centraliza el texto de 40 espacios
   print ("Universidad catolica del Cibao".center(40," ")) 
   print ("Ucateci".center(40," "))
   print ("Programacion 1".center(40," "))
   print ("Segundo Parcial".center(40," "))
   print("Carga Horaria Docente".center(40," "))
   print("Menú Principal".center(40," "))
   print ("Fecha: "+time.strftime("%d/%m/%y"))
   print (40* "=")

   print ("1- Información del grupo")
   print ("2- Registrar datos principales")
   print ("3- Registrar datos secundarios")
   print ("4- Registrar proceso")
   print ("5- Consultar datos principales")
   print ("6- Consultar datos secundarios")
   print ("7- Consultar por relación")
   print ("0- Salir")
   opcion = int(input("Su opcion: "))
   while True:
      if(opcion==1):
        Info()
      elif(opcion==2):
        RegistrarDatosPrincipales()
      elif(opcion==3):
        RegistrarDatosSecundarios()     
      elif(opcion==4):
        RegistrarProceso()
      elif(opcion==5):
        ConsultarDatosPrincipales()
      elif(opcion==6):
         ConsultarDatosSecundarios()
      elif(opcion==7):
          ConsultarDatosDeRelacion()
      elif(opcion==0):
          print ("Gracias, vuelva pronto")
          break
      else:
         print ("Opción no válida")
         opcion = int(input("Elija una opcion: "))

login()