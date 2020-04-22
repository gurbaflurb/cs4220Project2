#!/usr/bin/python3
import socket
import sys

def main():
    port = 2248
    addr = '0.0.0.0'

    if(len(sys.argv) < 2):
        print(f'Usage: {sys.argv[0]} <loss_percent>\n')
        exit()