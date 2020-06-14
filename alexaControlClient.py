import socket
import json
import iRobot as bot
import time

HOST = '192.168.0.108'  # The server's hostname or IP address
PORT = 11001        # The port used by the server

MV='MV'
MVS='MVS'
MVSO='MVSO'
MVL='MVL'
MVR='MVR'
MVB='MVB'
FDF='FDF'
FDL='FDL'
FDR='FDR'
FDHL='FDHL'
FDHR='FDHR'
HON='HON'
HOFF='HOFF'
HONDUR='HONDUR'
HOFFDUR='HOFFDUR'
FTEM='FTEM'
FHUM='FHUM'
FTEMHUM='FTEMHUM'
SNDPIC='SNDPIC'
SNDVID='SNDVID'
STARTAUTO='STARTAUTO'
STOPAUTO='STOPAUTO'
DANCESTART='DANCESTART'
DANCESTARTDUR='DANCESTARTDUR'
STOPALL='STOPALL'
EXITBOT='EXITBOT'


#Dummy json data
#{"action":"","timeStamp":1592130955041,"value":"","outDist":"20","outTemp":"","outHumid":""}

bot.startBot()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:      
        data = s.recv(2048)
        jsonData=json.loads(data)
        print(data)
        command=jsonData["action"]
        #Exit the program if command is Exit bot which is abbreviated as EXITBOT
        if command=='EXITBOT':
            print('Exiting program')
            break
        
        #implement switch case on commands:
        
        if command==MV:
            print('Move straight till obstacle is detected')
        elif command==MVS:
            print('Move straight untill obstable is detected or x seconds elapsed')
            duration=jsonData["value"]
            bot.moveStraightDur(duration)
        elif command==MVSO:
            print(command)
        elif command==MVL:
            print(command)
        elif command==MVR:
            print(command)
        elif command==MVB:
            print(command)
        elif command==FDF:
            print(command)
        elif command==FDL:
            print(command)
        elif command==FDR:
            print(command)
        elif command==FDHL:
            print(command)
        elif command==FDHR:
            print(command)
        elif command==HON:
            print(command)
        elif command==HOFF:
            print(command)
        elif command==HONDUR:
            print(command)
        elif command==HOFFDUR:
            print(command)
        elif command==FTEM:
            print(command)
        elif command==FHUM:
            print(command)
        elif command==FTEMHUM:
            print(command)
        elif command==SNDPIC:
            print(command)
        elif command==SNDVID:
            print(command)
        elif command==STARTAUTO:
            print(command)
        elif command==STOPAUTO:
            print(command)
        elif command==DANCESTART:
            print(command)
        elif command==DANCESTARTDUR:
            print(command)
        elif command==STOPALL:
            print(command)
        elif command==EXITBOT:
            print(command)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

