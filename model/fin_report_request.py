from marshmallow import post_load,Schema,fields


class fin_report_request():
    def __init__(self,start_date,end_date,seller_id,ozon_token) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.seller_id = seller_id
        self.ozon_token = ozon_token

class fin_report_request_schema(Schema):
    start_date = fields.DateTime(format='%Y-%m-%dT%H:%M:%S.%f%z')
    end_date = fields.DateTime(format='%Y-%m-%dT%H:%M:%S.%f%z')
    seller_id = fields.Number()
    ozon_token = fields.String()

    @post_load
    def get_request(self,data,**kwargs):
        return fin_report_request(**data)