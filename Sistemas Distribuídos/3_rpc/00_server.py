from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
    # Definição de funções


def adder_function(x, y):
    return x + y


def main(*_arg) -> None:
    with SimpleXMLRPCServer(('localhost', 21212), requestHandler=RequestHandler) as server:
        server.register_introspection_functions() # init

        # Registrar funções
        server.register_function(adder_function, 'add')

        # Iniciar servidor
        server.serve_forever()


if __name__ == '__main__':
    main()
