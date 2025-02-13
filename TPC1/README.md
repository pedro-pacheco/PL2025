# TPC1: Somador on/off

## Autor

- Pedro Pacheco
- A61042

## Resumo

O objectivo é criar um programa em *Python* que, sem o uso de expressões regulares, encontre todas as sequências de dígitos num texto e que os vá somando de acordo com as seguintes regras:

1. Sempre que encontrar a *string* “__Off__” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado

2. Sempre que encontrar a *string* “**On**” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado e dígitos posteriores são somados ao acumulador

3. Sempre que encontrar o carácter “**=**”, o resultado da soma é colocado na saída

4. Este funcionamento termina quando é inserida a *string* "__***__"

## Resolução

A resolução deste problema passa pela implementação de três funções: **multisplit()**, **splits()** e **getNumber()**.

São inicialmente criados um acumulador de inteiros e uma *flag* que determina se o comportamento de soma deverá estar ligado ou não. Por omissão esta *flag* está com valor *True* e o acumulador inicializado a 0.

Para cada linha inserida pelo utilizador no standard input, é chamada a função **multisplit()** que, com a ajuda da auxiliar **splits()**, vai separar a *string* original numa lista de *strings* separadas pelos diversos delimitadores.

Assim por exemplo a *string* de *input*

    
        The 12 British officially recognise the 2nd battle's duration as being from 10 July until 31 October 1940=, which overlaps the period off large-scale night attacks known as the Blitz, that lasted from 7 September=1940 onwards to 11 May 1941=.
    

daria origem à seguinte lista de *strings* separadas da seguinte forma

    
        ['the 12 british ', 'off', "icially recognise the 2nd battle's durati", 'on', ' as being from 10 july until 31 october 1940', '=', ', which overlaps the period ', 'off', ' large-scale night attacks known as the blitz, that lasted from 7 september', '=', '1940 ', 'on', 'wards to 11 may 1941', '=', '.']
    

Esta lista será então iterada de forma a serem encontradas as *strings* "**on**", "**off**" ou "**=**" que determinarão se a *flag* de soma se altera para *False* (sempre que encontra "**off**") e portanto parar de somar ao acumulador, se a *flag* se mantém a *True* ou altera para *True* caso já tenha sido previamente alterada para *False*, ou se o valor do acumulador deverá ser impresso para o *standard output* (*string* "=").

Este comportamento permanecerá activo enquanto o utilizador não inserir a *string* "***", momento no qual o programa termina.

Como exemplo de funcionamento, o *input* acima mencionado teria como *output*

    1993
    1993
    3945

