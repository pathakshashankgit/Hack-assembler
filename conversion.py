"""
Take a .asm file with no symbols, no comments, no white-spaces and produce a corresponding
.hack file
"""
from code_tables import jump_bin_code, dest_bin_code, comp_bin_code

# Checking of an instruction is an A-instruction or a C-instruction.
# The function returns 1 for A-Instruction and and 0 for a C-instruction
def inst_type (instruction : str):
    if (instruction[0]=='@'):
        return 1
    else:
        return 0

# This function will take an A-instruction as a string and will
# return the corresponding binary code.
def a_to_bin(instruction : str):
    short_conv = format(int(instruction[1:]), "b")
    # We need a 16-bit number, so we add the extra zeroes needed
    # in the front
    extra_zeroes = "0" * (16 - len(short_conv))
    return(extra_zeroes + short_conv)

# A parsed C-instruction as a class, with various fields
class parsed_c_instructions:
    # Taking dest, comp, and jump to be null by default, although, comp will
    # certainly change when an object will be used because each C-instruction
    # has a computation component 
    def __init__(self, dest = "null", comp = "null", jump = "null"):
        self.comp = comp
        self.dest = dest
        self.jump = jump

# A parser takes a C-instruction and produces a parsed_c_instr as the object
def parser (c_instr : str):
    # Creating a parsed_c_instructions object
    p1 = parsed_c_instructions()
    # Checking if the dest is empty in the instruction
    if ('=' in c_instr):
        eq_index = c_instr.index('=')
        p1.dest = c_instr[:eq_index]
        c_instr = c_instr[eq_index + 1:]
    # Checking if the jump is empty in the instruction
    if (';' in c_instr):
        sem_col_index = c_instr.index(';')
        p1.jump = c_instr[sem_col_index + 1:]
        c_instr = c_instr[:sem_col_index]
    p1.comp = c_instr
    return p1

# This function will take a C-instruction and will return the corresponding
# binary code
def c_to_bin(c_instruction : str):
    parsed_ins = parser (c_instruction)
    dest_in_bin = dest_bin_code (parsed_ins.dest)
    comp_in_bin = comp_bin_code (parsed_ins.comp)
    jump_in_bin = jump_bin_code (parsed_ins.jump)
    return ("111"+ comp_in_bin + dest_in_bin + jump_in_bin)

def assemble (in_file_name):
    # Making file objects
    instream = open(in_file_name + "L.asm", "r")
    outstream = open(in_file_name + ".hack", "w")

    # Reading from the file, doing the conversion, and writing it to the output file
    while ins := instream.readline():
        # Remove "\n" from last
        ins = ins.strip()
        # Checking what kind of instruction it is and writing the 
        # corresponding binary code
        if inst_type(ins):
            outstream.write(a_to_bin(ins) + "\n")
        else:
            outstream.write(c_to_bin(ins) + "\n")

        instream.close
        outstream.close
