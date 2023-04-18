import os 
import re


encoding_match = re.compile(r"localparam \[31:0\] ([A-Z_]*).*= (32'b[01?]+);")

fo = open("decoder.v","w")

with open("./riscv-opcodes/inst.sverilog") as fs :
    for line in fs.readlines():
        line = line.strip()
        code = encoding_match.findall(line)
        if len(code) > 0:
            code = code[0]
            vcoding = f"wire inst_{code[0]} = (inst == {code[1]});\n"
            fo.write(vcoding)
            print(vcoding,end='')
