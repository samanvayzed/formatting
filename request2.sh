#!/bin/bash

curl -d ' [{"d":1,"m":4, "y":2019}, {"d":3,"m":4, "y":2019}]' -H "Content-Type: application/json" -X POST http://localhost:5000/day


