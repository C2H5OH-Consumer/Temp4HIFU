## Use DASH to build user GUI
from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt

from presets import setmedium

## 

press_data = pd.read_csv(r"C:\Users\geral\OneDrive\Documents\GitHub\TempCompliance4HIFU\src\sample_data.csv")  # sample_data == 121 x 501 double
data_output = {''}
mediumProp = setmedium.setMedium('Water',0)


app = Dash('tempCompliance4HIFU')

# ALLOWED_TYPES = ("text", "number", "password", "email", "search","tel", "url", "range", "hidden",)

app.layout = [
    # Title
    html.H1(children = 'Temperature Compliance for HIFU Transducers', style = {'textAlign':'center'}), 
    html.H2(children = 'By Gerald Lee', style = {'textAlign':'center'}),
    
    # Top Section - INPUTS
    html.Div([     
                
        # Medium Section (Left)
        # html.Div([
            html.H3('Medium', style ={'textAlign':'center'}), 
            dcc.Dropdown(['Custom','Water','Glycerol','Egg White','Castor Oil'],'Custom',id='DROP_medium'),
            
            html.P('Speed of Sound [m/s]', style ={'textAlign':'left'}), 
            dcc.Input(id="Speed", type='number', placeholder='Input Speed of Sound'),

            html.P('Density [kg/m^3]', style ={'textAlign':'left'}),
            dcc.Input(id="Density", type='number', placeholder='Input Density'),

            html.P('Absorption Coeffient [Np/(m*MHz^2)]', style ={'textAlign':'left'}),
            dcc.Input(id="AbsCoeff", type='number', placeholder='Input Absorption Coefficient'),
        
            html.P('Specific Heat Capacity [J/(kg*K)]', style ={'textAlign':'left'}),
            dcc.Input(id="SpecHeatCap", type='number', placeholder='Input Specific Heat Capacity'),
                
            html.P('Thermal Diffusivity [(m^2)/s]', style ={'textAlign':'left'}),
            dcc.Input(id="ThermDiff", type='number', placeholder='Input Thermal Diffusivity'),  
          
        # ], style={'width': '30%', 'display': 'inline-block'}),


        # Heating Section (Right)
        # html.Div([
                html.H3('Heating', style ={'textAlign':'center'}), 

                html.P('Time Heating [s]', style ={'textAlign':'left'}),
                dcc.Input(id="HeatTime", type='number', placeholder='Input Heat Time'),

                html.P('Time Cooling [s]', style ={'textAlign':'left'}),
                dcc.Input(id="CoolTime", type='number', placeholder='Input Cool Time'),

                html.P('Duty Cycle [Percentage]', style ={'textAlign':'left'}),
                dcc.Input(id="DutyCycle", type='number', placeholder='Input Duty Cycle'),

        # ], style={'width': '30%', 'float': 'right', 'display': 'inline-block'}),


        # Trandsucer Section (Middle)
        # html.Div([
                html.H3('Transducer', style ={'textAlign':'center'}), 

                html.P('Frequency [MHz]', style ={'textAlign':'left'}),
                dcc.Input(id="Frequency", type='number', placeholder='Input Frequency'),

                html.P('F-Number', style ={'textAlign':'left'}),
                dcc.Input(id="FNum", type='number', placeholder='Input F Number'),

                html.P('Radius [mm]', style ={'textAlign':'left'}),
                dcc.Input(id="Radius", type='number', placeholder='Input Radius'),

    ], style={'width': '30%', 'display': 'inline-block','padding': '10px 5px'}),

    # ], style={'padding': '10px 5px'}),


    # Section 2 (Bottom Half) - For Display
    html.Div([
        html.Button('CALCULATE PRESSURE AND TEMPERATURE', id='button'),
        html.H2('Results', style ={'textAlign':'center'}), 
        # html.Div([
            dcc.Dropdown(['Pressure','Temperature'],'Pressure',id='DROP_field2D'),
            dcc.Graph(id='GRAPH_field2D',hoverData={'points': [{'customdata': 'Pressure'}]}),
        # ],style={'width': '45%', 'display': 'inline-block'}),

        # html.Div([
            dcc.Graph(id='GRAPH_time1D'),
        ], style={'width': '60%', 'float': 'right', 'display': 'inline-block','padding': '10px 5px'}),


    # ],style={'padding': '10px 5px'}),

]


