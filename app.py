import dash
import dash_core_components as dcc
import dash_html_components as html
import os
import numpy as np

import functions
import time

PATH_IMGS = r'./Imagenes'
IMGS = os.listdir(PATH_IMGS)
IMGS_PATH = [os.path.join(PATH_IMGS,i) for i in IMGS ]
### DEFINIMOS LOS LIMITES DE HSV respectivamente ##################3
min_default = [0,0,0]
max_default = [180,255,255]

##### INICIAMOS LA APP #####
app = dash.Dash(__name__)

##### AQUI VA TODA LA ESTRUCTURA DE NUESTRA PAGINA 
app.layout= html.Div(
  #CONTENEDOR PRINCIPAL
  className="main-container",
  children=[
    html.P(id="hidden-p", style={'display': 'none'}),
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
                    html.Div(
                      className='tab-section',
                      children=[
                        #TITULO
                        html.H2('Métrica'),
                        #CONTENEDOR PRINCIPAL
                        html.Div(
                          className='principal-metrica',
                          children=[
                            #Botones
                            html.Div(
                              className="buttons",
                              children = [
                                html.Button('Iniciar', className='start-button', id='start-button'),
                                html.Button('Detener', className='stop-button', id='stop-button')
                              ]
                            ),
                            # tiempo de mision
                            html.Div(
                              className="card time",
                              children = [
                                html.H4("Tiempo de Misión"),
                                html.H3(id='mision-time' ,children="00:00"),
                              ]
                            ),
                            # Sección ALTITUD
                            html.Div(
                              className="card altitud",
                              children = [
                                html.H4("Altitud"),
                                html.H3(id='altitud', children="0"),
                                html.P("metros")
                              ]
                            ),
                            # Sección COORDENADAS
                            html.Div(
                              className=("v-card coordenadas"),
                              children = [
                                html.H4("Coordenadas"),
                                html.Div(
                                  className="v-subcard",
                                  children = [
                                    html.H3(id='longitud', children="0"),
                                    html.P("Longitud")
                                  ]
                                ),
                                html.Div(
                                  className= "v-subcard",
                                  children = [
                                    html.H3(id='latitud', children="0"),
                                    html.P("Latitud")
                                  ]
                                )
                              ]
                            ),
                            # Sección TEMPERATURA
                            html.Div(
                              className="card temperatura",
                              children = [
                                html.H4("Temperatura"),
                                html.H3(id='temperatura', children="0"),
                                html.P("°C")
                              ]
                            ),
                            # Sección PRESION
                            html.Div(
                              className="card presión",
                              children = [
                                html.H4("Presión"),
                                html.H3(id ='presion', children="0"),
                                html.P("Pa")
                              ]
                            ),
                            # Sección HUMEDAD
                            html.Div(
                              className="card humedad",
                              children = [
                                html.H4("Humedad"),
                                html.H3(id='humedad', children="0"),
                              ]
                            ),
                            # Sección ACELEROMETRO
                            html.Div(
                              className=("card acelerometro"),
                              children = [
                                html.H4("Acelerometro"),
                                html.Div(
                                  className="subcard",
                                  children = [
                                    html.H3(id ='aceleX', children="0"),
                                    html.H3(id ='aceleY', children="0"),
                                    html.H3(id ='aceleZ', children="0")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard",
                                  children = [
                                    html.P("Eje X"),
                                    html.P("Eje Y"),
                                    html.P("Eje Z")
                                  ]
                                )
                              ]
                            ),
                            # Sección GIROSCOPIO
                            html.Div(
                              className=("card giroscopio"),
                              children = [
                                html.H4("Giroscopio"),
                                html.Div(
                                  className="subcard",
                                  children = [
                                    html.H3(id ='giroX', children="0"),
                                    html.H3(id ='giroY', children="0"),
                                    html.H3(id ='giroZ', children="0")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard",
                                  children = [
                                    html.P("Eje X"),
                                    html.P("Eje Y"),
                                    html.P("Eje Z")
                                  ]
                                )
                              ]
                            ),
                            # Sección VELOCIDAD
                            html.Div(
                              className="card velocidad",
                              children = [
                                html.H4("Velocidad"),
                                html.H3(id = "velocidad", children="0"),
                                html.P("m/s")
                              ]
                            ),
                            # Sección FECHA
                            html.Div(
                              className="fecha-bat",
                              children = [
                                # Aca va la pila
                                html.Section(
                                  className="pila",
                                  children= [
                                    html.Div(className="pila-head"), 
                                    html.Div(
                                      className="pila-body", 
                                      children= [
                                        html.Div(
                                          className="pila-fondo",
                                          id="pila-porcentaje",
                                          children=[
                                            html.Div(
                                              className="pila-pila",
                                            ),
                                            html.H5(id="battery-percent", children=["100%"])
                                          ]
                                        )
                                      ]
                                    )
                                  ]
                                ),
                                # Aca va la fecha
                                html.Section(
                                  className="card fecha", 
                                  children = [
                                    html.H4(id="date", children="20-08-2021"),
                                    html.H4(id="hour", children="17:43"),
                                  ]
                                ),
                              ]
                            ),
                            # Sección GRAFICA
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
                                              id='acel-gyro-graph',
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
          #contenido del segundo tab de imagen 
          dcc.Tab(id='tab-image',
                  className='custom-tab', 
                  selected_className='custom-tab--selected',
                  label='Imagen', 
                  value='tab-image', children=[
                    ###Contenido del segundo tab
                    ## IMAGEN
                    html.Div(
                      className='tab-section',
                      children=[
                        # TITULO
                        html.H2('Imagen'),
                        # CONTENEDOR PRINCIPAL
                        html.Div(
                          className='principal-image',
                          children=[
                            #CONTENEDOR GRAFICA
                            html.Div(
                              className='graph-container',
                              children=[
                                # GRAFICA
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
                                # CONTENEDOR BOTONES GRAFICA
                                html.Div(
                                  className='graph-buttons',
                                  children=[
                                    # BOTON ATRAS
                                    html.Button(
                                      'Atras',
                                      id='boton-atras',
                                      n_clicks=0,
                                      n_clicks_timestamp=-1
                                    ),
                                    # BOTON ADELANTE
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
                            # CONTENEDOR CONTROLADORES
                            html.Div(
                              className="controls-container",
                              children=[
                                #SLIDERS
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
                                # BLURS
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
                                # RESET BUTTON
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

active = False
dic = {"A":[], "G": []}
#Esta función nos da la orden para empezar a recibir datos
@app.callback(
  dash.dependencies.Output('hidden-p', 'children'),
  [dash.dependencies.Input('start-button', 'n_clicks'),
  dash.dependencies.Input('stop-button', 'n_clicks')]
)
def mision_starter_stopper(start, stop):
  global active, dic, time_starter
  
  ctx = dash.callback_context

  if not ctx.triggered:
    raise dash.exceptions.PreventUpdate
  else:
    clicked_button = ctx.triggered[0]['prop_id'].split('.')[0] .split('-')[0]
  
  if clicked_button=="start":
    print("Se presiono start")
    if active == False:
      time_starter = time.time()
      dic = {"A":[], "G": []}
      active = True
    else:
      raise dash.exceptions.PreventUpdate

  elif clicked_button=="stop":
    print("Se presiono stop")
    if active == True:
      active = False
    else: 
      raise dash.exceptions.PreventUpdate
  return None

## ESTA ES LA FUNCIÓN QUE ACTUALIZA LOS VALORES
## RECIBE AL CONTADOR LLAMADO INTERVAL DE LA LINEA 47
## EL CONTADOR LE DA LA SEÑAL PARA QUE LOS OUTPUTS SE REFRESQUEN
## EL INTERVAL TIENE UN TIEMPO DE ACTUALIZACION DE 0.5 SEGUNDOS O 500 MILISEGUNDOS
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
  dash.dependencies.Output('velocidad', 'children'),
  dash.dependencies.Output('acel-gyro-graph','figure'),
  dash.dependencies.Output('mision-time', 'children'),
  dash.dependencies.Output("pila-porcentaje", 'children'),
  [dash.dependencies.Input('interval-component', 'n_intervals')] 
)
def data_listener(n):
  global dic, active, time_starter

  if active == False:
    raise dash.exceptions.PreventUpdate

  # try:
  #   output = functions.open_serial(4) # ESTA FUNCIÓN TRAE LOS VALORES DEL PUERTO SERIAL Cambiar puerto si es necesario
  # except:
  #   print("Error al conectar con puerto serial")
  output = functions.random_generator()

  if output == None:
    al = dash.no_update
    la = dash.no_update
    lo = dash.no_update
    te = dash.no_update
    pr = dash.no_update
    hu = dash.no_update
    ax = dash.no_update
    ay = dash.no_update
    az = dash.no_update
    gx = dash.no_update
    gy = dash.no_update
    gz = dash.no_update
    graph_giro_ace = dash.no_update
  else: 
    al = output['Al']
    la = output['La']
    lo = output['Lo']
    te = output['Te']
    pr = output['Pr']
    hu = output['Hu']
    ax = output['Ax']
    ay = output['Ay']
    az = output['Az']
    gx = output['Gx']
    gy = output['Gy']
    gz = output['Gz']
    ve = output['Ve']

    g,a = functions.graphs_values(output)
    dic['A'].append(a)
    dic['G'].append(g)
    graph_giro_ace = functions.plot_graphs_ace_giro(dic)


  # El tiempo de misión solo se actualizará cada segundo
  if n%2 != 1: #Si no es un segundo exacto no te actualices
    mision_time = dash.no_update
  else:
    mision_time = functions.get_time_mision(time_starter)


  pila_value =   np.random.randint(5,101)
  pila_value_str = str(pila_value) + "%"
  if pila_value < 20:
    pila = [html.Div(
              className="pila-pila",
              style={'height': pila_value_str, "background-color": "#F95738"}
            ),
            html.H5(id="battery-percent", children=[pila_value_str])]
  else:
    pila = [html.Div(
              className="pila-pila",
              style={'height': pila_value_str, "background-color": "#55F165"}
            ),
            html.H5(id="battery-percent", children=[pila_value_str])]
  
  
  return al, la, lo, te, pr, hu, ax, ay, az, gx, gy, gz, ve, graph_giro_ace, mision_time, pila

@app.callback(
  dash.dependencies.Output('date', 'children'),
  dash.dependencies.Output('hour', 'children'),
  [dash.dependencies.Input('interval-component', 'n_intervals')] 
)
def date_and_hour(n):
  global active

  if active == True:
    raise dash.exceptions.PreventUpdate
  # La hora y el tiempo de misión solo se actualizarán cada segundo
  if n%2 != 1: #Si no es un segundo exacto no te actualices
    hour = dash.no_update
  else:
    hour = functions.current_time() 
  # La fecha solo se actualizará al iniciar el programa
  if n ==0 : #Si el intervalo es 1 (acaba de arrancar) actualizate
    date = functions.today_date()
  else:
    date = dash.no_update

  return date, hour


## ESTA FUNCIÓN ES LA RESPONSABLE DE LA INTERACCIÓN CON LA IMAGEN 
## ESTA EN CAMBIO SOLO TIENE 1 OUTPUT QUE ES LA IMAGEN A LA QUE SE LE 
## PUEDEN MOVER LOS VALORES DE hsv O LOS blurs 
## LO QUE HACE QUE SE ACTUALICE ES EL CAMBIO EN LO INPUTS
## QUE EN ESTE CASO SON LOS SLIDERS Y LOS BOTONES
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