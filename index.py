# ----------------------------------------------------------------------------------------------------
#Library imports
import config
import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from flask import Flask
import plotly.graph_objects as go
from datetime import datetime


from binance.client import Client
from dash_utils import section_one, section_two, section_three, section_four, section_five
import historical_data
# ----------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------
# init
def init_client():
    api_key = config.api_key
    api_secret = config.api_secret

    #CCreate an object of type binance client
    client = Client(api_key, api_secret)

    #Setting the API endpoint for the binance client, which will be accessed through the API Key and API Secret
    client.API_URL = config.API_URL

    return client


client = init_client() #Initialize the API client


# ----------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
# Create basic dash dashboard

#Setting flask server
server = Flask(__name__)

#Basic app
app=dash.Dash()
app

#Defining the HTML Component of the dash app
#1 Defining the layout

main_page_layout = html.Div(
                            children = 
                                [
                                html.Div(
                                        html.H2("CryptoDash - Powered by Binance API"),
                                        style = {
                                                "color":"white",
                                                "text-align":"center",
                                                "background-color":"grey",
                                                "border-style":"solid",
                                                "display":"inline-block",
                                                "width":"80%"
                                                }
                                        ),                                
                                html.Div(
                                        children = 
                                            [
                                            section_one()
                                            ],
                                        style = {
                                                "color":"grey",
                                                "text-align":"center",
                                                "background-color":"khaki",
                                                "border-style":"solid",
                                                "display":"inline-block",
                                                "width":"30%",
                                                "height":180
                                                }
                                        ),
                                html.Div(
                                        children = 
                                            [
                                            section_two()
                                            ],
                                        style = {
                                                "color":"grey",
                                                "text-align":"center",
                                                "background-color":"cornsilk",
                                                "border-style":"solid",
                                                "display":"inline-block",
                                                "width":"50%",
                                                "height":200
                                                }                                        
                                        ),
                                html.Div(
                                        children = 
                                            [
                                            section_three()
                                            ],
                                        style = {
                                                "color":"grey",
                                                "text-align":"center",
                                                "background-color":"cornsilk",
                                                "border-style":"solid",
                                                "display":"inline-block",
                                                "width":"40%",
                                                "height":300
                                                }
                                        ),
                                html.Div(
                                        children = 
                                            [
                                            section_four()
                                            ],
                                        style = {
                                                "color":"grey",
                                                "text-align":"center",
                                                "background-color":"khaki",
                                                "border-style":"solid",
                                                "display":"inline-block",
                                                "width":"40%",
                                                "height":300
                                                }
                                        ),
                                html.Div(
                                        children = 
                                            [
                                            html.H4("LAST 5 TRADES EXECUTED"),
                                            ],
                                        style = {
                                                "color":"grey",
                                                "text-align":"center",
                                                "background-color":"khaki",
                                                "border-style":"solid",
                                                "display":"inline-block",
                                                "width":"80%"
                                                }
                                        ),
                                html.Div(
                                        children = 
                                            [
                                            section_five()
                                            ],
                                        style = {
                                                "color":"grey",
                                                "text-align":"center",
                                                "background-color":"cornsilk",
                                                "border-style":"solid",
                                                "display":"inline-block",
                                                "width":"80%"
                                                }
                                        ),
                                html.Div(
                                        "WEBSOCKET TICKER" ,
                                        style = {
                                                "color":"grey",
                                                "text-align":"center",
                                                "background-color":"cornsilk",
                                                "border-style":"solid",
                                                "display":"inline-block",
                                                "width":"25%"
                                                }
                                        ),
                                html.Div(
                                        "PREDICTED PRICES FOR CRYPTO SYMBOL" ,
                                        style = {
                                                "color":"grey",
                                                "text-align":"center",
                                                "background-color":"khaki",
                                                "border-style":"solid",
                                                "display":"inline-block",
                                                "width":"25%"
                                                }
                                        ),
                                html.Div(
                                        "Section 7" ,
                                        style = {
                                                "color":"grey",
                                                "text-align":"center",
                                                "background-color":"cornsilk",
                                                "border-style":"solid",
                                                "display":"inline-block",
                                                "width":"30%"
                                                }
                                        ),
                                html.Div(
                                        children = [
                                                dbc.Col([ #Column 2
                                                    dcc.Interval
                                                        (
                                                        id='1-second-interval',
                                                        interval=1000,  # 1000 milliseconds
                                                        n_intervals=0
                                                        )
                                                    ]),
                                                dbc.Col([ #Column 2
                                                    dcc.Interval
                                                        (
                                                        id='5-second-interval',
                                                        interval=5000,  # 1000 milliseconds
                                                        n_intervals=0
                                                        )
                                                    ])
                                                ],
                                        style = {
                                                "color":"grey",
                                                "text-align":"center",
                                                "background-color":"goldenrod",
                                                "border-style":"solid",
                                                "display":"inline-block",
                                                "width":"80%"
                                                }
                                        )                                
                                ],
                            style = 
                                {
                                "width":"100%",
                                "paffing":10
                                }
                            ) #End parent html Div


