# Laboratório 10 de Python: Aventura na Amazônia

Décimo projeto para submissão em Python de MC102 (Algoritmos e Programação de Computadores), curso ministrado pela UNICAMP.

Dando continuidade aos projetos desenvolvidos nos laboratórios de MC102 (explicação no repositório [IniciandoEmPython](https://github.com/laratoledom/IniciandoEmPython/blob/main/README.md)), temos como proposta de desenvolvimento do código o seguinte problema:
_______________________________________________________________________________________________________________________________________________________________________

"A Floresta Amazônica é a maior floresta tropical do mundo, possuindo um bioma extremamente rico com inúmeras espécies de animais e plantas. Até os dias de hoje novas espécies vêm sendo descobertas e estudadas nessa região. 

Você se juntou a um grupo de pesquisa que está indo justamente procurar por um tipo particular de árvore presente apenas na Amazônia. Como você sabe programar em Python, sua tarefa será desenvolver um programa para rastrear o caminho sendo feito pelo grupo de pesquisa.

A região da floresta sendo explorada será representada por uma matriz 20x20. Você deve assumir que cada célula da matriz é quadrada e tem área de 1 km². O grupo irá partir de uma posição (i,j) e, para registrar o caminho sendo percorrido, você será informado(a) para qual direção o grupo vai andar (norte, sul, leste ou oeste, assumindo que o norte é para cima) e quantos quilômetros serão percorridos nessa direção (sem contar a célula atual). Além disso, você será informado(a) sempre que um exemplar da árvore sendo estudada for encontrado na região correspondente a célula atual.

A matriz estará inicialmente preenchida com o caractere '.'. Para marcar o caminho, você deve substituir o caractere '.' da posição inicial e de cada célula percorrida por '+'. Caso exista uma árvore de interesse, você deverá substituir o caractere '+' da posição atual por '#', indicando onde a árvore de interesse foi encontrada. Se você passar por uma posição onde uma árvore foi encontrada você deve manter o caractere '#'. Por exemplo, partindo da posição inicial (6,1) vocês andaram 4 km para o norte, 3 km para o leste, encontraram uma árvore de interesse, andaram 2 km para o sul e andaram 4km para o norte, essa parte da matriz deve ser preenchida da seguinte forma.

<b>. . . . + .<br>
. . . . + .<br>
. + + + # .<br>
. + . . + .<br>
. + . . + .<br>
. + . . . .<br>
. + . . . .<br>
. . . . . .</b><br><br>

Como entrada, o seu programa irá receber uma linha inicial com 2 inteiros i, j correspondentes a posição inicial (linha i e coluna j). Em seguida cada linha terá um dos seguintes formatos:

<b>•	N k indicando que vocês vão andar k quilômetros para o norte.<br>
•	S k indicando que vocês vão andar k quilômetros para o sul.<br>
•	L k indicando que vocês vão andar k quilômetros para o leste.<br>
•	O k indicando que vocês vão andar k quilômetros para o oeste.<br>
•	A indicando que uma árvore de interesse foi encontrada na célula atual.<br>
•	F indicando que vocês chegaram no fim do caminho.</b>

Como saída, o seu programa deve imprimir a matriz preenchida com o caminho no formato especificado."
____________________________________________________________________________________________________________________________________________________________________

<b>Observações:</b>
O arquivo foi executado através do PyCharm e no arquivo "testes" podem ser encontrados alguns exemplos de testes que verificam o código.

