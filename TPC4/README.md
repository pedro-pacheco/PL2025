# TPC4: Analisador Léxico para uma Linguagem de Query

## Autor

- Pedro Pacheco
- A61042

## Resumo

O objectivo é criar um pequeno Analisador Léxico que possibilite compreender alguns *tokens* básicos de uma Linguagem de *Query*

Exemplo de *input*
    
        select ?nome ?desc where {
                ?s a dbo:MusicalArtist.
                ?s foaf:name "Chuck Berry"@en .
                ?w dbo:artist ?s.
                ?w foaf:name ?nome.
                ?w dbo:abst
        }  LIMIT 1000

## Execução do programa
Após a compilação do programa, basta inserir no *standard input* os comandos que deseja que o analisador léxico interprete. Quando quiser terminar insira o comando "EXIT"

## Resolução

A resolução do problema pedido começou por ser a identificação dos *tokens* necessários para o léxico seguido da estipulação das diferentes expressões regulares ou regras que definem cada um deles, assim como de outras regras para o bom funcionamento do programa.

Após isso, a simplicidade do programa é nada mais do que ler o *input* do utilizador e corrê-lo pela função **analyser** que fará a correspondência entre cada palavra inserida pelo utilizador e o seu significado no contexto do problema.