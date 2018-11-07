#!/bin/bash

if [[ $# = 0 ]]; then
  echo "0 arguments"
elif [[ $# = 1 ]]; then
  if [ $1 = "on" ]; then
    python thermostatOn.py
  elif [ $1 = "off" ]; then
    python thermostatOff.py
  else
    echo "invalid argument"
  fi
elif [[ $# = 2 ]]; then
  echo "2 arguments"
else
  echo "invalid arguments"
fi
