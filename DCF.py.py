#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy pandas dash yfinance


# In[9]:


pip install plotly


# In[14]:


import dash
from dash import html, dcc, Input, Output, State
import plotly.graph_objs as go
import numpy as np
import yfinance as yf

app = dash.Dash(__name__)

# Define some CSS styles
styles = {
    'container': {
        'padding': '10px 30px',
        'border': '1px solid #DDD',
        'border-radius': '5px',
        'margin': '10px',
        'background-color': '#F9F9F9'
    },
    'input': {
        'margin': '10px 5px',
        'padding': '5px',
    },
    'label': {
        'margin': '10px 5px',
        'font-weight': 'bold',
        'color': '#555',
    },
    'button': {
        'margin': '20px 5px',
        'font-size': '16px',
        'font-weight': 'bold',
        'background-color': '#007BFF',
        'color': 'white',
        'border': 'none',
        'padding': '10px 20px',
        'cursor': 'pointer',
    },
    'header': {
        'text-align': 'center',
        'padding': '10px',
        'color': '#444',
        'background-color': '#EFEFEF',
        'margin': '10px',
        'border-radius': '5px',
        'font-size': '24px',
        'border-bottom': '2px solid #CCC'
    }
}

app.layout = html.Div([
    html.H1("DCF Model Dashboard", style=styles['header']),
    html.Div([
        html.Label('Stock Symbol:', style=styles['label']),
        dcc.Input(id='stock-input', type='text', value='AAPL', style=styles['input']),
    ], style=styles['container']),
    html.Div([
        html.Label('Growth Rate:', style=styles['label']),
        dcc.Input(id='growth-rate', type='number', value=0.05, style=styles['input']),
        html.Label('Discount Rate:', style=styles['label']),
        dcc.Input(id='discount-rate', type='number', value=0.10, style=styles['input']),
        html.Label('Years:', style=styles['label']),
        dcc.Input(id='years', type='number', value=10, style=styles['input']),
    ], style=styles['container']),
    html.Button('Calculate DCF', id='submit-val', n_clicks=0, style=styles['button']),
    html.Div(id='result-text', style={'margin': '20px', 'font-size': '24px'}),
    dcc.Graph(id='dcf-graph')
], style={'font-family': 'Arial, sans-serif', 'padding': '20px', 'background-color': '#FFFFFF'})

@app.callback(
    [Output('result-text', 'children'),
     Output('dcf-graph', 'figure')],
    [Input('submit-val', 'n_clicks')],
    [State('stock-input', 'value'),
     State('growth-rate', 'value'),
     State('discount-rate', 'value'),
     State('years', 'value')])
def update_output(n_clicks, ticker, growth_rate, discount_rate, years):
    if n_clicks > 0:
        fcf = get_free_cash_flow(ticker)
        dcf_value, cash_flows, discounted_cash_flows = calculate_dcf(fcf, growth_rate, discount_rate, years)
        figure = {
            'data': [
                go.Scatter(x=list(range(1, years + 1)), y=cash_flows, mode='lines+markers', name='Future Cash Flows'),
                go.Scatter(x=list(range(1, years + 1)), y=discounted_cash_flows, mode='lines+markers', name='Discounted Cash Flows')
            ],
            'layout': go.Layout(title='Cash Flow Projection', xaxis={'title': 'Year'}, yaxis={'title': 'Value'})
        }
        return f'The DCF value of {ticker} is ${dcf_value:.2f}', figure
    return 'Enter values and press calculate.', go.Figure()

if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




