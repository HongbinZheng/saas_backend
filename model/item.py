from model.total_model import total_model,total_model_schema
from model.stocks import stock,stock_schema
from marshmallow import post_load,Schema,fields


class item():
    def __init__(self, product_id, product_name, sales_amount, payout_amount, service_amount, delivered, not_delivered,sales_quantity,order_quantity,product_price,product_price_with_discount,commission_amount,reserved_stock,present_stock) -> None:
        self.product_id = product_id if product_id else 0
        self.product_name = product_name if product_name else None
        self.sales_amount = sales_amount if sales_amount else total_model(0,0,0)
        self.payout_amount = payout_amount if payout_amount else total_model(0,0,0)
        self.service_amount = service_amount if service_amount else total_model(0,0,0)
        self.delivered = delivered if delivered else total_model(0,0,0)
        self.not_delivered = not_delivered if not_delivered else total_model(0,0,0)
        self.sales_quantity = sales_quantity if sales_quantity else total_model(0,0,0)
        self.order_quantity = order_quantity if order_quantity else total_model(0,0,0)
        self.product_price,self.product_price_with_discount = product_price,product_price_with_discount
        self.present_stock = present_stock if present_stock else total_model(0,0,0)
        self.reserved_stock = reserved_stock if reserved_stock else reserved_stock
        self.commission_amount = commission_amount if commission_amount else total_model(0,0,0)


class item_schema(Schema):
    product_id = fields.String()
    product_name = fields.String()
    sales_amount = fields.Nested(total_model_schema())
    payout_amount = fields.Nested(total_model_schema())
    service_amount = fields.Nested(total_model_schema())
    delivered = fields.Nested(total_model_schema())
    not_delivered = fields.Nested(total_model_schema())
    sales_quantity = fields.Nested(total_model_schema())
    order_quantity =fields.Nested(total_model_schema())
    product_price = fields.Number()
    product_price_with_discount = fields.Number()
    commission_amount = fields.Nested(total_model_schema())
    present_stock = fields.Nested(total_model_schema())
    reserved_stock = fields.Nested(total_model_schema())