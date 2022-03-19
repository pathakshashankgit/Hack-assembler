"""
Preprocessing a file to remove white-spaces, comments and empty lines
"""
def pre (in_file_name):
    instream = open (in_file_name + ".asm", "r")
    # If the name of the input file is foo.asm, the output file will be called fooP.asm
    # where the P stands for preprocessed
    outstream = open(in_file_name + "P.asm", "w")
    while ins := instream.readline():
        # Removing all comments
        if ('/' in ins):
            eol = ins.index('/')
            ins = ins[: eol]+"\n"
        # Removing all white spaces
        ins = ins.replace(" ","")
        # Removing all empty lines
        if (ins == "\n"):
            continue
        outstream.write(ins)
    instream.close
    outstream.close

