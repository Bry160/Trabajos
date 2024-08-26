import socket

class Server:

    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__connection = None
        self.__server = None

    def getHost(self):
        return self.__host

    def getPort(self):
        return self.__port

    def getConnection(self):
        return self.__connection

    def getServer(self):
        return self.__server

    def setHost(self, host):
        self.__host = host

    def setPort(self, port):
        self.__port = port

    def setConnection(self, connection):
        self.__connection = connection

    def setServer(self, server):
        self.__server = server

    def openConnection(self):
        self.setServer(socket.socket())
        self.getServer().bind((self.getHost(), self.getPort()))
        self.getServer().listen()

    def receiveData(self):
        my_conn, addr = self.getServer().accept()
        self.setConnection(my_conn)
        print("Conexión hecha desde: " + str(addr))

        while True:
            data = self.getConnection().recv(1024).decode()

            if not data:
                break

            data = str(data).upper()
            print("Desde el cliente: " + str(data))
            data = input("Escribe mensaje: ")
            self.getConnection().send(data.encode())

    def closeConnection(self):
        self.getConnection().close()


s = Server("127.0.0.1", 5001)
s.openConnection()
s.receiveData()
s.closeConnection()
