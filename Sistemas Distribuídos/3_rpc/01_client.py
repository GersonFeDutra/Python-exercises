# Importar biblioteca
import xmlrpc.client

# Definir servidor
SERVER_1 = xmlrpc.client.ServerProxy('http://10.0.84.179:21212')
SERVER_2 = xmlrpc.client.ServerProxy('http://10.0.84.199:21212')
SERVER_3 = xmlrpc.client.ServerProxy('http://10.0.84.198:21212')
SERVER_4 = xmlrpc.client.ServerProxy('http://10.0.84.202:21212')


def main(*_arg) -> None:
    # Chamar funções disponíveis no servidor
    #print(SERVER_1.add(2, 3))  # Returns 5
    #print(SERVER_2.add(2, 3))  # Returns 5
    #print(SERVER_3.add(2, 3))  # Returns 5
    print(SERVER_4.add(2, 3))  # Returns 5


if __name__ == '__main__':
    main()
