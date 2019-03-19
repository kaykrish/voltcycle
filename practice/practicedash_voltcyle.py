import dash
import dash_core_components as dcc
import dash_html_components as html
import base64

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#F8F9F9',
    'text': '#000000'
}

image_filename = 'logo.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Voltcycle',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div([
        html.Img(draggable=True, style={
                'height': '20%',
                'width': '20%'
            },  src='data:image/png;base64,{}'.format(encoded_image))
   ], style={'textAlign': 'center'}),

    html.Div(children='A tool for analysis of cyclic voltammetry.', style={
        'textAlign': 'center',
        'color': colors['text']
    })
])



if __name__ == '__main__':
    app.run_server(debug=True)