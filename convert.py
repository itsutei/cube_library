import mistletoe
import re

in_path = "./md/clock.md"
with open(in_path, "r") as input_file:
    ipt = input_file.read()

md = mistletoe.markdown(ipt)

md = re.sub(r'<p>', r'<p style="margin-bottom: 3em">', md)

out_path = "./html/clock.html"

with open(out_path, "w") as output_file:
    output_file.write(md)
