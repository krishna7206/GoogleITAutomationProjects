#!/usr/bin/env python3
import re
import csv
import sys
import operator
import string
per_user={}
error={}
log = sys.argv[1]
with open (log,"r") as file:
    line = file.readline()[0:]
    for line in file:
        username = re.search(r"\(([\w]*)\)",line)
        fullstring = username[1]
        if "INFO" in line:
            if fullstring not in per_user:
                per_user[fullstring] = [1,0]
            else:
                per_user[fullstring][0] += 1
        if "ERROR" in line:
            if fullstring not in per_user:
                per_user[fullstring] = [0,1]
            else:
                per_user[fullstring][1] += 1 
            e = re.search(r"ERROR: ([\w]*).* ",line)
            finstr = e.group(0)
            finstra = finstr.replace("ERROR","")
            if finstra not in error:
                error[finstra] = 1
            else:
                error[finstra] +=1
    sort_list = sorted(error.items(), key=operator.itemgetter(1),reverse=True)
    sort_list2 = sorted(per_user.items(),key=operator.itemgetter(0))
    #errorfinal = {sort_list[i]:sort_list[i+1] for i in range(0,len(sort_list)-1)}        
    with open("error_message.csv","w",newline="") as f:
        write = csv.writer(f)
        fields = ["Error","Count"]
        write.writerow(fields)
        write.writerows(sort_list)
         #f.write("Error,Keys\n")
         #for key in error.keys():
             #f.write("%s,%s\n"%(key,error[key]))
    with open("user_statistics.csv","w",newline="") as f1:
       
        f1.write("Username,INFO,ERROR\n")
        
        for i in range(0,len(sort_list2)):
            str1 = ','.join([str(elem) for elem in sort_list2[i][1]])
            str2 = sort_list2[i][0]
            str3 = str2+","+str1
            f1.write("%s,%s\n"%(str2,str1))
        
     
        
       
        
    