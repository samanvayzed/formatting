from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
from flask import request
from datetime import datetime

from flask_cors import CORS, cross_origin
from wtforms import TextField,TextAreaField, SubmitField
from wtforms.validators import Required
 
import sys
import os
import datetime
import calendar

import pickle

import json
# Preparing the Classifier
#monthwise

cur_dir = os.path.dirname('__file__')

#monthwise
regressor = pickle.load(open(os.path.join(cur_dir,
			'pkl_objects/modelmonths.pkl'), 'rb'))
model_columns = pickle.load(open(os.path.join(cur_dir,
			'pkl_objects/model_columnsm.pkl'),'rb')) 

#daywise
clf = pickle.load(open(os.path.join(cur_dir,
			'pkl_objects/modeldays.pkl'), 'rb'))
model_cold = pickle.load(open(os.path.join(cur_dir,
			'pkl_objects/model_columnsd.pkl'),'rb')) 

#weekwise
clfweek = pickle.load(open(os.path.join(cur_dir,
			'pkl_objects/modelweek.pkl'), 'rb'))
model_colw = pickle.load(open(os.path.join(cur_dir,
			'pkl_objects/model_columnsw.pkl'),'rb')) 

# Your API definition
app = Flask(__name__)

#for localhost
cors = CORS(app, resources={r"/": {"origins": "http://localhost:5000"}})

#daywise
@app.route('/day', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

#for gcp cloud
#cors = CORS(app, resources={r"/": {"origins": "https://jts-board.appspot.com/"}})

#@app.route('/', methods=['POST'])
#@cross_origin(origin='*',headers=['Content- Type','Authorization'])

def predict():
    #print(request)
    if clf:
        try:
            print("LLLLLLLLLLLLLLL")
            jsond = request.json
            queryd = pd.get_dummies(pd.DataFrame(jsond))
            queryd = queryd.reindex(columns=model_cold, fill_value=0)
            
            predictiond = list(clf.predict(queryd).astype("int64"))
            print(predictiond)
            


            print(queryd)
            copy_queryd = queryd.copy(deep=True)
            copy_queryd.columns = ['day','month','year']

            date_time = pd.to_datetime(copy_queryd[['day', 'month', 'year']])
            #date_time.columns = ['timestamp']
 
            date_time_df=pd.DataFrame(date_time, columns=["timestamp"])
            date_time_df['d'] = date_time_df['timestamp'].dt.dayofweek
            dnum=pd.DataFrame(date_time_df['d'])
            dname = dnum['d'].apply(lambda x: calendar.day_abbr[x])
            #df['weekday'] = df['Timestamp'].apply(lambda x: x.weekday())
            
            print("PPPPPPPPPPPPPP")
            #print(copy_queryd)
            #print(date_time_df)
            #print(dname)
            print("JJJJJJJJJJJJJJ")

            #print(queryd['m'])
            #mname = queryd['d'].apply(lambda x: calendar.day_abbr[x])
            #print(mname)
            #print(queryxid1)

            #mname=pd.DataFrame(queryd['d'])
            #mname=pd.DataFrame(mname)
        
            predictiond=pd.DataFrame(predictiond, columns=["s"])
            predictiond['s'] = predictiond['s'].apply(lambda x: x/1000)

            print(predictiond)
            con=pd.concat([dname,predictiond], axis=1)##################
            print(con)
            df=pd.DataFrame(con)###############


            df.set_index('d')['s'].to_dict()
            print(df)

            count = df.shape[0]
            #print(count)
   
            #print("LLLLLLLLLLOOO") 
            #print(df)
            #print("KKKKKKKKKKKKK")
 

            days = df['d'].tolist()
            sales = df['s'].tolist()

            #print("LLLLLLLLLLOOO")
            #print(months[1])
            #print(sales[1])
            #print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=days[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])


            #print(list_of_dicts)

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts)

            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")

    









            a = "cheese"        
            return json_dict    
            #return jsonify({'prediction': str(predictiond)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

#monthwise
@app.route('/month', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predmonth():
    #print(request)
    if regressor:
        try:
            json1= request.json
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_columns, fill_value=0)
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['m'] = copy_query1['m'].astype(str) + '月'
  

            print("JJJJJJJJJJJJJJJJJJ")
            print(query1)
            print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['m']
            #print(mname)
            #print(query1)
            
            mname=pd.DataFrame(mname)
            print(mname)
             
            prediction1 = (regressor.predict(query1).astype('int64'))
            #print(prediction1)
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["s"])
            
            prediction1['s'] = prediction1['s'].apply(lambda x: x/1000)

            con=pd.concat([mname,prediction1], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('m')['s'].to_dict()

            count = df.shape[0]
            #print(count)
   
            #print("LLLLLLLLLLOOO") 
            #print(df)
            #print("KKKKKKKKKKKKK")
 

            months = df['m'].tolist()
            sales = df['s'].tolist()

            print("PPPPPPPPPP")
            print(months)
            print(sales)
            print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=months[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])

            print("BBBBBBBBBBBBBB")
            print(list_of_dicts)
            print("LLLLLLLLLLLLLL")

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts,ensure_ascii=False)

            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")


            #dict(zip(df.m, df.s))
            
            #from collections import defaultdict
            #mydict = defaultdict(list)
            #for k, v in zip(df.m.values,df.s.values):
            #    mydict[k].append(v)
            #    mydict[k]="x"
            #    mydict[v]="v"

                
            #print("LLLLLLLLLLOOO") 
            #print(mydict)
            #print(k)
            #print(v)
            #print("LLLLLLLLLL")
            
            #df.groupby('name')[['value1','value2']].apply(lambda g: g.values.tolist()).to_dict()

                
            
            #return jsonify({'prediction': str(prediction1)})
            #t = "cheese"
            #return(t)
            return(json_dict)
            
        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')
  
    #weekwise
@app.route('/week', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predweek():
    #print(request)
    if clfweek:
        try:
            print("WWWWWWWWWWWWWWWWWWWWWWWWW")
            jsonw= request.json
            queryw = pd.get_dummies(pd.DataFrame(jsonw))
            queryw = queryw.reindex(columns=model_colw, fill_value=0)


            print(queryw)
            print("OOOOOOOOOOOOOOOOO")
            #print(query1['m'])
            #mname = queryw['w'].apply(lambda x: calendar.day_abbr[x])########
            #print(mname)
            #print(query1)
            mname=pd.DataFrame(queryw['w'])#########
            print(mname)
            print("WWWWWWWWWWWWWWWWWWWWWw")

            
            predictionw = (clfweek.predict(queryw).astype("int64"))
            
            #print("PPPPPPPPPPPPPP")
            #print(predictionw)
            #print("JJJJJJJJJJJJJJ")

            #print(prediction1)
            #print(prediction)
            predictionw=pd.DataFrame(predictionw, columns=["s"])##########
            print(predictionw)
            predictionw['s'] = predictionw['s'].apply(lambda x: x/1000)

            con=pd.concat([mname,predictionw], axis=1)##################
            print(con)
            df=pd.DataFrame(con)################


            df.set_index('w')['s'].to_dict()
            #print(df)



            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO") 
            #print(df)
            #print("KKKKKKKKKKKKK")


            weeks = df['w'].tolist()
            sales = df['s'].tolist()

            #print("LLLLLLLLLLOOO")
            #print(months[1])
            #print(sales[1])
            #print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=weeks[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])


            #print(list_of_dicts)

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts)

            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")

            return json_dict
            #return jsonify({'prediction weekwise': str(predictionw).splitlines()})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    app.run(debug=True)
