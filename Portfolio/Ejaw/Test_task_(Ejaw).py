#!/usr/bin/env python
# coding: utf-8

# ## TASK

# 1) Скачать исторические данные с Бинанс :
# 
# - period:  1 Nov 2020 - 1 Jul 2021
# - таймфрейм (1Hour and 5 minute)
# - BTCUSDT  and ETHUSDT

# 2) Стратегия:
# 	ТОЧКА ВХОДА:
# 		- Если индикатор RSI(14) > 50 и ЕМА(20) пересекла ЕМА(50) вверх— покупаем
# 	ТОЧКА ВЫХОДА:
# 		- Если ЕМА(20) пересекла ЕМА(50) вниз — продаём
# 

# 3) Параметры стратегии:
# 	Баланс = 1000 (usdt)
# 	Лот (1 ордер) = 100 (usdt)
# 	
# 	если  таймфрейм (1Hour) — то за последних 6 месяцев (1 Января — 1 Июля)
# 	если  таймфрейм (5 minute) — то за последний месяц (Июнь)
# 

# 4) Результат бектеста:
# 
# - Конечный баланс
# - Профит (usdt)
# - % Профита
# - Максимально прибыльная сделка (usdt)
# - Максимально убыточная сделка (usdt)
# - К-во всех сделок
# - К-во прибыльных сделок
# - К-во убыточных сделок
# 
# - Максимальное к-во прибыльных сделок в подряд
# - Максимальное к-во убыточных сделок в подряд
# 
# 
# Комментарий:
# - всего должно получиться 4 ответа (результатов бектеста)
# 

import requests 
import json 
import pandas as pd 
import numpy as np  
from datetime import datetime

import warnings
warnings.filterwarnings('ignore')


def max_len(lst):
    ml = 0
    curr_lst = []
    for x in lst:
        if x:
            curr_lst.append(x)
        else:
            if len(curr_lst) > ml:
                ml = len(curr_lst)
            curr_lst = []
    if len(curr_lst) > ml:
                ml = len(curr_lst)
    return ml


def get_klines_iter(symbol, interval, start, end, limit=500):
    df = pd.DataFrame()
    startDate = end
    while startDate > start:
        url = 'https://api.binance.com/api/v3/klines?symbol=' + symbol + '&interval=' + interval + '&limit='  + str(limit)
        if startDate is not None:
            url += '&endTime=' + str(startDate)
        
        df2 = pd.read_json(url)
        df2.columns = [
            'Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', 'Quote asset volume', 
            'Number of trades','Taker by base', 'Taker buy quote', 'Ignore'
        ]
        df = pd.concat([df2, df], axis=0, ignore_index=True, keys=None)
        startDate = df.Opentime[0]   
    df.reset_index(drop=True, inplace=True)    
    return df[['Opentime', 'Open', 'High', 'Low', 'Close']]


def RSI(series, period):
    delta = series.diff().dropna()
    u = delta * 0
    d = u.copy()
    u[delta > 0] = delta[delta > 0]
    d[delta < 0] = -delta[delta < 0]
    u[u.index[period-1]] = np.mean( u[:period] ) # first value is sum of avg gains
    u = u.drop(u.index[:(period-1)])
    d[d.index[period-1]] = np.mean( d[:period] ) # first value is sum of avg losses
    d = d.drop(d.index[:(period-1)])
    rs = pd.DataFrame.ewm(u, com=period-1, adjust=False).mean() /          pd.DataFrame.ewm(d, com=period-1, adjust=False).mean()
    return 100 - 100 / (1 + rs)


