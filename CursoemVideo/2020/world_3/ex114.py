from urllib import request

# url: str = 'https://www.google.com.br'
url: str = 'https://www.pudim.com.br'

try:
    connection = request.urlopen(url)
except Exception as error:
    print(f'\033[31mConnection error: {error}\033[m')
else:
    print(f'\033[32mConnection established: {connection}\033[m')
    print(connection.read())
