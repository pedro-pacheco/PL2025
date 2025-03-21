# TPC6: Analisador Sintático Recursivo Descendente

## Autor

- Pedro Pacheco
- A61042

## Resumo

O objectivo é desenvolver um analisador sintático recursivo descendente para avaliar expressões matemáticas simples

Pretende-se que seja capaz de calcular o valor correto de expressões matemáticas como as seguintes:

```
26/3**4-8+2*3
32.666666666666664

89+4*3-30/3/2
96
```

## Resolução

Em primeiro lugar, foi construído um analisador léxico para todos estes *tokens*.
Este *lexer* utiliza expressões regulares para reconhecer os *tokens* e converter os números para valores inteiros

Em seguida foi usado um analisador sintático - um *parser* que aplica o algoritmo Recursivo Descendente de modo a construir a árvore que avalia correctamente a expressão.

A gramática utilizada foi a seguinte:

```yacc
Exp : NUMBER ExpreCont

ExpreCont : '+' NUMBER ExpressCont
          | '-' NUMBER ExpressCont
          | '*' NUMBER ExpressCont
          | '/' NUMBER ExpressCont
```

À medida que o analisador sintático vai lendo correctamente os *tokens* vai adicionando-os a uma lista que no final é passada a uma função que faz o cálculo aritmético do valor da expressão.
