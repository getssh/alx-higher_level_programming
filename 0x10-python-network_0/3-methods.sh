#!/bin/bash
#get allowed methods form server
curl -sIL "$1" -X OPTIONS | grep -i Allow | cut -d " " -f2-
