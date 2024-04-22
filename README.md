# combisensor
how to read the sensor data which gives the output through rs485 using python script
isme humne id set kiya hai sensors ka 1 and 2. so iska protocol for id-1 F4 01 01 F9, an for id-2 F4 02 01 FA, for id-3 F4 03 01 FB like this we are going. startbit- F4, secondbt- address, 3rd byte- command which is 01, 4th byte - from F9 to FFH. and the response which i am getting is F5 01 status the last bit.   status is 01 for car, 02 for no car and 03 for faulty sensor.
