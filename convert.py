import mistletoe
import re

path = input()
in_path = "./md/" + path + ".md"
out_path = "./html/" + path + ".html"

with open(in_path, "r") as input_file:
    ipt = input_file.read()

md = mistletoe.markdown(ipt)

md = re.sub(r'<p>', r'<p style="margin-bottom: 3em">', md)
md = re.sub(r'<a href=(.*?)>', r'<a href=\1 target="blank">', md)

with open(out_path, "w") as output_file:
    output_file.write(md)
