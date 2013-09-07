from django.conf.urls import patterns, url
	
from robot_control import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^tutorial/$', views.tutorial, name='tutorial'),
	url(r'^blockly/$', views.blockly, name='blockly'),
    	url(r'^quiz/$', views.quiz, name='quiz'),
	url(r'^joystick-status/$', views.joystick_status, name='joystick_status'),
	url(r'^RFID-status/$', views.RFID_status, name='RFID_status'),
	url(r'^movements/forward$',     views.forward,     name='movement_forward'),
	url(r'^movements/turn_left$',   views.turn_left,   name='movement_turn_left'),
	url(r'^movements/turn_right$',  views.turn_right,  name='movement_turn_right'),
	url(r'^movements/sensor_wall$', views.sensor_wall, name='movement_sensor_wall'),
)

