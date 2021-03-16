# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 17:21:48 2021

@author: SLENDERMAN

"""
import socket, threading

#Creating TCP connection
def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #TCPsock.settimeout(delay)

    try:

        TCPsock.connect((ip, port_number))
        output[port_number] = socket.getservbyport(port_number, 'tcp')

    except:

        output[port_number] = ''
        if("cse" not in ip):
             #print("error: host {} not exist".format(ip))
             pass

#Creating UDP connection
def UDP_connect(ip, port_number, delay, output):
    UDPsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )
    UDPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #UDPsock.settimeout(delay)
    try:

        UDPsock.connect((ip, port_number))
        output[port_number] = socket.getservbyport(port_number, 'udp')

    except:

        output[port_number] = ''
        if("cse" not in ip):
             #print("error: host {} not exist".format(ip))
             pass

# Scanning Ports
def scan_ports(host_ip, protocol,portlow, porthigh):


  try:

     print("scanning host={}, protocol={}, ports: {} -> {}".format(host_ip,protocol,portlow,porthigh))
     # To run TCP_connect concurrently
     threads = {}
     # For printing purposes
     output = {}
    # Spawning threads to scan ports
     if protocol in "tcp":

       for i in range(portlow,porthigh):
         t = threading.Thread(target=TCP_connect, args=(host_ip, i, 1, output))
         threads[i]=t

     elif protocol in "udp":

       for i in range(portlow,porthigh):
         t = threading.Thread(target=UDP_connect, args=(host_ip, i, 1, output))
         threads[i]=t

     # Starting threads
     for i in range(portlow,porthigh):
        threads[i].start()

     # Locking the main thread until all threads complete
     for i in range(portlow,porthigh):
        threads[i].join()

     # Printing listening ports from small to large
     for i in range(portlow,porthigh):
        if output[i] != '':
            print("port {}       open   : {}".format(i,output[i]))
  except:

      print("invalid protocol: "+protocol+". Specify tcp or udp")


# nain function. Program starts from main
def main():

    host_ip = input("Enter host IP: ")
    protocol = input("Enter the Protol Name: ")
    portlow =  int(input("Enter the port low number: "))
    porthigh = int(input("Enter the Protol high number: "))
    scan_ports(host_ip, protocol, portlow, porthigh)
    #scan_ports("localhost", "UDP".lower(),0, 1000)

if __name__ == "__main__":
    main()