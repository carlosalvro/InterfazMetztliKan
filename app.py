import dash
import dash_core_components as dcc
import dash_html_components as html
import os
import functions

### UBICAMOS LA CARPETA DE IMAGENES PARA LLAMARLAS ###############
PATH_IMGS = r'../Imagenes'
IMGS = os.listdir(PATH_IMGS)
IMGS_PATH = [os.path.join(PATH_IMGS,i) for i in IMGS ]
### DEFINIMOS LOS LIMOTES DE HSV respectivamente ##################3
min_default = [0,0,0]
max_default = [180,255,255]

##### INICIAMOS LA APP #####
app = dash.Dash(__name__)

##### AQUI VA TODA LA ESTRUCTURA DE NUESTRA PAGINA 
app.layout= html.Div(
  #CONTENEDOR PRINCIPAL
  className="main-container",
  children=[
    # CABEZERA DONDE VA EL LOGO
    html.Div(
      className='header', children=[
        html.Img(src='./assets/Images/Kan-Horizontal.png', className='logo')
      ]
    ),
    # aqui va todo lo demás
    html.Section(
      className='main',
      children=[
        # iniciamos componente de los tabs (las pestañas para cambiar de métrica a imagen)
        dcc.Tabs(className='main-tabs',
                #  vertical=True,
                  value='tab-metrica',children=[
          # iniciamos el primer tab de metrica
          dcc.Tab(id='tab-metrica',
                  className='custom-tab',
                  selected_className='custom-tab--selected', 
                  label='Métrica', 
                  value='tab-metrica', children=[
                    ###Contenido del primer tab

####Este componente interval es muy importante, es el que nos da el tiempo de actualización de la página                    
                    #ES SU UNÍCO PROPOSITO (ES INVISIBLE, NO SE MOSTRARÁ NADA EN LA PÁGINA)
                    dcc.Interval(
                        id='interval-component',
                        interval=500, # milisegundos
                        n_intervals=0
                    ),
                    # aqui comienza el contenedor de metricas
                    # IMAGEN
                    html.Div(
                      className='tab-section',
                      children=[
                        #TITULO
                        html.H2('Métrica'),
                        #CONTENEDOR PRINCIPAL
                        html.Div(
                          className='principal-metrica',
                          children=[
                            #CONTENEDOR GRÁFICA
                            html.Div(
                              className="card-1 altitud",
                              children = [
                                html.H4("Altitud"),
                                html.H3(id='altitud', children="120"),
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
                                    html.H3(id='latitud', children="128.5"),
                                    html.H3(id='longitud', children="-103.9")
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
                                html.H3(id='temperatura', children="30"),
                                html.P("°C")
                              ]
                            ),
                            html.Div(
                              className="card-1 presión",
                              children = [
                                html.H4("Presión"),
                                html.H3(id ='presion', children="2"),
                                html.P("Pa")
                              ]
                            ),
                            html.Div(
                              className="card-1 humedad",
                              children = [
                                html.H4("Humedad"),
                                html.H3(id='humedad', children="3"),
                              ]
                            ),
                            html.Div(
                              className=("card-3 acelerometro"),
                              children = [
                                html.H4("Acelerometro"),
                                html.Div(
                                  className="subcard-3 values-3",
                                  children = [
                                    html.H3(id ='aceleX', children="128.5"),
                                    html.H3(id ='aceleY', children="-103.9"),
                                    html.H3(id ='aceleZ', children="150.0")
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
                                    html.H3(id ='giroX', children="128.5"),
                                    html.H3(id ='giroY', children="-103.9"),
                                    html.H3(id ='giroZ', children="150.0")
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

@app.callback(
  dash.dependencies.Output('altitud', 'children'),
  dash.dependencies.Output('latitud', 'children'),
  dash.dependencies.Output('longitud', 'children'),
  dash.dependencies.Output('temperatura', 'children'),
  dash.dependencies.Output('presion', 'children'),
  dash.dependencies.Output('humedad', 'children'),
  dash.dependencies.Output('aceleX', 'children'),
  dash.dependencies.Output('aceleY', 'children'),
  dash.dependencies.Output('aceleZ', 'children'),
  dash.dependencies.Output('giroX', 'children'),
  dash.dependencies.Output('giroY', 'children'),
  dash.dependencies.Output('giroZ', 'children'),
  [dash.dependencies.Input('interval-component', 'n_intervals')] 
)
def data_listener(n):
  output = functions.open_serial()
  al = output[0]
  la = output[1]
  lo = output[2]
  te = output[3]
  pr = output[4]
  hu = output[5]
  ax = output[6]
  ay = output[7]
  az = output[8]
  gx = output[9]
  gy = output[10]
  gz = output[11]
  return al, la, lo, te, pr, hu, ax, ay, az, gx, gy, gz


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
def image_controler(adelante, atras, H, S, V, gauss, median, reset):
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