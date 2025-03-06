import re

def create_html(input):
    output = f"<!DOCTYPE html>\n<html>\n<body>\n{input}</body>\n</html>"
    return output

def md_to_html(input):
    #headers
    output = re.sub(r"^# (.*)", r"<h1>\1</h1>", input, flags = re.M)
    output = re.sub(r"^## (.*)", r"<h2>\1</h2>", output, flags = re.M)
    output = re.sub(r"^### (.*)", r"<h3>\1</h3>", output, flags = re.M)

    #bolds and italics
    output = re.sub(r"(\*){2}(.+?)(\*){2}", r"<b>\2</b>", output, flags = re.M)
    output = re.sub(r"(\*)(.+?)(\*)", r"<i>\2</i>", output, flags = re.M)

    #lists
    #writing li tags
    output = re.sub(r"(?<=\n)(\d\. )(.*)", r"<li>\2</li>", output, flags = re.M)
    
    #writing ol tags
    output = re.sub(r'(\n<li>.+</li>)+', r'\n<ol>\g<0>\n</ol>', output, flags = re.M)

    #urls
    output = re.sub(r"(?<!\!)\[(.*)\]\((.*)\)", r'<a href="\2">\1</a>', output, flags = re.M)

    #images
    output = re.sub(r"\!\[(.*)\]\((.*)\)", r'<img src="\2" alt="\1"/>', output, flags = re.M)

    return output
    

def main():
    input_file = open("test.md", "r", encoding="utf-8")

    input_md = input_file.read()

    converted = md_to_html(input_md)

    html = create_html(converted)

    output_file = open("output_html.html", "w")

    output_file.write(html)

    #print(html)

    input_file.close()
    output_file.close()

if __name__ == "__main__":
    main()