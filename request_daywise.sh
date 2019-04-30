#!/bin/bash

curl -d ' [{"userid":102,"year":2019 ,"month":5 ,"day":25}]' -H "Content-Type: application/json" -X POST http://35.221.107.96:12345/predict 


