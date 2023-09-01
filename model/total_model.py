from marshmallow import Schema,fields


class total_model():
    def __init__(self,total,FBO,FBS) -> None:
        self.total = total
        self.FBO = FBO
        self.FBS = FBS

class total_model_schema(Schema):
    total = fields.Number()
    FBO = fields.Number()
    FBS = fields.Number()