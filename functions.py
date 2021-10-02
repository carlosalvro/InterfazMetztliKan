import plotly.express as px
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import cv2
import plotly.express as px
import serial
import json
import re
from datetime import date, datetime, timedelta
import time




###   FUNCIONES PARA LAS METRICAS ##############
################################################

## Grafica de lineas acelerometro y giroscopio
def plot_graphs_ace_giro(dic = None):
  if dic == None: #Si no se recibe nada que la gráficas muestren 0
    x = [0]
    y1 = [0]
    y2 = [0]
  else:
    y1 = dic['A']
    y2 = dic['G']
    x = [i for i in range(len(y1))] 

  fig = make_subplots(rows=2, cols=1)

  fig.append_trace(go.Scatter(x=x, y=y1, line=dict(color='#F24333')), row=1, col=1)
  fig.append_trace(go.Scatter(x=x, y=y2, line=dict(color='#F7B32B')), row=2, col=1)


  fig.update_layout(width=550, 
                    height=330, 
                    showlegend=False, 
                    margin=dict(l=20, r=20, t=20, b=20),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font_color="white")
  # fig.update_layout(title_text='Acelerometro', title_x=0.5, title_font_size=20)
  fig.update_yaxes(title_text="Acelerometro", row=1, col=1)
  fig.update_yaxes(title_text="Giroscopio", row=2, col=1)
  return fig

## Función para crear las meshgrids del cilindro
## Dado el radio r, la altura h, y la cordenada de la base a
def cylinder(r,h, a = 0, nt = 100, nv = 50):
  theta = np.linspace(0, 2*np.pi, nt)
  v = np.linspace(a, a+h, nv)
  theta, v = np.meshgrid(theta,v)
  x = r*np.cos(theta)
  y = r*np.sin(theta)
  z = v
  return x,y,z

## Grafica para plotear el cilindro "Cansat"
def plot_cansat():
  r=2
  a= -2.5
  h=5
  x,y,z = cylinder(r,h,a)
  colorscale = [[0,'blue'], [1,'blue']]

  X = go.Scatter3d(x=[0,3],y=[0,0], z=[0,0],
                    showlegend=False,
                    mode  ='lines',
                    line = dict(color = 'black', width=2))
  Y = go.Scatter3d(x=[0,0],y=[0,3], z=[0,0],
                    showlegend=False,
                    mode  ='lines',
                    line = dict(color = 'black', width=2))
  Z = go.Scatter3d(x=[0,0],y=[0,0], z=[0,3],
                    showlegend=False,
                    mode  ='lines',
                    line = dict(color = 'black', width=2))
  cyl = go.Surface(x = x, y = y, z = z,
                  opacity = 0.5,
                  colorscale=colorscale,
                  showscale=False)

  fig = go.Figure(data = [cyl,Z,X,Y])
  fig.update_scenes(xaxis_range=[-5,5],
                    yaxis_range=[-5,5],
                    zaxis_range=[-2.5, 2.5])
  fig.update_layout(width=550, 
                    height=330, 
                    showlegend=False, 
                    margin=dict(l=20, r=20, t=20, b=20),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font_color="white")
  return fig



###   FUNCIONES PARA LAS IMAGENES ##############
################################################

## Función para cargar la imagen desde el directorio,
## ya con sus valores por defecto de HSV
## min y max deben de ser listas de 3 valores 
## HSV respectivamente para poner los limites.
## Los valores minimos son 0 
## Los valores maximos son [180, 255, 255]
def plot_image(file, min, max):
  try:
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  except:
    img = file

  range1 = np.array(min, np.uint8)
  range2 = np.array(max, np.uint8)

  imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  ##Aplicamos la mascara
  mask = cv2.inRange(imgHSV, range1, range2)
  segmentacion = cv2.bitwise_and(img, img, mask=mask)
  fig = px.imshow(segmentacion)
  fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=20, r=20, t=20, b=5)
  )
  fig.update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)
  return fig


def median_blur(file):
  try:
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  except:
    img = file

  filtro = cv2.medianBlur(img, 3)
  return filtro  

def gaussian_blur(file):
  try:
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  except:
    img = file

  filtro = cv2.GaussianBlur(img, (5,5),cv2.BORDER_DEFAULT)
  return filtro  




# def serial_cleaner():
#   ### ESTA FUNCIÓN CONVIERTE LO QUE RECIBE DEL PUERTO SERIAL 
#   ### A UN DICCIONARIO EN PYTHON 
#   ### SE ESPERA QUE DEL PUERTO SE RECIBA ALGO ASI 
#   ### ["Al":"201", "La":"119", "Lo":"72", "Te":"15", "Pr":"2", "Hu":"2","Ax":"-2","Ay":"319","Az":"219","Gx":"-136","Gy":"105","Gz":"-349"]
#   ### NO IMPORTA EL ORDEN SOLO LA ESTRUCTURA
#   prueba = """["Al":"201", "La":"119", "Lo":"72", "Te":"15", "Pr":"2", "Hu":"2","Ax":"-2","Ay":"319","Az":"219","Gx":"-136","Gy":"105","Gz":"-349"]"""
#   pattern = r"[\[\{](.+)[\]\}]"
#   return re.match(pattern, prueba).group(1)


def open_serial(port):
  complete_port = '/dev/pts/'+ str(port) 
  ser = serial.Serial(complete_port, baudrate=115200) 
  decode_data = ser.readline().decode('utf-8')

  cadena = re.match(r'(\{.+\})', decode_data)

  if cadena != None:
    try:
      output = json.loads(cadena.group(1))  
      return output  
    except Exception as e :
      print(e)
      print(cadena.group(1))
      print('---------------')
  else:
    return None
    

def random_generator():
  al = str(np.random.randint(0,401))
  la = str(np.random.randint(0,401))
  lo = str(np.random.randint(0,401))
  te = str(np.random.randint(0,41))
  pr = str(np.random.randint(0,3))
  hu = str(np.random.randint(0,3))
  ax = str(np.random.randint(-400,401))
  ay = str(np.random.randint(-400,401))
  az = str(np.random.randint(-400,401))
  gx = str(np.random.randint(-400,401))
  gy = str(np.random.randint(-400,401))
  gz = str(np.random.randint(-400,401))
  ve = str(np.random.randint(0,41))
  bat = np.random.randint(1,101)

  dic = {'Al':al,'La':la,'Lo':lo,'Te':te,'Pr':pr,'Hu':hu,'Ax':ax,'Ay':ay,'Az':az,'Gx':gx,'Gy':gy,'Gz':gz, 'Ve':ve, 'Bat':bat}
  return dic
#Obtiene la fecha de hoy en el formato determinado
def today_date():
  today = date.today()
  return today.strftime("%d/%m/%Y")

#Obtiene la hora actual en el formato determinado
def current_time():
  now = datetime.now()
  return now.strftime("%H:%M")


# Le saca la norma a los vectores aceleración y giroscopio
def graphs_values(output):
  ax = float(output['Ax'])
  ay = float(output['Ay'])
  az = float(output['Az'])
  gx = float(output['Gx'])
  gy = float(output['Gy'])
  gz = float(output['Gz'])

  g = np.linalg.norm(np.array([gx,gy,gz]))
  a = np.linalg.norm(np.array([ax,ay,az]))
  return g,a

#Contador tipo cronometro para contar el tiempo de misión transcurrido
def get_time_mision(starter_time):
  now_time = time.time()
  secs = int(now_time - starter_time)
  sec2time = timedelta(seconds=secs)
  timer = (datetime.min  + sec2time).time()
  timer = timer.strftime("%M:%S")
  return timer
