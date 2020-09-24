# Grab file from the internet
from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# progress bar
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

# open log
FILE_NAME = '/home/cameron/local_copy.log'

# Variables
total_requests = 0
totalyear_requests = 0

  
# I chose to skip the filehandle like you mentioned in the  slack example
for line in open(FILE_NAME):
  total_requests += 1
  if line.find("1994")!= -1:
    totalyear_requests += 1

    
    
    
# Print results
print("Total Log Requests Made in the Last Year: ", totalyear_requests)

print("Total Requests Made in Time Period of Log: ", total_requests)
    
# How many requests were made on each day?
#for line in open(FILE_NAME):

  

  
  
  
  
# How many requests were made on a week by week basis? per month?





# Percentage of requests not success full




# Percentage directed  elsewhere 




# what was the most requested file


# What was the least requested file
    
    

    

    
# Log split into 12 spereate files
awk 'BEGIN {
    split("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec ", months, " ")
    for (a = 1; a <= 12; a++)
        m[months[a]] = sprintf("%02d", a)
}
{
    split($4,array,"[:/]")
    year = array[3]
    month = m[array[2]]

    print > FILENAME"-"year"_"month".txt"
}' incendiary.ws-1995



