#!/bin/bash
# Script: pilot.sh
# Purpose: select button and transmit RF signals on frequency 433

echo `sudo ./sendiq -s 250000 -f 433.9200e6 -t u8 -i $1`
