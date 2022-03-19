from preprocessing import pre
from conversion import assemble
from os import remove
from remove_symbols import rem_symbols

# Taking the name of the file as input, for example foo.asm
in_file_name = input()

# Now in_file_name becomes just foo
in_file_name = in_file_name[: len(in_file_name) - 4]

# Removing whitespaces and comments
pre (in_file_name)

# Removing symbols and substituting approptiate numbers
rem_symbols (in_file_name)

# Doing the conversion
assemble (in_file_name)

# Delete extra files
remove(in_file_name + "P.asm")
remove(in_file_name + "L.asm")