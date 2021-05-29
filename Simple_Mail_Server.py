import socket
import re
import time


def server_program():
    #create Hash
    mail = dict()
    while True:
        # get the hostname
        host = socket.gethostname() #use system ip
        port = 5000  # initiate port no above 1024
        server_socket = socket.socket()  # get instance
        server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        print('Server Is Now Listening At Welcome Socket')
        server_socket.listen(2)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from Client at IP: " + str(address[0]) + ' and Port: ' + str(address[1]))
        data = conn.recv(1024).decode()
        print('Frame recieved: ' + data)
        if data[2] == 'M':  #store mail
            key = re.search('To: (.*) From:', data) # find destination from frame
            if key.group(1) in mail:
                mail[key.group(1)].append(data)
            else:
                templist = [data]
                mail[key.group(1)] = templist
            print('Message added to server: ' + str(mail[key.group(1)]))
        if data[2] == 'C': #output email
            keyword = 'From: '
            before_keyword, keyword, after_keyword = data.partition(keyword) #find username from frame
            if after_keyword in mail:
                while mail[after_keyword]:
                    message = mail[after_keyword].pop()
                    print('Frame Sent: ' + message)
                    conn.send(message.encode())
            time.sleep(1) #prevent sending 2 packets at same time overwhelming client
            ending = 'stop'
            conn.send(ending.encode())
            

        conn.close()  # close the connection


if __name__ == '__main__':
    server_program()