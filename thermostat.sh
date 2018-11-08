#!/bin/bash

if [[ $# = 0 ]]; then
  echo "0 arguments"
elif [[ $# = 1 ]]; then
  if [ $1 = "on" ]; then
    python thermostatOn.py
  elif [ $1 = "off" ]; then
    python thermostatOff.py
  else
    re='^[0-9]+$'
    if ! [[ $1 =~ $re ]] ; then
      echo "error: Not a number" >&2; exit 1
    else
      python -c'import thermostatFunctions as thermostat; thermostat.setTemp($1)'
    fi
  fi
elif [[ $# = 2 ]] ; then
  echo "2 arguments"
else
  echo "invalid arguments"
fi
