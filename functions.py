import plotly.express as px
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go

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


def cylinder(r,h, a = 0, nt = 100, nv = 50):
  theta = np.linspace(0, 2*np.pi, nt)
  v = np.linspace(a, a+h, nv)
  theta, v = np.meshgrid(theta,v)
  x = r*np.cos(theta)
  y = r*np.sin(theta)
  z = v
  return x,y,z

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