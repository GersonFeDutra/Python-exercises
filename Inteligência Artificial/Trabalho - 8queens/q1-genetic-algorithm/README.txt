
## Respostas

h) Rode o algoritmo 10 vezes com os parâmetros itmax = 100, tampop = 150, e txmut =
0.2. Quantas vezes, das 10 execuções, ele encontrou um indivíduo que consegue
resolver o problema das 8 rainhas?
**Resposta:** _8 vezes._ Veja a saída do [1° Teste](#1°-teste) abaixo.

j) Faça o mesmo processo, mantendo os parâmetros da questão anterior e alterando o
tamanho da população para tampop = 100 e tampop = 200. Aplicando o algoritmo
10 vezes em cada uma dessas configurações, quantas vezes ele encontra a solução?
**Resposta:** _6 vezes com 100 indivíduos e 9 vezes com 200._ Veja a saída dos [2°](#2°-teste) e [3°](#3°-teste) abaixo.

### Execuções

#### 1° Teste:

1° Execução:
id:1968, fit:28
⬛⬜⬛⬜⬛⬜👑⬜
⬜⬛⬜👑⬜⬛⬜⬛
⬛👑⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛👑⬛⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
gen:7, dna:(6, 3, 7, 2, 4, 8, 1, 5)

2° Execução:
id:4465, fit:28
⬛⬜⬛⬜👑⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜👑⬜⬛⬜⬛
⬛👑⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
⬛⬜⬛⬜⬛👑⬛⬜
⬜⬛👑⬛⬜⬛⬜⬛
gen:7, dna:(3, 5, 8, 4, 1, 7, 2, 6)

3° Execução:
id:6307, fit:28
⬛⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛⬜⬛⬜👑⬜⬛⬜
⬜⬛👑⬛⬜⬛⬜⬛
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
⬜👑⬜⬛⬜⬛⬜⬛
gen:6, dna:(5, 8, 4, 1, 3, 6, 2, 7)

4° Execução:
id:36599, fit:27
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛👑⬛👑⬛
⬛👑⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
⬛⬜⬛⬜⬛👑⬛⬜
⬜⬛⬜👑⬜⬛⬜⬛
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜⬛
gen:100, dna:(7, 3, 1, 6, 2, 5, 2, 4)

5° Execução:
id:39621, fit:28
⬛⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛⬜⬛⬜👑⬜⬛⬜
⬜⬛👑⬛⬜⬛⬜⬛
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
⬜👑⬜⬛⬜⬛⬜⬛
gen:10, dna:(5, 8, 4, 1, 3, 6, 2, 7)

6° Execução:
id:69899, fit:27
⬛⬜⬛👑⬛⬜👑⬜
⬜👑⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
⬜⬛⬜⬛⬜👑⬜⬛
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛👑⬛⬜⬛⬜⬛
⬛⬜⬛⬜👑⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜⬛
gen:100, dna:(5, 2, 6, 1, 7, 4, 1, 3)

7° Execução:
id:70693, fit:28
⬛⬜⬛⬜⬛⬜⬛👑
⬜👑⬜⬛⬜⬛⬜⬛
⬛⬜⬛👑⬛⬜⬛⬜
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜👑⬜
⬜⬛⬜⬛👑⬛⬜⬛
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
gen:3, dna:(4, 2, 7, 3, 6, 8, 5, 1)

8° Execução:
id:72307, fit:28
⬛⬜⬛⬜👑⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛⬜⬛👑⬛⬜⬛⬜
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
⬛⬜⬛⬜⬛👑⬛⬜
⬜👑⬜⬛⬜⬛⬜⬛
gen:5, dna:(4, 8, 5, 3, 1, 7, 2, 6)

9° Execução:
id:75312, fit:28
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
⬛👑⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛👑⬛⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜👑⬜
⬜⬛⬜👑⬜⬛⬜⬛
gen:9, dna:(6, 3, 1, 8, 4, 2, 7, 5)

10° Execução:
id:79483, fit:28
⬛⬜⬛⬜👑⬜⬛⬜
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
⬜👑⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜👑⬜
⬜⬛👑⬛⬜⬛⬜⬛
gen:13, dna:(2, 6, 8, 3, 1, 4, 7, 5)

#### 2° Teste:

1° Execução:
id:2069, fit:28
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛👑⬛⬜⬛
⬛👑⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
gen:10, dna:(5, 3, 1, 7, 2, 8, 6, 4)

2° Execução:
id:3390, fit:28
⬛⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛⬜⬛⬜👑⬜⬛⬜
⬜⬛👑⬛⬜⬛⬜⬛
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
⬜👑⬜⬛⬜⬛⬜⬛
gen:6, dna:(5, 8, 4, 1, 3, 6, 2, 7)

3° Execução:
id:4105, fit:28
⬛⬜⬛⬜👑⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
⬛⬜⬛👑⬛⬜⬛⬜
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
⬛👑⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
gen:4, dna:(4, 7, 5, 3, 1, 6, 8, 2)

4° Execução:
id:24399, fit:27
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
⬛⬜⬛⬜⬛👑⬛⬜
⬜👑⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛👑⬛👑⬛
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜👑⬜⬛⬜⬛
gen:100, dna:(7, 4, 1, 8, 6, 3, 6, 2)

5° Execução:
id:26697, fit:28
⬛⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛⬜⬛⬜👑⬜⬛⬜
⬜👑⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛👑⬛⬜
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
gen:11, dna:(6, 4, 7, 1, 3, 5, 2, 8)

6° Execução:
id:46799, fit:27
⬛⬜⬛👑⬛⬜👑⬜
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛👑⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
⬛⬜⬛⬜👑⬜⬛⬜
⬜👑⬜⬛⬜⬛⬜⬛
gen:100, dna:(2, 8, 3, 1, 7, 5, 1, 6)

7° Execução:
id:66899, fit:27
⬛👑⬛⬜⬛👑⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
⬛⬜⬛⬜👑⬜⬛⬜
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜👑⬜
⬜⬛👑⬛⬜⬛⬜⬛
gen:100, dna:(4, 1, 8, 5, 3, 1, 7, 2)

8° Execução:
id:67823, fit:28
⬛⬜⬛⬜👑⬜⬛⬜
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
⬜👑⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜👑⬜
⬜⬛👑⬛⬜⬛⬜⬛
gen:5, dna:(2, 6, 8, 3, 1, 4, 7, 5)

9° Execução:
id:69316, fit:28
⬛⬜⬛⬜⬛👑⬛⬜
⬜⬛👑⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜👑⬜
⬜👑⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
⬜⬛⬜⬛👑⬛⬜⬛
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜👑⬜⬛⬜⬛
gen:7, dna:(7, 4, 2, 8, 6, 1, 3, 5)

10° Execução:
id:89599, fit:27
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛👑👑⬜⬛
⬛👑⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜👑⬜
⬜⬛⬜👑⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
⬜⬛👑⬛⬜⬛⬜⬛
gen:100, dna:(1, 3, 8, 6, 2, 2, 5, 7)

#### 3° Teste:

1° Execução:
id:4239, fit:28
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛👑⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
⬛⬜⬛⬜👑⬜⬛⬜
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
gen:11, dna:(6, 3, 1, 7, 5, 8, 2, 4)

2° Execução:
id:6413, fit:28
⬛👑⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛⬜⬛⬜👑⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜👑⬜⬛⬜⬛
⬛⬜⬛⬜⬛👑⬛⬜
⬜⬛👑⬛⬜⬛⬜⬛
gen:5, dna:(5, 1, 8, 6, 3, 7, 2, 4)

3° Execução:
id:9798, fit:28
⬛⬜⬛👑⬛⬜⬛⬜
⬜👑⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
⬜⬛⬜⬛⬜👑⬜⬛
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛👑⬛⬜⬛⬜⬛
⬛⬜⬛⬜👑⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
gen:7, dna:(5, 2, 6, 1, 7, 4, 8, 3)

4° Execução:
id:10496, fit:28
⬛⬜⬛⬜⬛⬜👑⬜
⬜⬛⬜⬛👑⬛⬜⬛
⬛⬜👑⬜⬛⬜⬛⬜
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛👑⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
⬛👑⬛⬜⬛⬜⬛⬜
⬜⬛⬜👑⬜⬛⬜⬛
gen:2, dna:(4, 7, 3, 8, 2, 5, 1, 6)

5° Execução:
id:50999, fit:27
👑⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜👑⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
⬛👑⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
gen:100, dna:(1, 5, 7, 1, 3, 8, 6, 4)

6° Execução:
id:54771, fit:28
⬛⬜⬛⬜⬛👑⬛⬜
⬜⬛👑⬛⬜⬛⬜⬛
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
⬛⬜⬛👑⬛⬜⬛⬜
⬜👑⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜⬛⬜👑⬜
⬜⬛⬜⬛👑⬛⬜⬛
gen:9, dna:(3, 6, 2, 5, 8, 1, 7, 4)

7° Execução:
id:58586, fit:28
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛⬜⬛⬜👑⬜⬛⬜
⬜👑⬜⬛⬜⬛⬜⬛
gen:9, dna:(4, 8, 1, 5, 7, 2, 6, 3)

8° Execução:
id:62802, fit:28
⬛⬜⬛⬜👑⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛⬜⬛👑⬛⬜⬛⬜
👑⬛⬜⬛⬜⬛⬜⬛
⬛⬜👑⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛⬜👑
⬛⬜⬛⬜⬛👑⬛⬜
⬜👑⬜⬛⬜⬛⬜⬛
gen:11, dna:(4, 8, 5, 3, 1, 7, 2, 6)

9° Execução:
id:66543, fit:28
⬛⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
⬛⬜⬛⬜⬛⬜⬛👑
⬜⬛👑⬛⬜⬛⬜⬛
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛⬜⬛⬜👑⬜⬛⬜
⬜👑⬜⬛⬜⬛⬜⬛
gen:8, dna:(5, 8, 4, 1, 7, 2, 6, 3)

10° Execução:
id:69689, fit:28
⬛⬜⬛⬜⬛⬜⬛👑
⬜👑⬜⬛⬜⬛⬜⬛
⬛⬜⬛⬜👑⬜⬛⬜
⬜⬛👑⬛⬜⬛⬜⬛
👑⬜⬛⬜⬛⬜⬛⬜
⬜⬛⬜⬛⬜⬛👑⬛
⬛⬜⬛👑⬛⬜⬛⬜
⬜⬛⬜⬛⬜👑⬜⬛
gen:8, dna:(5, 2, 4, 7, 3, 8, 6, 1)
