import socket
import json
import iRobot as bot
import time
import _thread

HOST = 'anilexa.com'  # The server's hostname or IP address
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


def sendMessage(s:socket.socket ,status,outMsg):
    json_repon=f'{"action":"PI_RESPONSE","timeStamp":{},"value":"{}","outMSG":"{}"}'.format(str(time.time()),status,outMsg)
    s.send(jsonData+'\n')
    
    

#Dummy json data
#{"action":"","timeStamp":1592130955041,"value":"","outDist":"20","outTemp":"","outHumid":""}

bot.startBot()
time.sleep(2)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        time.sleep(0.1)
        print("waiting for command from server")
        data = s.recv(1024)
        
        print("Received",data)
        jsonData=json.loads(data)
        print(data)
        command=jsonData["action"]
        #Exit the program if command is Exit bot which is abbreviated as EXITBOT
        if command==EXITBOT:
            print('Exiting program')
            bot.halt()
            break
        
        #implement switch case on commands:
        
        if command==MV:
            print('Move straight till obstacle is detected')
            intdur=3
            thread3=_thread.start_new_thread(bot.moveStraightDur,(intdur,))
            sendMessage(s,'success','moving ahead')
        elif command==MVS:
           
            #bot.moveStraightDur(int(duration))
        elif command==MVSO:
            print(command)
        elif command==MVL:
            print(command)
            print('Turnign left ')
            
            thread3=_thread.start_new_thread(bot.turnLeft,())
            sendMessage(s,'success','turning left')
            
        elif command==MVR:
            print(command)
            print('Turnign left ')
            thread3=_thread.start_new_thread(bot.turnRight,())
            sendMessage(s,'success','turning right')
            
        elif command==MVB:
            print(command)
            print('moving back ')
            thread3=_thread.start_new_thread(bot.aboutTurn,())
            sendMessage(s,'success','Turning Back')
        elif command==FDF:
            print(command)
            print('Finding distance ')
            bot.turnSensorByDegree(7)
            time.sleep(0.3)
            sendMessage(s,'success',str(bot.distance))
            
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
            bot.headlightOn()
            sendMessage(s,'success','head light is on')
            
        elif command==HOFF:
            print(command)
            bot.headlightOff()
            sendMessage(s,'success','head light is off')
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
            print('starting auto')
            thread3=_thread.start_new_thread(bot.run,())
            sendMessage(s,'success','starting automatic')
        elif command==STOPAUTO:
            print(command)
        elif command==DANCESTART:
            print(command)
        elif command==DANCESTARTDUR:
            print(command)
        elif command==STOPALL:
            print(command)
            bot.GLOBAL_STOP=False
            
            sendMessage(s,'success','stopping all')
        elif command==EXITBOT:
            print(command)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

