compile-TCP:
	@echo "Compiling C files for the TCP client and server!"
	gcc -static -O3 c++/TCPclient.c -o TCPclient
	gcc -static -O3 c++/TCPserver.c -o TCPserver

compile-UDP:
	@echo "Compiling C file for the UDP client and server!"
	gcc -static -O3 c++/UDPclient.c -o UDPclient
	gcc -static -O3 c++/UDPserver.c -o UDPserver