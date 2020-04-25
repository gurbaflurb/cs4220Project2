# CS 4220 Project 2
I wrote this program in python 3 and tested it with python 3.8

## Instructions
This program uses the python standard library. To run the programs you will need python 3 installed.

### TCP 
Start up a TCP server by navigating to the `servers` directory and running `python3 TCPserver.py` on linux and `py -3 TCPserver.py`. This will start a TCP server that will listen for inbound connections. Then in a different terminal you need to navigate to the clients directory and run `python3 TCPclient.py <ip address of server> TestUploadFile.pdf` on linux or `py -3 TCPclient.py <ip address of server> TestUploadFile.pdf`. See self tests below for examples.

### UDP
Start up a TCP server by navigating to the `servers` directory and running `python3 UDPserver.py <loss_percent>` on linux and `py -3 UDPserver.py <loss_percent>`. This will start a TCP server that will listen for inbound connections and set the chance to lose a packet to the loss_percent. Then in a different terminal you need to navigate clients directory and run `python3 UDPclient.py <ip address of server> TestUploadFile.pdf` on linux or `py -3 UDPclient.py <ip address of server> TestUploadFile.pdf`. See self tests below for examples.

## Self-tests
### TCP Transfer of TestUploadFile.pdf
![TCP Transfer Image](https://github.com/gurbaflurb/cs4220Project2/blob/master/img/image1.png)

### UDP Transfer of TestUploadFile.pdf
![UDP Transfer Image](https://github.com/gurbaflurb/cs4220Project2/blob/master/img/image2.png)

### UDP Transfer of TestUploadFile.pdf
![UDP Transfer Image loss of 5%](https://github.com/gurbaflurb/cs4220Project2/blob/master/img/image3.png)