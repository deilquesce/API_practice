# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 13:16:17 2023

@author: Daniel Matthew
"""
# site name to access api 
# https://e163-2607-fea8-3ce0-40a0-1d4a-7c9d-3781-60d0.ngrok.io/user/?user=dan

from flask import *


import json, time
app= Flask(__name__)

#declare endpoint
@app.route('/', methods=['GET'])
def home_page():
    data_set = {
        'Page':'Home', 
        'Message': 'Successfully loaded homepage', 
        'Timestamp': time.time()
        }
    json_dump = json.dumps(data_set)
    return json_dump

#declare endpoint
@app.route('/user/', methods=['GET'])
def req_page():
    
    user_query = str(request.args.get('user')) #/user/?user=fafa
    
    data_set = {
        'Page':'Request', 
        'Message': f'Successfully loaded request page for {user_query}', 
        'Timestamp': time.time()
        }
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/runKNN/', methods=['GET']) # ?acc=90&rt=.2
def tst_page():
    # what numbers we need to pass
    passed_int = int(request.args.get('id')) #/runKNN/?id=10
    user_query = str(passed_int)
    
    
    # run through the algorithm here
    
    #return result as string
    res = str(user_query)
    
    data_set = {
        'Page':'Request',
        'Data Passed': f'{user_query}',
        'Result': f'{res}', 
        'Timestamp': time.time()
        }
    json_dump = json.dumps(data_set)
    return json_dump
    

if __name__ == '__main__':
    app.run(port=7777)




