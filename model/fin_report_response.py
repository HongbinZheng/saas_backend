import datetime as dt

from marshmallow import Schema, fields


class fin_report_response():
    def __init__(self,start_date,end_date) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.data = []
    def set_date(self,data):
        self.data = data