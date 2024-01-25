'''
Escreva um programa cliente/servidor com RPC onde:

Servidor deve implementar uma lista para armazenamento de mensagens;

- Disponibilizar funções remotas para:
   - Armazenar uma string na lista;
   - Recuperar lista de mensagens;
   - Retornar o IP do servidor;
   - Retornar data e hora do servidor no formato: YYYY-MM-DD HH:MM

Cliente
- Invocar as funções remotas do servidor implementado.

Testes
- O Cliente deve invocar os métodos da implementação de outro(a) colega;
- O servidor deve ser acessado por clientes em outras máquinas;

Enviar o link dos arquivos cliente.py e servidor.py de um repositório git. 
'''

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime
from typing import Callable
from sys import stderr


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


IP: str = '127.0.0.1'
PORT: int = 21212
messages: list[str] = []
rpc_methods: list[tuple[Callable, str]] = []

def rpc(func: Callable) -> None:
    global rpc_methods

    # print(func.__name__)
    rpc_methods.append((func, func.__name__))
    return func

# Definição de funções
@rpc
def store(s: str) -> None:
    '''Armazena a string na lista'''
    messages.append(s)

@rpc
def get() -> list[str]:
    '''Retorna a lista de mensagens'''
    return messages

@rpc
def get_ip() -> str:
    '''Retorna o IP do servidor'''
    return IP

@rpc
def get_datetime() -> str:
    '''Retorna a data e hora no formato YYYY-MM-DD HH:MM'''
    return datetime.now().strftime('%y-%m-%d %H:%M')

def register_all(server: SimpleXMLRPCServer) -> None:
    for method in rpc_methods:
        server.register_function(method[0], method[1])


def main(*_arg) -> None:

    with SimpleXMLRPCServer((IP, PORT), requestHandler=RequestHandler, allow_none=True) as server:
        server.register_introspection_functions() # init

        # Registrar funções
        register_all(server)

        # Iniciar servidor
        server.serve_forever()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\033[31m' 'Process interrupted' '\033[m', file=stderr)
