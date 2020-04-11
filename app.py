# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import psycopg2
import pandas as pd

app = Flask(__name__)
CORS(app)
api = Api(app)

# Require a parser to parse our POST request.
parser = reqparse.RequestParser()
parser.add_argument("arg01")

# データベースの接続情報
connection_config = {
    'user': 'xxgvdlopjhsvsk',
    'password': '38078c4a27e141748248c1c42b0ec966549d95df7a51537eb55e96a426fd035b',
    'host': 'ec2-54-147-209-121.compute-1.amazonaws.com',
    'port': '5432', # なくてもOK
    'database': 'd2fj6i9l6jq4tu'
}


class MyApi(Resource):
    def post(self):
        print('func post')
        # hello
        print('- parse')
        args = parser.parse_args()
        val = args['arg01']
        val_val = val + ' ---> flask'

        # postgres
        print('- postgres')
        connection = psycopg2.connect(**connection_config)
        df = pd.read_sql(sql='SELECT * FROM hello_table;', con=connection)
        val_val = val_val + " --- df_colname: \n" + str(df)

        return {"after_api": val_val}


api.add_resource(MyApi, "/myapi")

if __name__ == "__main__":
    app.run('127.0.0.1', 5002, debug=False)