app.layout = main_page_layout
# ----------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------



#Setting the app callback to update live-ticker output based on the input

@app.callback(
    Output(component_id='live-ticker-check', component_property='children'),
    Input(component_id='cryptosymbolcheck', component_property='value'),
    Input('5-second-interval', 'n_intervals')
)
def update_live_ticker_check(input_value, n): #This takes the first and second inputs
    crypto_ticker = client.get_symbol_ticker(symbol=input_value + "USDT")
    crypto_price = crypto_ticker["price"]
    return crypto_price #,  'Crypto Price USDT B: ' + crypto_price # These are the first and the second output



@app.callback(
    Output(component_id='live-ticker', component_property='children'),
    Input(component_id='cryptosymbol', component_property='value'),
    Input('1-second-interval', 'n_intervals')
)
def update_live_ticker(input_value, n): #This takes the first and second inputs
    crypto_ticker = client.get_symbol_ticker(symbol=input_value + "USDT")
    crypto_price = crypto_ticker["price"]
    return crypto_price #,  'Crypto Price USDT B: ' + crypto_price # These are the first and the second output



#App callback for calculating total amount of trade
@app.callback(
    Output('target-saleamt', 'children'),
    Input('target-saleval-input', 'value'),
    Input('target-saleqty-input', 'value'),    
    Input('5-second-interval', 'n_intervals')    
    )
def update_sale_amount(sell_price , sell_qty, n):
    sell_amt = float(sell_price) * float(sell_qty)
    return "Total Trade amount : " + str(sell_amt) + " USDT"


@app.callback(
    Output('target-purchaseamt', 'children'),
    Input('target-purchaseval-input', 'value'),
    Input('target-purchaseqty-input', 'value'),    
    Input('5-second-interval', 'n_intervals')    
    )
def update_purchase_amount(purchase_price , purchase_qty, n):
    purchase_amt = float(purchase_price) * float(purchase_qty)
    return "Total Trade amount : " + str(purchase_amt) + " USDT"



#Setting callback to fetch the target value customer wants to reach
#Callback for selling
@app.callback(
    Output('target-saleval-result', 'children'),
    Input('live-ticker', 'children'),
    Input('target-saleval-input', 'value'),
    Input('5-second-interval', 'n_intervals')
    )
def update_target_sale(curr_val, expected_val, n):
    if int(float(expected_val)) == 0:
        return 'No value entered'
    if float(curr_val) >= float(expected_val): #If current price for selling is higher than expected price, execute trade
        return 'TRADE EXECUTED. Target met. Expected value : ' + str(expected_val) + '. Current value : ' +  str(curr_val)
    else:
        return 'Waiting for right price... Expected value : ' + str(expected_val) + '. Current value : ' + str(curr_val)


#Callback for buying/purchasing
@app.callback(
    Output('target-purchaseval-result', 'children'),
    Input('live-ticker', 'children'),
    Input('target-purchaseval-input', 'value'),
    Input('5-second-interval', 'n_intervals')
    )
def update_target_buy(curr_val, expected_val, n):
    if int(float(expected_val)) == 0:
        return 'No value entered'
    if float(curr_val) <= float(expected_val): #If the current value for buying is lesser than expected price, execute trade
        return 'TRADE EXECUTED. Target met. Expected value : ' + str(expected_val) + '. Current value : ' +  str(curr_val)
    else:
        return 'Waiting for right price... Expected value : ' + str(expected_val) + '. Current value : ' + str(curr_val)





#app callback to refresh the historical charts
@app.callback(
    Output("graph", "figure"), 
    Input('cryptosymbol', 'value'),
    Input("toggle-rangeslider", "value"),
    Input('5-second-interval', 'n_intervals'))
def display_candlestick(symbol, value, n):
    df = historical_data.historical_data(symbol , client) #historical_data : Get loaded dataframe
    fig = go.Figure(go.Candlestick(
        x=df['dateTime'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
    ))
    
    fig.update_layout(
        xaxis_rangeslider_visible='slider' in value
    )

    return fig




#-----UNCLEAR DEPENDENCY
# This section is added due to dash callback error : KeyError: "Callback function not found for output 'target-result.children', perhaps you forgot to prepend the '@'?"
# Despite id target-result not existing in any layout
@app.callback(
    Output('target-result', 'children'),
    Input('live-ticker', 'children'),
    Input('target-saleval-input', 'value'),
    Input('5-second-interval', 'n_intervals')
    )
def update_target_result(input_value, anotherval,  n):
    return 'TESTING'
#-----END UNCLEAR DEPENDENCY

# ----------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
#2 Invoking dash app through main
if __name__ == '__main__':
        app.run_server(debug = False, host="0.0.0.0", port = 8080)  
        #app.run_server(debug = True)  

#This will launch and run a server on a port. You will see a URL you can click. 
# ----------------------------------------------------------------------------------------------------

