# -*- coding: cp1252 -*-
from socket import *
from datetime import datetime
# needed for my timeout system

def main():
    # destination server is localhost
    serverName = 'localhost'
    # destination port number
    serverPort = 12000
    # number of pings starts at 0
    counter = 0;
    # prompt for user’s message
    message = raw_input('Input Lowercase Message')
    # while counter less than 10
    while counter < 10: 
        # add one to counter aka pings
        counter = counter +1
        # create socket
        mainSocket = socket(AF_INET,SOCK_DGRAM)
        try:
            mainSocket.settimeout(1.0)
            # timeout after 1 second
            startTime = datetime.now()
            # start time is current time at declaration
            mainSocket.sendto(message,(serverName, serverPort))
            # send the message
            modifiedMessage, serverAddress = mainSocket.recvfrom(1024)
            # modified message is the message it gets back
            endTime = datetime.now()
            # end time is current time at declaration
        except timeout:
            # if timeout
            print 'PING ' +str(counter)+' '+ str(startTime)+ ': Request timed out!' # print timeout mssg
            mainSocket.close()
            # close socket
        else:
            # else print PING num Start Time Returned Message and RTT
            print 'PING ' +str(counter)+' '+ str(startTime)+': Returned: ' + modifiedMessage + ' after '+ str(endTime-startTime)

    mainSocket.close()
    #close socket
    pass

if __name__ == '__main__':
    main()
