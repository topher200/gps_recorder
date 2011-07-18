#!/bin/bash

for i in $(seq 10); do
    adb pull /sdcard/sl4a/sensor_output_$i.json
done
