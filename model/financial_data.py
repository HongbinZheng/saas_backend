from marshmallow import Schema, fields

from model.total_model import total_model_schema,total_model
from model.item import item_schema

class financial_data():
    def __init__(self, platform, sales_amount, payout_amount, service_amount, delivered, not_delivered, sales_quantity, order_quantity,commission_amount,items) -> None:
        self.platform = platform if platform else None
        self.sales_amount = sales_amount if sales_amount else 0
        self.payout_amount = payout_amount if payout_amount else 0
        self.service_amount = service_amount if service_amount else 0
        self.delivered = delivered if delivered else 0
        self.not_delivered = not_delivered if not_delivered else 0
        self.sales_quantity = sales_quantity if sales_quantity else 0
        self.order_quantity = order_quantity if order_quantity else 0
        self.commission_amount = commission_amount 
        self.items = items

class financial_data_schema(Schema):
    platform = fields.String()
    sales_amount = fields.Number()
    payout_amount = fields.Number()
    service_amount = fields.Number()
    delivered = fields.Number()
    not_delivered = fields.Number()
    sales_quantity = fields.Number()
    order_quantity = fields.Number()
    commission_amount = fields.Number()
    items = fields.List(fields.Nested(item_schema()))