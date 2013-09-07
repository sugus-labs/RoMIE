import sys
import time
import os
import subprocess
import webbrowser
import threading
import traceback

from django.http import HttpResponse
from django.shortcuts import render
from robot_control.models import Category, Question, Response
from django.core.mail import send_mail

import json

MAX_TIME = 180 # seconds
PORT = '8000'
GLOBAL_LOCK = threading.Lock()
tag = None

try:
    from robot_app.joystick_handler import get_event
    Joystick=True
except:
    Joystick=False
    print 'The joystick is not working'

# ############ -  Bluetooth Initialization  - ###############
try:
    import bluetooth #For GNU/Linux using PyBluez
    #import lightblue #For Mac OS X using lightblue
    #sys.path.append('/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC') #For Mac OS X using lightblue
    BT_name = "linvor"
    BT_address = '00:12:02:09:05:16'
    #nearby_devices = bluetooth.discover_devices()
    BT_port = 1
    #Client Socket
    client_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM) #For GNU/Linux using PyBluez
    #client_sock = lightblue.socket()
    port = client_sock.connect((BT_address, BT_port))
    BT_available=True
except:
    BT_available=False
    print 'No Bluetooth device is available'

def wait_ack(client_sock):
    total_received = "" 
    while 'ACK' not in total_received and 'NAK' not in total_received:
        total_received += client_sock.recv(1024)
    if 'NAK' in total_received:
        global popen
        popen.kill()
        #TODO BOMBAAAAAAAAAAA!!!!

    print repr(total_received)

    return total_received

def forward(request):
    if request.META.get('REMOTE_ADDR') not in ('127.0.0.1', 'localhost', '::1', '127.0.1.1'):
        return HttpResponse("INVALID_CLIENT_ADDRESS")
    client_sock.send('F')
    response = wait_ack(client_sock)
    return HttpResponse(response)

def turn_left(request):
    if request.META.get('REMOTE_ADDR') not in ('127.0.0.1', 'localhost', '::1', '127.0.1.1'):
        return HttpResponse("INVALID_CLIENT_ADDRESS")
    client_sock.send('L')
    response = wait_ack(client_sock)
    return HttpResponse(response)

def turn_right(request):
    if request.META.get('REMOTE_ADDR') not in ('127.0.0.1', 'localhost', '::1', '127.0.1.1'):
        return HttpResponse("INVALID_CLIENT_ADDRESS")
    client_sock.send('R')
    response = wait_ack(client_sock)
    print response 
    return HttpResponse(response)

def sensor_wall(request):
    if request.META.get('REMOTE_ADDR') not in ('127.0.0.1', 'localhost', '::1', '127.0.1.1'):
        return HttpResponse("INVALID_CLIENT_ADDRESS")
    client_sock.send('S')
    response = client_sock.recv(1024)
    #TODO: recibir lectura del sensor  
    #return HttpResponse(response)
    print "response ",response 
    return HttpResponse(response)

HEADER_CODE = """
import urllib2

OPENER = urllib2.build_opener(urllib2.ProxyHandler({}))

def forward():
    return OPENER.open("http://localhost:%(port)s/RoMIE/movements/forward").read()

def turn_left():
    return OPENER.open("http://localhost:%(port)s/RoMIE/movements/turn_left").read()

def turn_right():
    return OPENER.open("http://localhost:%(port)s/RoMIE/movements/turn_right").read()

def sensor_wall():
    response = OPENER.open("http://localhost:%(port)s/RoMIE/movements/sensor_wall").read()
    print "response second: ",response
    if "1" in response:
        return True
    else:
        return False
    #return response
    #return OPENER.open("http://localhost:%(port)s/RoMIE/movements/sensor_wall").read()


""" % { 'port' : PORT }

def move(direction):
    client_sock.send(direction)
    response = client_sock.recv(1024)
    
#     #print "direction: %s" % direction
#     #print "response: %s" % response
    string_tag_position = response.find("Tag")
    if string_tag_position != -1:
        in_tag_position = string_tag_position + 5
        out_tag_position = in_tag_position + 15
        tag = response[in_tag_position:out_tag_position]
        tag_full = tag.replace(" ", "")
        print tag_full
        if tag_full:
            global tag 
            tag= tag_full
            print "Tengo el TAG: ",tag