def general(data, symbol):
    data = data.copy()
    initial_balance_USDT = 1000
    order = 100
    balance_USDT = initial_balance_USDT
    balance_symbol = 0
    data['balance_USDT'] = 0
    data['balance_{}'.format(symbol)] = 0
    data['profit_deal'] = 0
    list_index_up = []
    list_index_down = []
    for i in data.index.to_list():
        current_price = data.loc[i, 'Close']
        if balance_USDT > 0 and data.loc[i, 'RSI(14)'] > 50 and data.loc[i, 'EMA(20)'] > data.loc[i, 'EMA(50)']:
            val_order = min(order, balance_USDT)
            balance_USDT -= val_order
            balance_symbol += val_order / current_price
            list_index_up.append(i)
            for j in list_index_down:
                data.loc[j, 'profit_deal'] = (
                    (data.loc[j, 'Close'] - data.loc[i, 'EMA(50)']) / data.loc[i, 'EMA(50)']
                )
                data.loc[j, 'profit'] = order * (1 - data.loc[i, 'Close'] / data.loc[j, 'Close'])
            list_index_down = []                
        if balance_symbol > 0 and data.loc[i, 'EMA(20)'] < data.loc[i, 'EMA(50)']:
            val_order = min(order/current_price, balance_symbol)
            balance_symbol -= val_order
            balance_USDT += val_order * current_price 
            list_index_down.append(i)
            for j in list_index_up:
                data.loc[j, 'profit_deal'] = (
                    (data.loc[j, 'Close'] - data.loc[i, 'EMA(50)']) / data.loc[i, 'EMA(50)']
                )
                data.loc[j, 'profit'] = order * (1 - data.loc[i, 'Close'] / data.loc[j, 'Close'])
            list_index_up = []
        data.loc[i, 'balance_USDT'] = balance_USDT
        data.loc[i, 'balance_{}'.format(symbol)] = balance_symbol
    total_balance_USDT = balance_USDT + balance_symbol * current_price
    profit = total_balance_USDT - initial_balance_USDT 
    percentage_profit = profit / initial_balance_USDT * 100
    max_profit = data['profit'].max()
    min_profit = data['profit'].min()
    count_deal = len(data[data['profit_deal']!=0])
    count_deal_plus = len(data[data['profit_deal']>0])
    count_deal_minus = len(data[data['profit_deal']<0])
    max_deal_plus = max_len(data['profit_deal']>0)
    max_deal_minus = max_len(data['profit_deal']<0)
    print('Конечный баланс:', total_balance_USDT)
    print('Профит (usdt):', profit)
    print('% Профита:', percentage_profit)
    print('Максимально прибыльная сделка (usdt):', max_profit)
    print('Максимально убыточная сделка (usdt):', min_profit)
    print('К-во всех сделок:', count_deal)
    print('К-во прибыльных сделок):', count_deal_plus)
    print('К-во убыточных сделок:', count_deal_minus)
    print('Максимальное к-во прибыльных сделок в подряд:', max_deal_plus)
    print('Максимальное к-во убыточных сделок в подряд:', max_deal_minus)


start = int((datetime(2020, 11, 1) - datetime(1970,1,1)).total_seconds() * 1000)
end = int((datetime(2021, 7, 1) - datetime(1970,1,1)).total_seconds() * 1000)
BTCUSDT_1H = get_klines_iter('BTCUSDT', '1h', start, end, limit=1000)
BTCUSDT_5M = get_klines_iter('BTCUSDT', '5m', start, end, limit=1000)
ETHUSDT_1H = get_klines_iter('ETHUSDT', '1h', start, end, limit=1000)
ETHUSDT_5M = get_klines_iter('ETHUSDT', '5m', start, end, limit=1000)

BTCUSDT_1H['RSI(14)'] =RSI(BTCUSDT_1H.Close, 14)
BTCUSDT_5M['RSI(14)'] =RSI(BTCUSDT_5M.Close, 14)
ETHUSDT_1H['RSI(14)'] =RSI(ETHUSDT_1H.Close, 14)
ETHUSDT_5M['RSI(14)'] =RSI(ETHUSDT_5M.Close, 14)

BTCUSDT_1H['EMA(20)'] = pd.Series.ewm(BTCUSDT_1H.Close, span=20).mean()
BTCUSDT_1H['EMA(50)'] = pd.Series.ewm(BTCUSDT_1H.Close, span=50).mean()
BTCUSDT_5M['EMA(20)'] = pd.Series.ewm(BTCUSDT_5M.Close, span=20).mean()
BTCUSDT_5M['EMA(50)'] = pd.Series.ewm(BTCUSDT_5M.Close, span=50).mean()
ETHUSDT_1H['EMA(20)'] = pd.Series.ewm(ETHUSDT_1H.Close, span=20).mean()
ETHUSDT_1H['EMA(50)'] = pd.Series.ewm(ETHUSDT_1H.Close, span=50).mean()
ETHUSDT_5M['EMA(20)'] = pd.Series.ewm(ETHUSDT_5M.Close, span=20).mean()
ETHUSDT_5M['EMA(50)'] = pd.Series.ewm(ETHUSDT_5M.Close, span=50).mean()

time_1H = int((datetime(2021, 1, 1) - datetime(1970,1,1)).total_seconds() * 1000)
time_5M = int((datetime(2021, 6, 1) - datetime(1970,1,1)).total_seconds() * 1000)
BTCUSDT_1H_new = BTCUSDT_1H[BTCUSDT_1H['Opentime']>time_1H]
BTCUSDT_5M_new = BTCUSDT_5M[BTCUSDT_5M['Opentime']>time_5M]
ETHUSDT_1H_new = ETHUSDT_1H[ETHUSDT_1H['Opentime']>time_1H]
ETHUSDT_5M_new = ETHUSDT_5M[ETHUSDT_5M['Opentime']>time_5M]


# Результат:
# 1. BTCUSDT, 1 Hour
general(BTCUSDT_1H_new, "BTC")

# 2. BTCUSDT, 5 minute
general(BTCUSDT_5M_new, "BTC")

# 3. ETHUSDT, 1 Hour
general(ETHUSDT_1H_new, "ETH")

#  4. ETHUSDT, 5 minute
general(ETHUSDT_5M_new, "ETH")
