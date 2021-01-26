frase: str = 'Curso em Vídeo Python'
lista: list = frase.split()

print(
f'''Analisando a String "{frase}":

Caractere na posição 3: {frase[3]}

Substrings:
Do 3° à 13° posição: {frase[3:13]}
Do primeiro caractere ate a 13° posição: {frase[:13]}
Da 1° até a 15° posição, de 2 em 2: {frase[1:15:2]}
Da 1° posição até o último caractere, de 2 em 2: {frase[1::2]}
Do primeiro ao último caractere de 2 em 2: {frase[::2]}

Análise:
Quantidade de caracteres: {len(frase)}
Quantidade de "o"s: {frase.count('o')}
Quantidade de "O"s: {frase.count('O')}
Quantidade de 'O's (maiúsculas ou minúsculas): {frase.upper().count("O")}

A substring "Curso" está presente na frase? {"Curso" in frase}
Em que índice "Curso" está posicionado na frase? {frase.find("Curso")}
E "vídeo"? {frase.find("vídeo")}
* -1 indica que a substring não existe na frase.

Lista com todas as palavras da frase:
{lista}
1° Palavra da frase (índice 0 da lista): '{lista[0]}'
4° Letra (índice 3) da 3° Palavra da frase (índice 2 da lista): '{lista[2][3]}'

Substituição:
"Python" -> "C++": {frase.replace('Python', 'C++')}
* Note que strings são imultáveis, logo a substituição de uma string indica que uma deve ser removida para gerar outra
* Portanto, a frase continua sendo: "{frase}"
* Exceto se o novo valor for atribuído na variável 'frase'
''')
