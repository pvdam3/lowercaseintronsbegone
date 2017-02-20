import sys
infile=sys.argv[1]
outfile=infile+'_spliced.fasta'

handle=open(infile)
output=''
for line in handle.readlines():
	if line.startswith('>'):
		output+=line
	else:
		for letter in line:
			if letter.isupper():
				## only add uppercase letters to the output string:
				output+= letter
		output+='\n'

with open(outfile, 'w') as writer:
 	writer.write(output)