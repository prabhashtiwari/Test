import os
import sys
import json
import random
import string

def init():

    global SERVER_MAC 
    SERVER_MAC = "00:00:00:00:00:00"
    random_key = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]) 
    global CLIENT_ID
    CLIENT_ID = "TEST_"+str(SERVER_MAC)+"_"+ str(random_key)
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
    # Wildcard topic
    global TOPIC_IN
    TOPIC_IN = "Test/+/in"