
import urllib2

OPENER = urllib2.build_opener(urllib2.ProxyHandler({}))

def forward():
    return OPENER.open("http://localhost:8000/RoMIE/movements/forward").read()

def turn_left():
    return OPENER.open("http://localhost:8000/RoMIE/movements/turn_left").read()

def turn_right():
    return OPENER.open("http://localhost:8000/RoMIE/movements/turn_right").read()

def sensor_wall():
    response = OPENER.open("http://localhost:8000/RoMIE/movements/sensor_wall").read()
    print "response second: ",response
    if "1" in response:
        return True
    else:
        return False
    #return response
    #return OPENER.open("http://localhost:8000/RoMIE/movements/sensor_wall").read()


for count in range(100):
  if sensor_wall():
    turn_left()
  else:
    forward()
    turn_right()
    if sensor_wall():
      turn_left()
