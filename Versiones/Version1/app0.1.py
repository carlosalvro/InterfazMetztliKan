import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.H3 import H3
from dash_html_components.H4 import H4
import numpy as np
import plotly.express as px
import os 
import cv2

######FUNCIONES##########
def plot_figure(file, min, max):
  img = cv2.imread(file)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  range1 = np.array(min, np.uint8)
  range2 = np.array(max, np.uint8)

  imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  ##Aplicamos la mascara
  mask = cv2.inRange(imgHSV, range1, range2)
  segmentation = cv2.bitwise_and(img, img, mask = mask)
  
  fig = px.imshow(segmentation)
  return fig


def mask_HSV(imgRGB, min, max):
  range1 = np.array(min, np.uint8)
  range2 = np.array(max, np.uint8)

  imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)

  ##Aplicamos la mascara
  mask = cv2.inRange(imgHSV, range1, range2)
  segmentation = cv2.bitwise_and(imgRGB, imgRGB, mask = mask)

  return segmentation



PATH_IMGS = r'../../Imagenes/'
IMGS = os.listdir(PATH_IMGS)
IMGS_PATH = [os.path.join(PATH_IMGS,i) for i in IMGS ]
min_defa = [0,0,0]
max_defa = [180,255,255]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
  children=[
    html.Div(
      html.H1('SpaceSat',
      style={'padding':'2% 4%',
      'background-color':'#589bc4'})
      ),
    html.Div(children=[
      html.Div(id = 'row1', children=[
      html.Div(
        id='imagenes',
        children=[
          dcc.Graph(
            id = 'image',
            figure= plot_figure(IMGS_PATH[0], min_defa, max_defa)
          )
        ]),
      html.Div( 
        id='Buttons',
        style = {'margin':'0 26%',
        'display':'flex',
        'justify-content':'center'},
        children=[
          html.Button(
            'Atras',
            id='boton-atras',
            n_clicks=0,
            n_clicks_timestamp=-1
          ),
          html.Button(
            'Adelante',
            id='boton-adelante',
            n_clicks=0,
            n_clicks_timestamp=-1
          )
        ])
        ],
        className='seven columns'
      ),
      html.Div(
        id = 'controladores',
        style={'margin':'2% 0'},
        children=[
          html.Div([
            html.H3('Hue'),
            dcc.RangeSlider(
              id='H-slider',
              min = 0,
              max = 180,
              step=1,
              marks = {0:'0',180:'180'},
              value=[33,85],
              allowCross=False,
              updatemode='drag'
            ),
            html.H3('Saturation'),
            dcc.RangeSlider(
              id='S-slider',
              min = 0,
              max = 255,
              step=1,
              marks = {0:'0',255:'255'},
              value=[58,255],
              allowCross=False,
              updatemode='drag'
            ),
            html.H3('Value'),
            dcc.RangeSlider(
              id='V-slider',
              min = 0,
              max = 255,
              step=1,
              marks = {0:'0',255:'255'},
              value=[0,255],
              allowCross=False,
              updatemode='drag'
            )
          ])
        ],
        className='five columns'
      )
    ]
    ),
    dcc.Store(id='intermediate-boton-image', storage_type='memory')
  ])


@app.callback(
  dash.dependencies.Output('imagenes', 'children'),
  [dash.dependencies.Input('boton-adelante','n_clicks'),
  dash.dependencies.Input('boton-atras','n_clicks'),
  dash.dependencies.Input('H-slider','value'),
  dash.dependencies.Input('S-slider','value'),
  dash.dependencies.Input('V-slider','value')]
)
def prueba(adelante, atras, H,S,V):
  image_number = adelante - atras
  min = [H[0], S[0], V[0]]
  max = [H[1], S[1], V[1]]
  return [dcc.Graph(
            id = 'image',
            figure= plot_figure(IMGS_PATH[image_number], min, max)
          ),
        html.P(f'H: {H}, S: {S}, V: {V}', 
        style = {'margin':'0 26%',
        'display':'flex',
        'justify-content':'center'})]


if __name__ == '__main__':
  app.run_server(debug=True)