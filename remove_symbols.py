from code_tables import symbol_code_table, symbol_num_code

# Update symbol_code_table by storing the numbers corresponding to symbols
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
    # Move to the starting of the file
    instream.seek(0)
    # Give a memory address to a variable starting from 16
    var = 16
    while ins := instream.readline():
        ins = ins.strip()
        # If the line isn't a label declaration
        if ins[0] == "@":
            # If the A-instruction doesn't contain a symbol, move on
            if ins[1:].isnumeric():
                continue
            # Else store the variable address, if not already done
            elif ins[1:] not in symbol_code_table[0]:
                symbol_code_table[0].append(ins[1:])
                symbol_code_table[1].append(str(var)) 
                var +=1
    instream.close()

# Removes
def rem_symbols (in_file_name):
    update_tables (in_file_name)
    instream = open (in_file_name + "P.asm", "r")
    outstream = open (in_file_name + "L.asm", "w")

    while ins := instream.readline():
        ins = ins.strip()
        # If ins is an A-instruction
        if ins[0] == "@":
            # and does contain a symbol
            if ins[1:] in symbol_code_table[0]:
                # write the correpnding number after @
                outstream.write("@" + symbol_num_code(ins[1:]) + "\n")
            else : 
                # else write the instruction
                outstream.write(ins + "\n")
        # If it is a pseudo-command, don't write it
        elif ins[0] == "(":
            continue
        # Else if it is just a C-instruction, write it
        else :
            outstream.write(ins + "\n")

    instream.close()
    outstream.close()
    

