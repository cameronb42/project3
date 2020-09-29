# Grab file from the internet
from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# progress bar
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

# open log
FILE_NAME = 'local_copy.log'

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
    

  
  
  
  
# PART 2 OF THE PROJECT DUE THE 25TH  
# How many requests were made on each day?


  

  
  
  
  
# How many requests were made on a week by week basis? per month?





# Percentage of requests not success full
FILE_NAME = 'local_copy.log'
def ClientCachePercentage(FILE_NAME):
    Contents = open("FILE_NAME", "r").xreadlines(  )
    TRequests = 0
    CRequests = 0

for line in Contents:
        TRequests += 1
if line.split(" ")[8] == "441, 404":  # if server returned "not modified"
           CRequests += 1 
return (100*CRequests)/TRequests
  



# Percentage directed  elsewhere 
def ClientCachePercentage(local_copy.log):
    Contents = open("local_copy.log", "r").xreadlines(  )
    TotalRequests = 0
    CachedRequests = 0
for line in Contents:
        TotalRequests += 1
        if line.split(" ")[8] == "304":  
            CachedRequests += 1
return (100*CachedRequests)/TotalRequests



# what was the most requested file
import collections
FILE_NAME = open("/home/cameron/local_copy.log", "r")
clean_log=[]
for line in FILE_NAME:
    try:

        clean_log.append(line[line.index("GET")+4:line.index("HTTP")]) 
    except:
            pass
counter = collections.Counter(clean_log)
for count in counter.most_common(1):
    print(str(count[1]) + "	" + str(count[0]))
FILE_NAME.close()


# What was the least requested file
import collections
FILE_NAME = open("/home/cameron/local_copy.log", "r")
clean_log=[]
for line in FILE_NAME:
    try:

        clean_log.append(line[line.index("GET")+4:line.index("HTTP")]) 
    except:
            pass
counter = collections.Counter(clean_log)
for count in counter.least_common(1):
    print(str(count[1]) + "	" + str(count[0]))
FILE_NAME.close()
    

    

    
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
}' incendiary.ws-1994



