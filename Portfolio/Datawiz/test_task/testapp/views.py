from django.shortcuts import render
from dwapi import datawiz
from datetime import datetime
import datetime

# Create your views here.
def login(request):
    if request.method == 'POST':
        API_KEY = request.POST.get("login")
        API_SECRET = request.POST.get("password")

        # API_KEY = "test1@mail.com"
        # API_SECRET = "1qaz"
        try:
            dw = datawiz.DW(API_KEY, API_SECRET)
            client_data = dw.get_client_info()
            client_info = {}
            client_info['name'] = client_data['name']
            client_info['shops'] = client_data['shops']
            client_info['date_from'] = client_data['date_from'].strftime("%d. %B %Y")
            client_info['date_to'] =client_data['date_to'].strftime("%d. %B %Y")

            df_turnover = dw.get_products_sale(by=["turnover"], date_from = datetime.date(2015, 11, 17),\
                                                                     date_to = datetime.date(2015, 11, 18))
            turnover_from = round(df_turnover.sum(axis=1)[0], 2)
            turnover_to = round(df_turnover.sum(axis=1)[1], 2)
            turnover_difference = round(turnover_to - turnover_from, 2)
            turnover_percentage = round(turnover_difference / max(turnover_to, turnover_from) * 100, 2)
            data_turnover = {"turnover_from": turnover_from, "turnover_to": turnover_to, "turnover_difference": \
                        turnover_difference, "turnover_percentage": turnover_percentage}

            df_qty = dw.get_products_sale(by=["qty"], date_from=datetime.date(2015, 11, 17), \
                                                   date_to=datetime.date(2015, 11, 18))
            qty_from = round(df_qty.sum(axis=1)[0], 2)
            qty_to = round(df_qty.sum(axis=1)[1], 2)
            qty_difference = round(qty_to - qty_from, 2)
            qty_percentage = round(qty_difference / max(qty_to, qty_from) * 100, 2)
            data_qty = {"qty_from": qty_from, "qty_to": qty_to, "qty_difference": \
                        qty_difference, "qty_percentage": qty_percentage}

            df_receipts_qty = dw.get_products_sale(by=["receipts_qty"], date_from=datetime.date(2015, 11, 17), \
                                              date_to=datetime.date(2015, 11, 18))
            receipts_qty_from = round(df_receipts_qty.sum(axis=1)[0], 2)
            receipts_qty_to = round(df_receipts_qty.sum(axis=1)[1], 2)
            receipts_qty_difference = round(receipts_qty_to - receipts_qty_from, 2)
            receipts_qty_percentage = round(receipts_qty_difference / max(receipts_qty_to, receipts_qty_from) * 100, 2)
            data_receipts_qty = {"receipts_qty_from": receipts_qty_from, "receipts_qty_to": receipts_qty_to, \
                        "receipts_qty_difference": receipts_qty_difference, "receipts_qty_percentage": receipts_qty_percentage}

            average_check_from = round(turnover_from / receipts_qty_from, 2)
            average_check_to = round(turnover_to / receipts_qty_to, 2)
            average_check_difference =round(average_check_to - average_check_from, 2)
            average_check_percentage = round(average_check_difference /max(average_check_to, average_check_from) * 100, 2)
            data_average_check = {"average_check_from": average_check_from, "average_check_to": average_check_to, \
                     "average_check_difference": average_check_difference, "average_check_percentage": average_check_percentage}

            data_indicator = {"data_turnover": data_turnover, "data_qty": data_qty, "data_receipts_qty": data_receipts_qty,\
                                  "data_average_check": data_average_check}

            list_id_product = list(df_turnover)
            list_qty_from = list(df_qty.iloc[0])
            list_qty_to = list(df_qty.iloc[1])
            list_turnover_from = list(df_turnover.iloc[0])
            list_turnover_to = list(df_turnover.iloc[1])
            grow_sales = [(list_id_product[i], round(list_qty_to[i] - list_qty_from[i], 2), round(list_turnover_to[i] - \
                        list_turnover_from[i], 2)) for i in range(len(list_qty_from)) if list_qty_from[i] < list_qty_to[i]]
            fell_sales = [(list_id_product[i], round(list_qty_to[i] - list_qty_from[i], 2), round(list_turnover_to[i] - \
                        list_turnover_from[i], 2)) for i in range(len(list_qty_from)) if list_qty_from[i] > list_qty_to[i]]

            data = {"data_indicator": data_indicator, "grow_sales": grow_sales, "fell_sales": fell_sales}
            return render(request, "index.html", context={"client_info": client_info, "data": data})

        except:
            return render(request, "login.html")

    return render(request, "login.html")

