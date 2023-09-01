import datetime as dt

from marshmallow import Schema, fields

class service_amount(object):
    def __init__(self,total,service_detail) -> None:
        self.total = total if total else 0
        self.service_detail = service_detail if service_detail else None    
    
    def set_service_detail(self,service_detail):
        self.service_detail = service_detail