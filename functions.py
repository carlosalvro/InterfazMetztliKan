import plotly.express as px
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import cv2
import os 
import plotly.express as px
import serial
import json





###   FUNCIONES PARA LAS METRICAS ##############
################################################

## Grafica de lineas acelerometro y giroscopio
def plot_graphs_ace_giro():
  x = [i for i in range(1,51)]
  y1 = np.random.randint(-100,100,50)
  y2 = np.random.randint(-100,100,50)
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


def open_serial():
  ser = serial.Serial('/dev/pts/5')
  decode_data = ser.readline().decode('utf-8')
  dic = json.loads(decode_data)
  output = [
    dic['Al'],
    dic['Al'],
    dic['La'],
    dic['Lo'],
    dic['Te'],
    dic['Pr'],
    dic['Hu'],
    dic['Ax'],
    dic['Ay'],
    dic['Az'],
    dic['Gx'],
    dic['Gy'],
    dic['Gz'],
  ]
  return output