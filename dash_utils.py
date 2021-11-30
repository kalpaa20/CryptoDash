#DASH
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from flask import Flask

def section_one():
#def make_card(alert_message, color, cardbody, style_dict = None):
    
	return	html.Div([
					html.H4("CHOOSE A CRYPTOCURRENCY CODE TO CHECK PRICE"),
		            html.Div
		                (
		                    [
		                    "Input: ",
		                    dcc.Input(id='cryptosymbolcheck', value='BTC',  type='text')
		                    ]
		                ),
		            html.Br(),
		            html.Div("Live Ticker"),
		            html.Div(id='live-ticker-check')
		            ]
		            )


def section_two():
    return  html.Div(
    				[
                    html.H2("TRADING SECTION"),
                    html.H4("ENTER A CRYPTOCURRENCY CODE TO TRADE"),
                    html.Div
                        (
                            [
                            "Input: ",
                            dcc.Input(id='cryptosymbol', value='BTC',  type='text')
                            ]
                        ),
                    html.Br(),
                    html.Div("Live Ticker"),
                    html.Div(id='live-ticker')
					]
					)



def section_three():
	return  html.Div(
					[
                    html.H4("TRADING SECTION : SELL "),
                    html.Div([
                            "Enter target price for Selling: ",
                            dcc.Input(id='target-saleval-input', value=0, type='number')
                            ]),
                    html.Br(),
                    html.Div([
                            "Enter quantity for Selling: ",
                            dcc.Input(id='target-saleqty-input', value=0, type='number')
                            ]),
                    html.Br(),
                    html.Div(id = 'target-saleamt'),
                    html.Br(),
                    html.Div("Trade Result : "),
                    html.Div(id = 'target-saleval-result')
                    ]
					)


def section_four():
	return html.Div(
					[
                    html.H4("TRADING SECTION : BUY  "),
                    html.Div([
                            "Enter target price for Purchasing: ",
                            dcc.Input(id='target-purchaseval-input', value=0, type='number')
                            ]),
                    html.Br(),
                    html.Div([
                            "Enter quantity for Purchasing: ",
                            dcc.Input(id='target-purchaseqty-input', value=0, type='number')
                            ]),
                    html.Br(),
                    html.Div(id = 'target-purchaseamt'),
                    html.Br(),
                    html.Div("Trade Result : "),
                    html.Div(id = 'target-purchaseval-result')
					])


def section_five():
	return html.Div([
		    dcc.Checklist(
		        id='toggle-rangeslider',
		        options=[{'label': 'Include Rangeslider', 
		                  'value': 'slider'}],
		        value=['slider']
		    ),
		    dcc.Graph(id="graph"),
		])
