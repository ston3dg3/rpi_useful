#!/bin/bash
# Script: monitor.sh
# Purpose: toggle between monitor and managed mode of given interface

echo "Try: sudo monitor.sh <interface> <mon/managed>"
echo "-------------------------------------------------"

case $1 in
	wlan0)
		echo "interface wlan0 selected";;
	wlan1)
		echo "interface wlan1 selected";;
	wlan2)
		echo "interface wlan2 selected";;
	*)
		echo "Wrong Input. Try: sudo monitor.sh <interface> <mon/managed>";;
esac

case $2 in
	mon)
		echo `sudo ip link set $1 down 2>&1`
		echo `sudo iw dev $1 set type monitor 2>&1`
		echo `sleep 0.2`
		echo `iwconfig > tempiwconfig.txt 2>&1`
		echo `sleep 0.2`
		if [ `grep -ic Monitor tempiwconfig.txt` -gt 0 ] ; then
			echo "Successfuly put interface $1 in monitor mode"
		else
			echo "Error: could not put interface $1 in monitor mode"
		fi;;
	managed)
		echo `sudo ip link set $1 up`
		echo `sudo iw dev $1 set type managed`
		echo `sleep 0.2`
		echo `iwconfig > tempiwconfig.txt 2>&1`
		echo `sleep 0.2`
		if [ `grep -q Monitor tempiwconfig.txt` ] ; then
			echo "Error: could not put interface $1 into managed mode!"
		else
			echo "Successfuly put interface $1 into managed mode"
		fi;;
	*)
		echo "Wrong input. Try: sudo monitor.sh <interface> <mon/managed>";;
esac
echo "-----------------------------------"
