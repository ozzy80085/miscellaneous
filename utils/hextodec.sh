#!/bin/bash

#pipe some hex (case insensitive) into this program and the decimal value will be returned

read test
echo "ibase=16; ${test^^} "|bc
