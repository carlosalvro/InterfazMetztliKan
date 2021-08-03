import dash
import dash_core_components as dcc
from dash_core_components.Graph import Graph
import dash_html_components as html
from dash_html_components.Div import Div
from dash_html_components.H3 import H3
from dash_html_components.H4 import H4
from dash_html_components.I import I
from dash_html_components.Section import Section
import numpy as np
import cv2
from numpy.lib.type_check import imag
import plotly.express as px
import os
import functions

PATH_IMGS = r'../Imagenes'
IMGS = os.listdir(PATH_IMGS)
IMGS_PATH = [os.path.join(PATH_IMGS,i) for i in IMGS ]
min_default = [0,0,0]
max_default = [180,255,255]


app = dash.Dash(__name__)


app.layout= html.Div(
  className="main-container",
  children=[
    html.Div(
      className='header', children=[
        html.Img(src='./assets/Images/Logo-Horizontal-SpaceSat.png', className='logo')
      ]
    ),
    html.Section(
      className='main',
      children=[
        dcc.Tabs(className='main-tabs',
                #  vertical=True,
                 value='tab-metrica',children=[
          ###Aqui comienzan los tabs
          dcc.Tab(id='tab-metrica',
                  className='custom-tab',
                  selected_className='custom-tab--selected', 
                  label='Métrica', 
                  value='tab-metrica', children=[
                    ###Contenido del primer tab


                    html.Div(
                      className='tab-section',
                      children=[
                        html.H2('Métrica'),
                        html.Div(
                          className='principal-metrica',
                          children=[
                            html.Div(
                              className="card-1 altitud",
                              children = [
                                html.H4("Altitud"),
                                html.H3("120"),
                                html.P("metros")
                              ]
                            ),
                            html.Div(
                              className=("card-2 coordenadas"),
                              children = [
                                html.H4("Coordenadas"),
                                html.Div(
                                  className="subcard-2 values-2",
                                  children = [
                                    html.H3("128.5"),
                                    html.H3("-103.9")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard-2 uds",
                                  children = [
                                    html.P("Latitud"),
                                    html.P("Longitud")
                                  ]
                                )
                              ]
                            ),
                            html.Div(
                              className="card-1 temperatura",
                              children = [
                                html.H4("Temperatura"),
                                html.H3("30"),
                                html.P("°C")
                              ]
                            ),
                            html.Div(
                              className="card-1 presión",
                              children = [
                                html.H4("Presión"),
                                html.H3("2"),
                                html.P("Pa")
                              ]
                            ),
                            html.Div(
                              className="card-1 humedad",
                              children = [
                                html.H4("Humedad"),
                                html.H3("3"),
                              ]
                            ),
                            html.Div(
                              className=("card-3 acelerometro"),
                              children = [
                                html.H4("Acelerometro"),
                                html.Div(
                                  className="subcard-3 values-3",
                                  children = [
                                    html.H3("128.5"),
                                    html.H3("-103.9"),
                                    html.H3("150.0")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard-3 uds",
                                  children = [
                                    html.P("Eje X"),
                                    html.P("Eje Y"),
                                    html.P("Eje Z")
                                  ]
                                )
                              ]
                            ),
                            html.Div(
                              className=("card-3 giroscopio"),
                              children = [
                                html.H4("Giroscopio"),
                                html.Div(
                                  className="subcard-3 values-3",
                                  children = [
                                    html.H3("128.5"),
                                    html.H3("-103.9"),
                                    html.H3("150.0")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard-3 uds",
                                  children = [
                                    html.P("Eje X"),
                                    html.P("Eje Y"),
                                    html.P("Eje Z")
                                  ]
                                )
                              ]
                            ),
                            html.Div(
                              className="card-1 velocidad",
                              children = [
                                html.H4("Velocidad"),
                                html.H3("30"),
                                html.P("m/s")
                              ]
                            ),
                            html.Div(
                              className="card-1 fecha",
                              children = [
                                html.H4("Fecha"),
                                html.H4("Bateria"),
                              ]
                            ),
                            html.Div(
                              className="card-graph",
                              children= [
                                dcc.Tabs(
                                  className="tabs-subgraph",
                                  value="ac-gi-graph",
                                  children = [
                                    dcc.Tab( id="ac-gi-graph",
                                      className="custom-subtab",
                                      selected_className='custom-subtab--selected',
                                      label="Graficas",
                                      value="ac-gi-graph",
                                      children=[
                                        html.Div(
                                          className="graph-ace-giro-container",
                                          children=[
                                            dcc.Graph(
                                              figure=functions.plot_graphs_ace_giro()
                                            )
                                          ]
                                        )
                                      ]
                                    ),
                                    dcc.Tab(id="cansat-graph",
                                      className="custom-subtab",
                                      selected_className='custom-subtab--selected',
                                      label="Cansat",
                                      value="cansat-graph",
                                      children=[
                                          html.Div(
                                          className="graph-cansat-container",
                                          children=[
                                            dcc.Graph(
                                              figure=functions.plot_cansat()
                                            )
                                          ]
                                        )
                                      ]
                                    )
                                  ]
                                )
                              ]
                            )
                          ]
                        )
                      ]
                    )
                  ]),
          dcc.Tab(id='tab-image',
                  className='custom-tab', 
                  selected_className='custom-tab--selected',
                  label='Imagen', 
                  value='tab-image', children=[
                    ###Contenido del segundo tab
                   
                    html.Div(
                      className='tab-section',
                      children=[
                        html.H2('Imagen'),
                        html.Div(
                          className='principal-image',
                          children=[
                            html.Div(
                              className='graph-container',
                              children=[
                                html.Div(
                                  className= "image-container",
                                  id= "imagen-cansat",
                                  children = [
                                    dcc.Graph(
                                    className='graph',
                                    figure=functions.plot_image(IMGS_PATH[1], min_default, max_default)
                                    ),
                                  ]
                                ),
                                html.Div(
                                  className='graph-buttons',
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
                                  ]
                                )
                              ]
                            ),
                            html.Div(
                              className="controls-container",
                              children=[
                                html.Div(className='sliders', children=[
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
                                ]),
                                html.H3("Desenfoques"),
                                html.Div(className ='blur-buttons', 
                                  children=[
                                    html.Button(
                                      'Gaussiano',
                                      id='gauss',
                                      n_clicks=0,
                                      n_clicks_timestamp=-1
                                    ), 
                                    html.Button(
                                      'Median',
                                      id = 'median',
                                      n_clicks=0,
                                      n_clicks_timestamp=-1
                                    )
                                ]),
                                html.Button(
                                    'Reset',
                                    id='reset',
                                    n_clicks=0,
                                    n_clicks_timestamp=-1
                                )
                              ]          
                            )
                          ]
                        )
                      ]
                    )
                  ])
        ])
      ]
    )
  ]
)

gau = 0
med = 0
res = 0

@app.callback(
  dash.dependencies.Output("imagen-cansat", "children"),
  [dash.dependencies.Input('boton-adelante','n_clicks'),
  dash.dependencies.Input('boton-atras','n_clicks'),
  dash.dependencies.Input('H-slider','value'),
  dash.dependencies.Input('S-slider','value'),
  dash.dependencies.Input('V-slider','value'),
  dash.dependencies.Input('gauss','n_clicks'),
  dash.dependencies.Input('median','n_clicks'),
  dash.dependencies.Input('reset','n_clicks')]
)
def prueba(adelante, atras, H, S, V, gauss, median, reset):
  global gau, med, res

  image_number = adelante - atras
  image = IMGS_PATH[image_number]
  min = [H[0], S[0], V[0]]
  max = [H[1], S[1], V[1]]

  if gauss!=gau:
    image = functions.gaussian_blur(image)
    print("Apply 1 time gauss")
    gau = gauss
  else:
    pass

  if median!=med:
    image = functions.median_blur(image)
    print("Apply 1 time median")
    med =median

  if reset!= res:
    image = IMGS_PATH[image_number]
    res = reset
  else:
    pass
  
  return [dcc.Graph(
            className='graph',
            figure= functions.plot_image(image, min, max)
          ),
        html.P(f'H: {H}  S: {S}  V: {V}')]


if __name__=='__main__':
  app.run_server(debug=True)