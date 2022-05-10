#!/usr/bin/python3 -u
'''
********************************************************************
// OTT EcoLog 800 data receiver -> MQTT
// v0.1 CRCC - Pablo 02/2022
********************************************************************
'''
import paho.mqtt.client as mqtt
import ssl
from datetime import datetime
import json
import pymysql
import sys
import re

# MQTT Settings 
MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_Topic = "piezos/"
MQTT_username = "XXXXXX"
MQTT_password = "XXXXXXXXXX"

#DB Settings
DB_host="localhost"
DB_user="root"
DB_password="Io20xjh12"

print ("Content-Type: text/plain\r\n")

# Subscribe
def on_connect(client, userdata, flags, rc):
  mqttc.subscribe(MQTT_Topic, 0)

#print(datetime.now().strftime('%m/%d/%Y %H:%M:%S'))
dt=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') # Mysql Format UTC for DB
        # EN base de datos almacenamos en UTC y luego al visualizar # # mostramos la hora correcta (como en Grafana)
        # dt=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

def on_subscribe(mosq, obj, mid, granted_qos):
  pass

#def on_disconnect(client, userdata, rc):
#  print("client disconnected ok")
   
# MAIN ######################

#print("\nSTART   " + datetime.now().strftime('%m/%d/%Y %H:%M:%S') )

args=sys.stdin.read().split('\n')

f = open("debug.txt","a")

mqttc = mqtt.Client()

# Assign event callbacks
#mqttc.on_message 	= on_message
mqttc.on_connect 	= on_connect
mqttc.on_subscribe 	= on_subscribe
#mqttc.on_disconnect = on_disconnect


# Connect
#mqttc.tls_set(ca_certs="ca.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
mqttc.username_pw_set(MQTT_username, MQTT_password)
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

#FORMAT after TAGS:
# STATION_ID SEID DATEFORM
# 082-450712 0001 YYYYMMDD
# YYYYMMDD;HHMMSS;XX.XX
# 20220223;190000;10.00
# 20220223;200000;10.00
#

args=[w.replace('\r','') for w in args]
station=sensor=dateformat=''
for line in args:
	if len(line) > 0:
		f.write(line+"\n")
		if line[0] == '<': 
			station=sensor=dateformat=''
			station		=line.partition('<STATION>')[2].partition('</STATION>')[0]
			sensor		=line.partition('<SENSOR>')[2].partition('</SENSOR>')[0]
			dateformat	=line.partition('<DATEFORMAT>')[2].partition('</DATEFORMAT>')[0]		
		elif station>'' and sensor>'' and dateformat>'':
			#print(station + "/" + sensor + "/" + dateformat)
			date	= line[0:8]
			hour	= line[9:15]
			value	= line[16:21]
			ret= mqttc.publish(MQTT_Topic+station+"/"+sensor+"/"+date+"/"+hour ,value) 
			#print("Values=" + date + " " + hour +" " +value)
			

f.close()			
mqttc.disconnect()

print ('Status: 200 OK\r\n')
print
