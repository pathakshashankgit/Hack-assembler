"""
Various tables for conversion, and functions to return the approriate values
"""

# For dest field
dest_code_table = [
   ["null", "M", "D", "MD", "A", "AM", "AD", "AMD"],
   ["000", "001", "010", "011", "100", "101", "110", "111"]
   ]

# For jump field
jump_code_table = [
   ["null", "JGT", "JEQ", "JGE", "JLT", "JNE", "JLE", "JMP"],
   ["000", "001", "010", "011", "100", "101", "110", "111"]
   ]

# For comp field
comp_code_table = [
    ["0", "1", "-1", "D", "A", "!D", "!A", "-D", "-A",
    "D+1", "A+1", "D-1", "A-1", "D+A", "D-A", "A-D", "D&A",
    "D|A", "M", "!M", "-M", "M+1", "M-1", "D+M", "D-M",
    "M-D", "D&M", "D|M"],
    ["0101010", "0111111", "0111010", "0001100", "0110000",
    "0001101","0110001", "0001111", "0110011", "0011111",
    "0110111","0001110","0110010","0000010","0010011",
    "0000111","0000000","0010101","1110000","1110001",
    "1110011","1110111","1110010","1000010","1010011",
    "1000111","1000000","1010101"]
]

symbol_code_table = [
   ["SP", "LCL", "ARG", "THIS", "THAT", "R0", "R1", "R2", 
   "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", 
   "R12", "R13", "R14", "R15", "SCREEN", "KBD"],
   ["0", "1", "2", "3", "4", "0", "1", "2", "3", "4", "5",
   "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
   "16384", "24576"]
]

def symbol_num_code(symb_str):
   ind = symbol_code_table[0].index(symb_str)
   return (symbol_code_table[1][ind])

# Returns the binary code of a dest string using the
# corresponding table
def dest_bin_code(dest_str):
   ind = dest_code_table[0].index(dest_str)
   return (dest_code_table[1][ind])

# Returns the binary code of a jump string using the
# corresponding table
def jump_bin_code(jump_str):
   ind = jump_code_table[0].index(jump_str)
   return (jump_code_table[1][ind])

# Returns the binary code of a comp string using the
# corresponding table
def comp_bin_code(comp_str):
   ind = comp_code_table[0].index(comp_str)
   return (comp_code_table[1][ind])