@callback(
    Output('GRAPH_field2D','figure'),
    Input('DROP_field2D','value')
)
def update_figure(value):
    return {value}



# @callback(
#     Output('GRAPH_time1D', 'figure'),
#     Input('GRAPH_field2D', 'hoverData'),
#     Input('crossfilter-xaxis-column', 'value'),
#     Input('crossfilter-xaxis-type', 'value'))
# def update_x_timeseries(hoverData, xaxis_column_name, axis_type):
#     country_name = hoverData['points'][0]['customdata']
#     dff = df[df['Country Name'] == country_name]
#     dff = dff[dff['Indicator Name'] == xaxis_column_name]
#     title = '<b>{}</b><br>{}'.format(country_name, xaxis_column_name)
#     return create_time_series(dff, axis_type, title)





# @callback(
#     Output('graph-content','figure'),
#     Input('dropdown-selection','value')
# )
# def update_graph(value):
#     dff = press_data[press_data.country==value]
#     return px.line(dff, x='year',y='pop')









# @callback(
#     Output('crossfilter-indicator-scatter', 'figure'),
#     Input('crossfilter-xaxis-column', 'value'),
#     Input('crossfilter-yaxis-column', 'value'),
#     Input('crossfilter-xaxis-type', 'value'),
#     Input('crossfilter-yaxis-type', 'value'),
#     Input('crossfilter-year--slider', 'value'))
# def update_graph(xaxis_column_name, yaxis_column_name,
#                  xaxis_type, yaxis_type,
#                  year_value):
#     dff = df[df['Year'] == year_value]

#     fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
#             y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
#             hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name']
#             )

#     fig.update_traces(customdata=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

#     fig.update_xaxes(title=xaxis_column_name, type='linear' if xaxis_type == 'Linear' else 'log')

#     fig.update_yaxes(title=yaxis_column_name, type='linear' if yaxis_type == 'Linear' else 'log')

#     fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

#     return fig


# def create_time_series(dff, axis_type, title):

#     fig = px.scatter(dff, x='Year', y='Value')

#     fig.update_traces(mode='lines+markers')

#     fig.update_xaxes(showgrid=False)

#     fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')

#     fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom',
#                        xref='paper', yref='paper', showarrow=False, align='left',
#                        text=title)

#     fig.update_layout(height=225, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})

#     return fig


# @callback(
#     Output('x-time-series', 'figure'),
#     Input('crossfilter-indicator-scatter', 'hoverData'),
#     Input('crossfilter-xaxis-column', 'value'),
#     Input('crossfilter-xaxis-type', 'value'))
# def update_x_timeseries(hoverData, xaxis_column_name, axis_type):
#     country_name = hoverData['points'][0]['customdata']
#     dff = df[df['Country Name'] == country_name]
#     dff = dff[dff['Indicator Name'] == xaxis_column_name]
#     title = '<b>{}</b><br>{}'.format(country_name, xaxis_column_name)
#     return create_time_series(dff, axis_type, title)


# @callback(
#     Output('y-time-series', 'figure'),
#     Input('crossfilter-indicator-scatter', 'hoverData'),
#     Input('crossfilter-yaxis-column', 'value'),
#     Input('crossfilter-yaxis-type', 'value'))
# def update_y_timeseries(hoverData, yaxis_column_name, axis_type):
#     dff = df[df['Country Name'] == hoverData['points'][0]['customdata']]
#     dff = dff[dff['Indicator Name'] == yaxis_column_name]
#     return create_time_series(dff, axis_type, yaxis_column_name)














if __name__ == '__main__':
    app.run(debug=True)



