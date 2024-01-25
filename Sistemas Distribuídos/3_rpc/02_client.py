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

# Importar biblioteca
import xmlrpc.client

# Definir servidor
SERVER = xmlrpc.client.ServerProxy('http://localhost:21212')


def main(*_arg) -> None:
    # Chamar funções disponíveis no servidor
    print(f'Connected to the server {SERVER.get_ip()}')
    SERVER.store('Hello')
    SERVER.store('World')
    SERVER.store(':D')
    print(f'Ending connection {SERVER.get_datetime()}')
    print(f'Stored messages:', *SERVER.get())


if __name__ == '__main__':
    main()
