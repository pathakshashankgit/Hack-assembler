from code_tables import symbol_code_table, symbol_num_code

def update_tables(in_file_name):
    instream = open (in_file_name + "P.asm", "r")

    # Will count the line number
    lc = -1
    while ins := instream.readline():
        ins = ins.strip()
        # If the line is a label declaration
        if ins[0] == '(':
            symbol_code_table[0].append(ins[1: len(ins) - 1])
            symbol_code_table[1].append(str(lc + 1))
            continue
        else:
            lc +=1
    instream.seek(0)
    # Give a memory address to a variable starting from 16
    var = 16
    while ins := instream.readline():
        ins = ins.strip()
        # if the line isn't a label declaration
        if ins[0] == "@":
            if ins[1:].isnumeric():
                continue
            elif ins[1:] not in symbol_code_table[0]:
                symbol_code_table[0].append(ins[1:])
                symbol_code_table[1].append(str(var)) 
                var +=1
    instream.close()

def rem_symbols (in_file_name):
    update_tables (in_file_name)
    instream = open (in_file_name + "P.asm", "r")
    outstream = open (in_file_name + "L.asm", "w")

    while ins := instream.readline():
        ins = ins.strip()
        if ins[0] == "@":
            if ins[1:] in symbol_code_table[0]:
                outstream.write("@" + symbol_num_code(ins[1:]) + "\n")
            else : 
                outstream.write(ins + "\n")
        elif ins[0] == "(":
            continue
        else :
            outstream.write(ins + "\n")

    instream.close()
    outstream.close()
    

