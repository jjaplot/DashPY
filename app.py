import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
bands=['Interpol', 'Dr Dog', 'Franz ', 'Haim']
ibu_values=[5,8,5,3]
abv_values=[12, 20, 5, 3]
color1='lightblue'
color2='darkgreen'
mytitle='Number of Records'
tabtitle='Tunes'
myheading='Bands and Number of Records'
label1='IBU'
label2='ABV'
githublink='https://github.com/jjaplot/DashPY'
sourceurl='https://github.com/jjaplot/DashPY'

########### Set up the chart
LPS = go.Bar(
    x=bands,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
singles = go.Bar(
    x=bands,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

band_data = [LPS, singles]
band_layout = go.Layout(
    barmode='group',
    title = mytitle
)

band_fig = go.Figure(data=band_data, layout=band_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=band_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()