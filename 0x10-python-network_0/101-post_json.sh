#!/bin/bash
#request with json
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
