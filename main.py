from flask import Flask,jsonify,request
from flask_cors import cross_origin

from model.fin_report_request import fin_report_request,fin_report_request_schema
from component.api_contollor import *
from component.response_constructor import *
from model.transaction_type import TransactionType
app = Flask(__name__)

@app.route('/')
def hellp_world():
    return 'Hello world'

@app.route('/fin_report',methods=['POST'])
@cross_origin()
def fin_report():
    request_data = fin_report_request_schema().load(request.get_json())
    print(request_data.start_date)
    print(request_data.end_date)

    res = construct_fin_report(request_data.start_date,request_data.end_date,request_data.seller_id,request_data.ozon_token)

    return res,200


if __name__ == '__main__':
    app.run()