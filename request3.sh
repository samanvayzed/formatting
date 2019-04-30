#!/bin/bash

curl -d ' [{"w":5 ,"y":2019},{"w":6, "y":2019},{"w":7, "y":2019}]' -H "Content-Type: application/json" -X POST http://localhost:5000/week
