from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
    # Definição de funções


def adder(x, y):
    return x + y


def subtract(x, y):
    return x - y


def div(x, y):
    return x / y


def mul(x, y):
    return x * y


def main(*_arg) -> None:
    with SimpleXMLRPCServer(('10.0.84.203', 21212), requestHandler=RequestHandler) as server:
        server.register_introspection_functions() # init

        # Registrar funções
        server.register_function(adder, 'add')
        server.register_function(subtract, 'sub')
        server.register_function(div, 'div')
        server.register_function(mul, 'mul')

        # Iniciar servidor
        server.serve_forever()


if __name__ == '__main__':
    main()
