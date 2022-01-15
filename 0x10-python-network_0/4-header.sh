#!/bin/bash
#adding custom header
curl -sfLH "X-School-User-Id: 98" "$1"
