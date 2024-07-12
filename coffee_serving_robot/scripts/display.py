import socket

ip_address = "100.11.10.112" #100.11.10.112

port = 1990

#while True:
number = input("Enter a number: ")

  #  if number == '9':
   #     break
    
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

number_bytes = str(number).encode()

udp_socket.sendto(number_bytes, (ip_address, port))

udp_socket.close()