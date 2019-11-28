from konlpy.tag import Twitter
from collections import Counter
import sys,os


crawled_module = sys.argv[1]
crawled_name = sys.argv[2]
nlpy = Twitter()
folder_path = "data/"+crawled_module+"/"+crawled_name+"/"
data_file = open(folder_path+"data.txt", "r")

lines = data_file.read()
particles = nlpy.pos(lines)
list = []
for particle, tag in particles:
    if tag in ['Noun', 'Adjective']:
        list.append(particle)
count = Counter(list)
static_file = open(folder_path+"analyze.txt", '+w')

for n, c in count.most_common():

    if len(n) >=2:
        static_file.write(n+"__"+str(c)+"회\n")


# for tag in tag_count:
#     t.write(" {:<14}".format(tag['tag'])+"{}".format(tag['count']))
#     print(" {:<14}".format(tag['tag']), end='\t')
#
#     print("{}".format(tag['count']))