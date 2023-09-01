import requests
import configparser
import json
import pandas as pd

config = configparser.RawConfigParser()
config.read('../config.properties')
url = config.read('api_url')
report_detail_url = 'https://api-seller.ozon.ru/v1/report/info'


def get_stock_info(last_id,headers):
    url = "https://api-seller.ozon.ru/v3/product/info/stocks"
    request = {
        "filter": {
            "offer_id": [],
            "product_id": [],
            "visibility": "ALL"
        },
        "last_id": last_id,
        "limit": 100
    }
    response = requests.post(
        url, data=json.dumps(request), headers=headers)

    return response.json()['result']


def get_pricing_info(last_id,headers):
    url = "https://api-seller.ozon.ru/v4/product/info/prices"
    request = {
        "filter": {
            "offer_id": [],
            "product_id": [],
            "visibility": "ALL"
        },
        "last_id": last_id,
        "limit": 100
    }
    response = requests.post(
        url, data=json.dumps(request), headers=headers)
    return response


def get_analytic_date(start_date, end_date,headers):
    api_url = "https://api-seller.ozon.ru/v1/analytics/data"
    request = {
        "date_from": str(start_date).replace(' ', 'T'),
        "date_to": str(end_date).replace(' ', 'T'),
        "metrics": [
            "ordered_units",
            "revenue"
        ],
        "dimension": [
            "sku"
        ],
        "filters": [],
        "sort": [
            {
                "key": "ordered_units",
                "order": "DESC"
            }
        ],
        "limit": 1000,
        "offset": 0
    }
    response = requests.post(
        api_url, data=json.dumps(request), headers=headers)
    result = response.json()['result']['data']
    return result


def get_fbo_shippment_report(start_date, end_date, offset,headers):
    url = "https://api-seller.ozon.ru/v2/posting/fbo/list"
    request = {
        "dir": "ASC",
        "filter": {
            "since": str(start_date).replace(' ', 'T'),
            "status": "",
            "to": str(end_date).replace(' ', 'T')
        },
        "limit": 1000,
        "offset": offset,
        "translit": True,
        "with": {
            "analytics_data": False,
            "financial_data": True
        }
    }
    response = requests.post(
        url, data=json.dumps(request), headers=headers)
    result = response.json()['result']
    return result

def get_fbo_shippment_report(start_date, end_date, offset,headers):
    print("connecting for fbo shippment...")
    url = "https://api-seller.ozon.ru/v2/posting/fbo/list"
    request = {
        "dir": "ASC",
        "filter": {
            "since": str(start_date).replace(' ', 'T'),
            "status": "",
            "to": str(end_date).replace(' ', 'T')
        },
        "limit": 1000,
        "offset": offset,
        "translit": True,
        "with": {
            "analytics_data": False,
            "financial_data": True
        }
    }
    response = requests.post(
        url, data=json.dumps(request), headers=headers)
    result = response.json()['result']
    return result


def get_fbs_shippment_report(start_date, end_date, offset,headers):
    print("connecting for fbs shippment...")
    url = "https://api-seller.ozon.ru/v3/posting/fbs/list"
    request = {
        "dir": "ASC",
        "filter": {
            "since": str(start_date).replace(' ', 'T'),
            "status": "",
            "to": str(end_date).replace(' ', 'T')
        },
        "limit": 100,
        "offset": offset,
        "translit": True,
        "with": {
            "analytics_data": False,
            "financial_data": True
        }
    }
    response = requests.post(
        url, data=json.dumps(request), headers=headers)
    result = response.json()['result']
    return result