# #         os.chdir("/home/gustavo/Desktop")
# #        if tag_full == "4F005687C4":
# #            global tag 
# #            tag= tag_full
#             print "Tengo el TAG: ",tag
#         if tag_full == "4F00569F08":
#             global tag
#             tag = tag_full
# #             #webbrowser.open("http://127.0.0.1:8000/RoMIE/question_son_goku/", new = 0)
# #             subprocess.call(["java","-jar","Pregunton.jar","1"])
#         elif tag_full == "4F0088ABCB":
#             global tag
#             tag = tag_full
# #             #webbrowser.open("http://127.0.0.1:8000/RoMIE/question_one_piece/", new = 0)
# #             subprocess.call(["java","-jar","Pregunton.jar","2"])
#         elif tag_full == "50008967FC":
#             global tag
#             tag = tag_full
# #             #webbrowser.open("http://127.0.0.1:8000/RoMIE/question_digimon/", new = 0)
# #             subprocess.call(["java","-jar","Pregunton.jar","3"])
#         elif tag_full == "4F00568090":
#             global tag
#             tag = tag_full
# #             #webbrowser.open("http://127.0.0.1:8000/RoMIE/question_naruto/", new = 0)
# #             subprocess.call(["java","-jar","Pregunton.jar","4"])
# # #     #    return tag    
# # ############################################################
def select_random_questions():
    #categories_dict = {'Science':3, 'History':4, 'Sport':1, 'Culture':2, 'Entertainment':5, 'Geography':6}
    categories_dict = {'Sport':1, 'Culture':2}
    # SCIENCE 
    #filtered_questions_science = Question.objects.filter(category = categories_dict['Science'])
    #science_question = filtered_questions_science.order_by('?')[:1]
    # HISTORY
    #filtered_questions_history = Question.objects.filter(category = categories_dict['History'])
    #history_question = filtered_questions_history.order_by('?')[:1]
    # SPORT
    filtered_questions_sport = Question.objects.filter(category = categories_dict['Sport'])
    sport_question = filtered_questions_sport.order_by('?')[:1]
    # HUMANITIES
    filtered_questions_culture = Question.objects.filter(category = categories_dict['Culture'])
    culture_question = filtered_questions_culture.order_by('?')[:1]
    # ENTERTAINMENT
    #filtered_questions_entertainment = Question.objects.filter(category = categories_dict['Entertainment'])
    #entertainment_question = filtered_questions_entertainment.order_by('?')[:1]
    # GEOGRAPHY
    #filtered_questions_geography = Question.objects.filter(category = categories_dict['Geography'])
    #geography_question = filtered_questions_geography.order_by('?')[:1]
    #return science_question, history_question, sport_question, humanities_question, entertainment_question, geography_question
    return sport_question, culture_question 

#questions_enabled = [1,0,0,0,1,1]
#science_question, history_question, sport_question, humanities_question, entertainment_question, geography_question = select_random_questions()
sport_question, culture_question = select_random_questions()

def index(request):
    if request.method == 'GET':
        # Selection of 2 questions randomly
        print "SPORT: ", sport_question
        print "CULTURE: ", culture_question
        #global tag 
        #tag = "4F005687C4"
        return render(request, 'robot_control/index.html', {'sport_question': sport_question, 'culture_question': culture_question,})
    elif request.method == 'POST':
        received_command = request.REQUEST["command"]
        #print received_command
        if BT_available==True:
            move(received_command)
        else:
            print 'Cannot send command to the robot.'
        #tag = move(received_command)
        #if tag:
        #    print tag
        return HttpResponse("POST OK")

def joystick_status(request):
    if Joystick==True:
        return HttpResponse(json.dumps(get_event()))
    else:
        return HttpResponse('No Joystick')

def RFID_status(request):
    #send_mail('RFID-status Access', 'In this moment RoMIE is accessing to the URL: /RFID-status', 'RoMIE@weblab.deusto.es',['gustavo.martin@opendeusto.es'])
    mail_admins('RFID-status Access', 'In this moment RoMIE is accessing to the URL: /RFID-status', fail_silently=False, connection=None, html_message=None)
    global tag
    print "TAG: ",tag
    if tag:
        current_tag = tag
        tag = None
        return HttpResponse(current_tag)
    else:
        return HttpResponse('No RFID')
    
def tutorial(request):
    return render(request, 'robot_control/tutorial.html')

def blockly(request):
    if request.method == 'GET':
        return render(request, 'robot_control/blockly.html')
    elif request.method == 'POST':
        block_code = request.REQUEST["code"]
        
        if block_code == "stop":
            global popen
            popen.kill()
        else:
            launch_in_background(block_code) 

        return render(request, 'robot_control/blockly.html')

def launch_in_background(block_code):
    global t
    t = threading.Thread(target=exec_code, args = (block_code,))
    t.start()

def exec_code(code):
    final_code = HEADER_CODE + code
    try:
        with GLOBAL_LOCK:
            #print final_code
            #exec final_code
            open("executable.py", "w").write(final_code)
            #print "final_code ",final_code
            global popen
            popen = subprocess.Popen([sys.executable, "executable.py"])
            print "subprocess: ",popen.pid
            initial_time = time.time()
                
            while time.time() < (initial_time + MAX_TIME):
                if popen.poll() is not None:
                    break
                time.sleep(1)
            
            if popen.poll() is None:
                print "Killing in the name of", (time.time() - initial_time)
                sys.stdout.flush()
                popen.terminate()
                popen.kill()
    except:
        traceback.print_exc()
        return HttpResponse("OH, FUCK")


def quiz(request):
    return render(request, 'robot_control/quiz.html')

#######################################################################################################################################

