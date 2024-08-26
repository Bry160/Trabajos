import socket

class Client:

    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__cliente = None

    def getHost(self):
        return self.__host

    def getPort(self):
        return self.__port

    def getCliente(self):
        return self.__cliente

    def setHost(self, host):
        self.__host = host

    def setPort(self, port):
        self.__port = port

    def setCliente(self, cliente):
        self.__cliente = cliente

    def openConnection(self):
        self.setCliente(socket.socket())
        self.getCliente().connect((self.getHost(), self.getPort()))

    def talkServer(self):
        message = input('Escribe mensaje: ')
        while message != 'q':
            self.getCliente().send(message.encode())
            data = self.getCliente().recv(1024).decode()

            print('Recibido desde servidor: ' + data)
            message = input("Escribe mensaje: ")

    def closeConnection(self):
        self.getCliente().close()

c = Client("127.0.0.1", 5001)
c.openConnection()
c.talkServer()
c.closeConnection()
