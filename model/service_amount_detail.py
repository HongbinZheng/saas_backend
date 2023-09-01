import datetime as dt

from marshmallow import Schema, fields

class service_amount_detail():
    def __init__(self,sale_commission,item_fulfillment,item_deliv_to_customer,direct_flow_trans,direct_flow_logistic) -> None:
        self.sale_comission = sale_commission if sale_commission else 0
        self.item_fulfillment = item_fulfillment if item_fulfillment else 0
        self.item_deliv_to_customer = item_deliv_to_customer if item_deliv_to_customer else 0
        self.direct_flow_trans = direct_flow_trans if direct_flow_trans else 0
        self.direct_flow_logistic = direct_flow_logistic if direct_flow_logistic else 0
    
class service_amount_detail_schema(Schema):
    sale_comission = fields.Decimal()
    item_fulfillment = fields.Decimal()
    item_deliv_to_customer = fields.Decimal()
    direct_flow_trans = fields.Decimal()
    direct_flow_logistic = fields.Decimal()