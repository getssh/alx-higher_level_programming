#!/bin/bash
#post with var
curl -X POST -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
