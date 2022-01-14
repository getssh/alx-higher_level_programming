#!/bin/bash
#getting contenet length
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
