#Librerias
from BinanceKeys import api_key,api_secret
from binance.client import Client
import websocket,json
import pandas as pd
import numpy as np

#Datos del cliente
api_key=api_key
api_secret=api_secret
client=Client(api_key,api_secret)

#Recepción de datos en vivo
SOCKET_mult="wss://fstream.binance.com/ws/adausdt@kline_1m"

#Cripto
symb='ADAUSDT'

def on_open(ws):
    print('Conexión abierta')
def on_close(ws):
    print('Conexión caducada')
def on_message(ws,message):
    #LIVE DATA
    global msg,symb
    msg=json.loads(message)
        
    #Cripto 5 minutos
    symbol_five=msg['s']
    time_five=msg['E']
    open_five=msg['k']['o']
    close_five=msg['k']['c']
    high_five=msg['k']['h']
    low_five=msg['k']['l']
    ccandle_five=msg['k']['x']

    if ccandle_five: 

        #DATA FRAME
        frame=pd.DataFrame([[symbol_five,time_five,open_five,close_five,high_five,low_five]],columns=['symbol','time','open','close','high','low'])
        frame.time=pd.to_datetime(frame.time,unit='ms')
        frame.open=frame.open.astype(float)
        frame.close=frame.close.astype(float)
        frame.high=frame.high.astype(float)
        frame.low=frame.low.astype(float)
        print(frame)
              
ws=websocket.WebSocketApp(SOCKET_mult,on_open=on_open,on_close=on_close,on_message=on_message)
ws.run_forever()

