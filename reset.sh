echo 117 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio117/direction
echo 0 > /sys/class/gpio/gpio117/value
echo 1 > /sys/class/gpio/gpio117/value
#echo 60 > /sys/class/gpio/unexport
