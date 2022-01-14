curl -sI 35.237.36.195 | grep -i Content-Length | awk '{print $2}'
