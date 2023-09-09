#!/bin/sh
export FLASK_APP=./main.py
flask --debug run -h 0.0.0.0 -p 443 --cert=adhoc