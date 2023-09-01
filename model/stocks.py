from marshmallow import Schema,fields


class stock():
    def __init__(self,present,reserved,type) -> None:
        self.present = present
        self.reserved = reserved
        self.type = type

class stock_schema(Schema):
    present = fields.Number()
    reserved = fields.Number()
    type = fields.String()