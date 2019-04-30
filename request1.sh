#!/bin/bash

curl -d ' [{"m":5 ,"y":2019},{"m":6, "y":2019},{"m":7, "y":2019}]' -H "Content-Type: application/json" -X POST http://localhost:5000/month
