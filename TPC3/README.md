# TPC3: Conversor de Markdown para HTML

## Autor

- Pedro Pacheco
- A61042

## Resumo

O objectivo é criar um pequeno conversor de MarkDown para HTML capaz de converter os seguintes elementos:

- Cabeçalhos
- Palavras a negrito
- Palavras em itálico
- Listas numberadas
- Hiperligações URL
- Imagens

## Execução do programa
Para compilar o ficheiro **tpc3.py** é necessário que haja no mesmo directório de compilação um ficheiro chamado **test.md** com o *Markdown* que se pretende converter.

## Resolução

O programa começa por ler o ficheiro de *input* para uma *string* que é passada à função **md_to_html**. 
Esta função é responsável por converter as linhas do arquivo Markdown para linhas correspondentes em HTML. Ela percorre cada linha do arquivo Markdown e verifica o seu formato, aplicando, com uso das funções da biblioteca **re**, as conversões necessárias para HTML.

Exemplo de *input* em Markdown para palavras em itálico
    
        This is an *example* of words in *italic*

Usando a função **sub** da biblioteca mencionada
    
        re.sub(r"(\*)(.+?)(\*)", r"<i>\2</i>", output, flags = re.M)

Obtemos o seguinte *output*
    
        This is an <i>example</i> of words in <i>italic</i>

A *string* devolvida pela função **md_to_html** é depois passada à função **create_html** que a injecta no meio de um *template* de HTML.

A *string* final é depois escrita num ficheiro de *output* chamado **output_html.html**.