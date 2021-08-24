import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

def plot_figure(file):
  dcc.Graph(
    figure=px.imshow(file)
  )