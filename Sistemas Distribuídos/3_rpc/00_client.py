# Importar biblioteca
import xmlrpc.client

# Definir servidor
SERVER = xmlrpc.client.ServerProxy('http://localhost:21212')


def main(*_arg) -> None:
    # Chamar funções disponíveis no servidor
    print(SERVER.add(2, 3))  # Returns 5


if __name__ == '__main__':
    main()
