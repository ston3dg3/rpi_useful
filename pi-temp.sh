#!/bin/bash
# Script: pi-temp.sh
# Purpose: display CPU and GPU temperature
# -------------------------------

cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"
echo "GPU => $(/opt/vc/bin/vcgencmd measure_temp | cut -d = -f2)"
echo "CPU => $((cpu/1000))'C"
