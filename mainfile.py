FILE_NAME = '/home/cameron/local_copy.log'

# Use open() to get a filehandle that can access the file
fh = open(FILE_NAME)

# Loop through the file 
for line in fh:
  if re.match("1995
  print(line)
