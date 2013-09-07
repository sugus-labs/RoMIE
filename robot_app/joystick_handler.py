import threading
import pygame
import sys
import time
import os
#os.environ['SDL_VIDEODRIVER']='windib'

try:
	pygame.init()
	pygame.joystick.init()
	gamepad = pygame.joystick.Joystick(0)
	gamepad.init()
	pygame.display.init()

	EVENT_NONE    = 0
	EVENT_FORWARD = 1
	EVENT_LEFT    = 2
	EVENT_RIGHT   = 3
	EVENT_BACK    = 4

	CURRENT_VALUE = []
	CURRENT_VALUE_LOCK = threading.Lock()
	CURRENT_VALUE_EV   = threading.Event()

	def add_event(event):
		with CURRENT_VALUE_LOCK:
			CURRENT_VALUE.append(event)
			CURRENT_VALUE.append(EVENT_NONE)
			CURRENT_VALUE_EV.set()
			time.sleep(0.5)
			CURRENT_VALUE_EV.clear()

	def get_event():
		global CURRENT_VALUE

		with CURRENT_VALUE_LOCK:
			if len(CURRENT_VALUE):
				backup = CURRENT_VALUE[:]
				CURRENT_VALUE = []
				return backup

		CURRENT_VALUE_EV.wait(10)

		with CURRENT_VALUE_LOCK:
			if len(CURRENT_VALUE):
				backup = CURRENT_VALUE[:]
				CURRENT_VALUE = []
				return backup

		return []


	class JoystickHandler(threading.Thread):
		def run(self):

			add_event(EVENT_NONE)

			while( True ):
			    #Joystick Input
			    #print "Waiting for Joystick input..."


			    event = pygame.event.wait()
			    #print "got event"
			    #print repr(event)

			    #if event.type == pygame.JOYBUTTONDOWN:
			        #print "Button down"
			        #time.sleep(4)
			    #elif event.type == pygame.JOYBUTTONUP:
			        #print "Button up"
			    if event.type == pygame.JOYAXISMOTION:
			        #print "Joystick moved"
			        if event.axis == 0:
			            if event.value > 0.5:
			                add_event(EVENT_RIGHT)
			                #print "RIGHT"
			                #right()
			                #acknowledge_cmd()  
			            elif event.value < -0.5:
			                add_event(EVENT_LEFT)
			                #print "LEFT"
			                #left()
			                #acknowledge_cmd()
			        elif event.axis == 1:
			            if event.value < -0.5:
			                add_event(EVENT_FORWARD)
			                #print "FORWARD"
			                #forward()
			                #acknowledge_cmd()
			            elif event.value > 0.5:
	                                add_event(EVENT_BACK)
			        # time.sleep(1)
	                    pygame.event.clear()

	handler = JoystickHandler()
	handler.start()

except:
	print "Joystick not found!"