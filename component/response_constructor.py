from decimal import *
from flask import jsonify


from component.api_contollor import *
from component.utils import *
from model.total_model import total_model
from model.item import item,item_schema
from model.financial_data import financial_data,financial_data_schema

def construct_fin_report(start_date, end_date, seller_id,ozonToken):
    items = {}
    ozon_clien_id, ozon_api_key = ozonToken.split('+')
    headers = {'Content-Type': 'application/json',
           'Api-key': ozon_api_key, 
           'Client-id': ozon_clien_id}
    get_stock_info_utils(items,headers)
    get_pricing_info_utils(items,headers)
    get_fbo_shippment_detail(start_date, end_date, items,headers)
    get_fbs_shippment_detail(start_date, end_date, items,headers)
    res_items = []
    total_sales_amount = 0
    total_payout_amount = 0
    total_sales_quantity = 0
    total_order_quantity = 0
    total_delivered = 0
    total_not_delivered = 0
    total_commission_amount = 0
    total_service_amount = 0
    for k, v in items.items():
        payout_amount = total_model(0, 0, 0)
        sales_amount = total_model(0, 0, 0)
        sales_quantity = total_model(0, 0, 0)
        order_quantity = total_model(0, 0, 0)
        delivered = total_model(0, 0, 0)
        not_delivered = total_model(0, 0, 0)
        commission_amount = total_model(0, 0, 0)
        service_amount = total_model(0, 0, 0)
        fbo_payout = v['fbo_payout'] if 'fbo_payout' in v else 0
        fbs_payout = v['fbs_payout'] if 'fbs_payout' in v else 0
        payout_total = addition(fbo_payout, fbs_payout)
        payout_amount = total_model(payout_total, fbo_payout, fbs_payout)
        total_payout_amount = addition(payout_total, total_payout_amount)

        fbo_sales_amount = v['fbo_sales_amount'] if 'fbo_sales_amount' in v else 0
        fbs_sales_amount = v['fbs_sales_amount'] if 'fbs_sales_amount' in v else 0
        sales_amount_total = addition(fbo_sales_amount, fbs_sales_amount)
        sales_amount = total_model(
            sales_amount_total, fbo_sales_amount, fbs_sales_amount)
        total_sales_amount = addition(
            total_sales_amount, sales_amount_total)
        fbo_sales_quantity = v['fbo_sales_quantity'] if 'fbo_sales_quantity' in v else 0
        fbs_sales_quantity = v['fbs_sales_quantity'] if 'fbs_sales_quantity' in v else 0
        sales_quantity_total = addition(
            fbo_sales_quantity, fbs_sales_quantity)
        sales_quantity = total_model(
            sales_quantity_total, fbo_sales_quantity, fbs_sales_quantity)
        total_sales_quantity = addition(
            sales_quantity_total, total_sales_quantity)

        fbo_order_quantity = v['fbo_order_quantity'] if 'fbo_order_quantity' in v else 0
        fbs_order_quantity = v['fbs_order_quantity'] if 'fbs_order_quantity' in v else 0
        order_quantity_total = addition(
            fbo_order_quantity, fbs_order_quantity)
        order_quantity = total_model(
            order_quantity_total, fbo_order_quantity, fbs_order_quantity)
        total_order_quantity = addition(
            total_order_quantity, order_quantity_total)

        fbo_shippment_delivered = v['fbo_shippment_delivered'] if 'fbo_shippment_delivered' in v else 0
        fbs_shippment_delivered = v['fbs_shippment_delivered'] if 'fbs_shippment_delivered' in v else 0
        delivered_total = addition(
            fbo_shippment_delivered, fbs_shippment_delivered)
        delivered = total_model(
            delivered_total, fbo_shippment_delivered, fbs_shippment_delivered)
        total_delivered = addition(total_delivered, delivered_total)

        fbo_shippment_not_delivered = v['fbo_shippment_not_delivered'] if 'fbo_shippment_not_delivered' in v else 0
        fbs_shippment_not_delivered = v['fbs_shippment_not_delivered'] if 'fbs_shippment_not_delivered' in v else 0
        not_delivered_total = addition(
            fbo_shippment_not_delivered, fbs_shippment_not_delivered)
        not_delivered = total_model(
            not_delivered_total, fbo_shippment_not_delivered, fbs_shippment_not_delivered)
        total_not_delivered = addition(
            total_not_delivered, not_delivered_total)

        fbo_commission_amount = v['fbo_commission_amount'] if 'fbo_commission_amount' in v else 0
        fbs_commission_amount = v['fbs_commission_amount'] if 'fbs_commission_amount' in v else 0
        commission_amount_total = addition(
            fbo_commission_amount, fbs_commission_amount)
        commission_amount = total_model(
             commission_amount_total, fbo_commission_amount, fbs_commission_amount)
        total_commission_amount = addition(
              commission_amount_total, total_commission_amount)

        fbo_service_total = 0
        if 'fbo_item_services' in v:
            for key, val in v['fbo_item_services'].items():
                fbo_service_total = addition(val, fbo_service_total)
        fbs_service_total = 0
        if 'fbs_item_services' in v:
            for key, val in v['fbs_item_services'].items():
                fbs_service_total = addition(val, fbs_service_total)
        service_amount_total = addition(
                fbo_service_total, fbs_service_total)
        service_amount = total_model(
                service_amount_total, fbo_service_total, fbs_service_total)
        total_service_amount = addition(
                total_service_amount, service_amount_total)
        res_item = item(k, None, sales_amount, payout_amount, service_amount, delivered, not_delivered,
                    sales_quantity, order_quantity, v['old_price'], v['price'], commission_amount,v['reserved_stock'],v['present_stock'])
        res_items.append(res_item)

        res = financial_data('Ozon',total_sales_amount,total_payout_amount,total_service_amount,total_delivered,total_not_delivered,total_sales_quantity,total_order_quantity,total_commission_amount,res_items)

    return financial_data_schema().dumps(res)
