import socket
import sys

def client_program():

    print('Enter ID as string: ')
    userid = input()
    if userid:
        while True:
            print('Enter 1: Send Mail, 2: Check Mail, 3: Exit Program ::')
            option = input()
            if option == '1':
                host = socket.gethostname()  # as both code is running on same pc
                port = 5000  # socket server port number

                client_socket = socket.socket()  # instantiate
                client_socket.connect((host, port))  # connect to the server

                print('Connected to Server')

                print('Enter Destination ID')
                destination = input()
                print('Enter Your Mail: ')
                message = input()
                tempframe = 'M To: ' + destination + ' From: ' + userid + ' Mail: ' + message
                templength = len(tempframe)
                if templength < 10:
                    framelength = '0' + str(templength)
                else:
                    framelength = str(templength)
                frame = str(framelength) + tempframe
                print('Frame To Send: ' + frame)
                client_socket.send(frame.encode())  # send message

                client_socket.close()  # close the connection
            elif option == '2':
                host = socket.gethostname()  # as both code is running on same pc for test
                port = 5000  # socket server port number

                client_socket = socket.socket()  # instantiate
                client_socket.connect((host, port))  # connect to the server

                print('Connected to Server')
                tempmessage = "C From: "+ userid
                templength = len(tempmessage)
                if templength < 10:
                    message = '0' + str(templength) + tempmessage
                else:
                    message = str(templength) + tempmessage
                print('Frame to Send: ' + message)
                client_socket.send(message.encode())  # send message
                listmail = []
                checkifmail = 0
                while True:
                    data = client_socket.recv(1024).decode()
                    if data == 'stop':
                        if checkifmail != 1:
                            print('No New Mail')
                        break
                    else:
                        checkifmail = 1
                        print('Frame Recieved: ' + data)
                        listmail.append(data.split(' ', 1)[1])
                if checkifmail != 0:
                    mailfinal = listmail.pop()
                    print('Email Recieved: ' + mailfinal)
                    while listmail:
                        mailfinal = listmail.pop()
                        print('Email Recieved: ' + mailfinal)


                client_socket.close()  # close the connection
            elif option == '3':
                sys.exit()
            else:
                print('Invalid Option')

    else:
        print('Invalid Username ID, Avoid Entering Blank Usernames or Usernames with Numbers at Start')

if __name__ == '__main__':
    client_program()