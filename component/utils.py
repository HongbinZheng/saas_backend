from decimal import *

from component.api_contollor import *
from model.transaction_type import TransactionType
from model.total_model import total_model


def get_fbo_shippment_detail(start_date,end_date,items,headers):
    fbo_shippment_list = get_fbo_shippment_report(start_date, end_date, 0,headers)
    fbo_shippment = fbo_shippment_list[:]
    offset = 0
    while len(fbo_shippment_list) != 0:
        offset += 1000
        fbo_shippment_list = get_fbo_shippment_report(
            start_date, end_date, offset,headers)
        if len(fbo_shippment_list) != 0:
            fbo_shippment = fbo_shippment_list[:] + fbo_shippment
    print(fbo_shippment)
    for i in fbo_shippment:
        for j in i['products']:
            offer_id = j['offer_id']
            sku = j['sku']
            if len(offer_id) == 0:
                offer_id = 'ozon_fbo_'+str(sku)
                items[offer_id] = {
                    "present_stock": 0,
                    "reserved_stock":0,
                     "price": j['price'],
                    "old_price": j['price']
                }
                # new_key = {i[offer_id]: {
                #     "present_stock": 0,
                #     "reserved_stock":0,
                #      "price": j['price']['price'],
                #     "old_price": j['price']['old_price']
                # }}
                # items.update(new_key)
            orders_quantity = 0
            for k in i['financial_data']['products']:
                if k['product_id'] == sku:
                    item = items[offer_id]
                    if 'fbo_payout' not in item:
                        new_key = {
                            'fbo_payout': 0,
                            'fbo_sales_amount': 0,
                            'fbo_sales_quantity': 0,
                            'fbo_order_quantity': 0,
                            'fbo_commission_amount':0,
                            'fbo_shippment_delivered': 0,
                            'fbo_shippment_not_delivered': 0
                        }
                        item.update(new_key)
                    item['fbo_payout'] = addition(k['payout'],item['fbo_payout'])
                    sales_amount = multiple(j['quantity'],k['price'])
                    item['fbo_sales_amount'] = addition(sales_amount,item['fbo_sales_amount'])
                    item['fbo_commission_amount'] = addition(item['fbo_commission_amount'],k['commission_amount'])
                    item['fbo_sales_quantity'] += j['quantity']
                    item['fbo_order_quantity'] += 1
                    if i['status'] == 'delivered':
                        item['fbo_shippment_delivered'] += j['quantity']
                    else:
                        item['fbo_shippment_not_delivered'] += j['quantity']

                    if 'fbo_item_services' not in item:
                        new_key = {'fbo_item_services': k['item_services']}
                        item.update(new_key)
                    else:
                        for key,v in k['item_services'].items():
                            item['fbo_item_services'][key] = addition(item['fbo_item_services'][key],v)

    
def get_fbs_shippment_detail(start_date,end_date,items,headers):
    fbs_shippment_list = get_fbs_shippment_report(start_date, end_date, 0,headers)
    fbs_shippment = fbs_shippment_list['postings'][:]
    offset = 0
    while fbs_shippment_list['has_next'] == True:
        offset += 100
        fbs_shippment_list = get_fbs_shippment_report(
            start_date, end_date, offset,headers)
        fbs_shippment = fbs_shippment_list['postings'][:] + fbs_shippment
    for i in fbs_shippment:
        for j in i['products']:
            offer_id = j['offer_id']
            sku = j['sku']
            orders_quantity = 0
            for k in i['financial_data']['products']:
                if k['product_id'] == sku:
                    item = items[offer_id]
                    if 'fbs_payout' not in item:
                        new_key = {
                            'fbs_payout': 0,
                            'fbs_sales_amount': 0,
                            'fbs_sales_quantity': 0,
                            'fbs_order_quantity': 0,
                            'fbs_commission_amount':0,
                            'fbs_shippment_delivered': 0,
                            'fbs_shippment_not_delivered': 0
                        }
                        item.update(new_key)
                    item['fbs_payout'] = addition(k['payout'],item['fbs_payout'])
                    sales_amount = multiple(j['quantity'], k['price']) 
                    item['fbs_sales_amount'] = addition(sales_amount,item['fbs_sales_amount'])
                    item['fbs_commission_amount'] = addition(item['fbs_commission_amount'],k['commission_amount'])
                    item['fbs_sales_quantity'] += j['quantity']
                    item['fbs_order_quantity'] += 1
                    if i['status'] == 'delivered':
                        item['fbs_shippment_delivered'] += j['quantity']
                    else:
                        item['fbs_shippment_not_delivered'] += j['quantity']

                    if 'fbs_item_services' not in item:
                        new_key = {'fbs_item_services': k['item_services']}
                        item.update(new_key)
                    else:
                        for key,v in k['item_services'].items():
                            item['fbs_item_services'][key] = addition(item['fbs_item_services'][key],v)

def get_stock_info_utils(items,headers):
    stock_info = get_stock_info('',headers)
    item_stock_list = stock_info['items'][:]
    while stock_info['total'] != 0:
        stock_info = get_stock_info(stock_info['last_id'],headers)
        item_stock_list = item_stock_list + stock_info['items'][:]
    #print(item_stock_list)
    for i in item_stock_list:
        present_total = 0
        fbo_present = 0
        fbs_present = 0
        reserved_total = 0
        fbo_reserved = 0
        fbs_reserved = 0
        for j in i['stocks']:
            if j['type'] == 'fbo':
                fbo_present=j['present']
                fbo_reserved=j['reserved']
                present_total = addition(present_total,fbo_present)
                reserved_total=addition(reserved_total,fbo_reserved)
            else:
                fbs_reserved=j['reserved']
                fbs_present=j['present']
                present_total = addition(present_total,fbs_present)
                reserved_total=addition(reserved_total,fbs_reserved)
        present_stock = total_model(present_total,fbo_present,fbs_present)
        reserved_stock = total_model(reserved_total,fbo_reserved,fbs_reserved)
        new_key = {i['offer_id']: {
            "present_stock": present_stock,
            "reserved_stock":reserved_stock
        }}
        items.update(new_key)

def get_pricing_info_utils(items,headers):
    pricing_info = get_pricing_info("",headers)
    price_list = pricing_info.json()['result']['items'][:]
    while pricing_info.status_code != 404:
        pricing_info = get_pricing_info(
            pricing_info.json()['result']['last_id'],headers)
        if pricing_info.status_code != 404:
            price_list = price_list + pricing_info.json()['result']['items'][:]
    for i in price_list:
        new_key = {
            "price": i['price']['price'],
            "old_price": i['price']['old_price']
        }
        items[i['offer_id']].update(new_key)

def addition(a,b):
    return float(Decimal(str(a))+ Decimal(str(b)))

def multiple(a,b):
    return float(Decimal(str(a))* Decimal(str(b)))