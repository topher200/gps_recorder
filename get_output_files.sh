#!/bin/bash

for i in $(seq 20); do
    adb pull /sdcard/sl4a/gps_output_$i.json
done
