#!/bin/bash
#request allowed options
curl -sI "$1" -X OPTIONS -i | grep Allow: | cut -d " " -f 2-
