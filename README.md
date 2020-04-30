# CS 4220 Project 2
I wrote this program in python 3 and tested it with python 3.8

## Instructions
This program uses the python standard library. To run the programs you will need python 3 installed.

### TCP 
Start up a TCP server by navigating to the `servers` directory and running `python3 TCPserver.py` on linux and `py -3 TCPserver.py`. This will start a TCP server that will listen for inbound connections. Then in a different terminal you need to navigate to the clients directory and run `python3 TCPclient.py <ip address of server> TestUploadFile.pdf` on linux or `py -3 TCPclient.py <ip address of server> TestUploadFile.pdf`. See self tests below for examples.

### UDP
Start up a TCP server by navigating to the `servers` directory and running `python3 UDPserver.py <loss_percent>` on linux and `py -3 UDPserver.py <loss_percent>`. This will start a TCP server that will listen for inbound connections and set the chance to lose a packet to the loss_percent. Then in a different terminal you need to navigate clients directory and run `python3 UDPclient.py <ip address of server> TestUploadFile.pdf` on linux or `py -3 UDPclient.py <ip address of server> TestUploadFile.pdf`. See self tests below for examples.

### Notes
- The TCP section will only show that it connected to and downloaded the file from the server.
- The UDP section will list which packets it is missing after each connection. It will then re-request from the server the entire file and only save the packets it misses the first time around. It will then repeat this until it has the entire file. The loss percentage for the UDP section goes from 0-100, where on 100, no packets will be sent. I would not advise using this mode because you will only see error messages from the client saying it is missing all the packets.
- The images I have for the UDP section are out dated since they used my previous attempt (that worked based on luck) to download the file via UDP. This method was based on gather packets and keep writing them to the file until the file hash matches what was sent originally. This method was scrapped for the new method which includes a packet number for each packet of data being sent so that the client can rebuild the final message and determine if there are missing packets.

## Self-tests
### TCP Transfer of TestUploadFile.pdf
![TCP Transfer Image](https://github.com/gurbaflurb/cs4220Project2/blob/master/img/image1.png)

### UDP Transfer of TestUploadFile.pdf
![UDP Transfer Image](https://github.com/gurbaflurb/cs4220Project2/blob/master/img/image2.png)

### UDP Transfer of TestUploadFile.pdf
![UDP Transfer Image loss of 5%](https://github.com/gurbaflurb/cs4220Project2/blob/master/img/image3.png)