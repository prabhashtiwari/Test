import os
import sys
import json
import random
import string

def init():

    global MAC 
    MAC = "00:00:00:00:00:00"
    random_key = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]) 
    global CLIENT_ID
    CLIENT_ID = "TEST_"+str(MAC)+"_"+ str(random_key)
    global SERVER_IP
    SERVER_IP = "server_ip"
    global SERVER_PORT
    SERVER_PORT = "1883"
    global MQTT_UNAM
    MQTT_UNAM = "mqtt_username"
    global MQTT_UPSK
    MQTT_UPSK = "mqtt_upsk"
    global VER 
    VER = "Ver1.1"
    global thread_flag
    thread_flag = ['True'] 
    global TOPIC_IN
    TOPIC_IN = "Test/"+str(MAC)+"/in"
    global TOPIC_OUT
    TOPIC_OUT = "Test/"+str(MAC)+"/out"
    # "Save csv data into array" 
    global SENSOR_DATA
    SENSOR_DATA=[]
    # "Save buffered data into array" 
    global BUFFERED_DATA
    BUFFERED_DATA=[]