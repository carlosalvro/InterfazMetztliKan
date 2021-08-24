# Codigo de jesus
def CORTAR_JSON(cadena):
  """
  Toma una cadena string y busca y corta fracciones de mensaje JSON
  Retorna:
    Cadena Extraida
    Bandera mensaje exitoso (1) o cadena basura (0)
	Resto de la cadena tomada
  """
  cadenaNueva = ''
  cadenaExtraida = ''
  mensajeExitoso = 0

  punto1 = cadena.find('{',0,len(cadena))
  punto2 = cadena.find('}',0,len(cadena))

  if(punto2 < punto1):
    mensajeExitoso = 0 #Trama Incompleta
    cadenaExtraida = cadena[0:punto2+1]
    cadenaNueva = cadena[punto1::]
  
  if(punto2 > punto1):
    mensajeExitoso = 1 #Trama Completa
    cadenaExtraida = cadena[punto1:punto2+1]
    cadenaNueva = cadena[punto2+1::]
  
  return cadenaExtraida, mensajeExitoso, cadenaNueva

#-------------------------------------------------------------------

def REVISAR_JSON(cadena):
  """
  Detecta si hay errores en una cadena JSON.
  Retorna una lista con valores 0 (error) o 1 (correcto). Posiciones:
  [0] -- Numero minimo de caracteres
  [1] -- Numero minimo de (:)
  [2] -- Numero minimo de (")
  [3] -- Relacion (:-,)
  [4] -- Relacion ("-:)
  """
  longitudCadena=len(cadena)
  numDosPuntos=cadena.count(':',0,len(cadena))
  numComas=cadena.count(',',0,len(cadena))
  numComillasDobles=cadena.count('"',0,len(cadena))
  listaErrores = []
  error = 0
  
  #[0] -- Numero minimo de caracteres
  if((longitudCadena)>=(9)):
    listaErrores.append(1)
  else:
    listaErrores.append(0)
  #[1] -- Numero minimo de (:)
  if((numDosPuntos)>=(1)):
    listaErrores.append(1)
  else:
    listaErrores.append(0)
  #[2] -- Numero minimo de (")
  if((numComillasDobles)>=(4)):
    listaErrores.append(1)
  else:
    listaErrores.append(0)
  #[3] -- Relacion (:-,)
  if((numDosPuntos-1)==(numComas)):
    listaErrores.append(1)
  else:
    listaErrores.append(0)
  #[4] -- Relacion ("-:)
  if((numComillasDobles)==(numDosPuntos*4)):
    listaErrores.append(1)
  else:
    listaErrores.append(0)

  if (listaErrores.count(1)==5):
    error = 1

  return(error)
  #No detecta valores vacios

#-------------------------------------------------------------------

def SEPARAR_MENSAJE_JSON(cadena):
  mensajeNombres = []
  mensajeValores = []
  indices = []

  numeroComillasDobles = cadena.count('"',0,len(cadena))

  indices.append(cadena.find('"', 0, len(cadena)))
  for i in range(1,numeroComillasDobles):
    indices.append(cadena.find('"', indices[len(indices)-1]+1, len(cadena)))

  for i in range(int(numeroComillasDobles/4)):
    mensajeNombres.append(cadena[indices[(i*4)+0]+1:indices[(i*4)+1]])
    mensajeValores.append(cadena[indices[(i*4)+2]+1:indices[(i*4)+3]])

  return mensajeNombres, mensajeValores

#-------------------------------------------------------------------



