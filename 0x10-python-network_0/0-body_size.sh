#!/bin/bash
curl -Is "$1" | grep -i Content-length | cut -f2 -d" "
