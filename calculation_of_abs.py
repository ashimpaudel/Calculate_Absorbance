'''with open ("/Users/Ashim/Desktop/python/workfile.txt", "r") as myfile:
    data=myfile.read()
    
print data
for i in data:
    print i '''

# table1 - table2/ table3 - table 2

ask = raw_input("file name of ref: ")
f = open("/Users/Ashim/Desktop/python/" + ask, "r")
a = f.readlines()



ref = []
for string in a:
  
    index_j = 0
    comma_count = 0
    for j in string:
        index_j += 1
        
        if j == ',':
            comma_count += 1
            if comma_count == 2:
                
                slicing_point = index_j
                t = string[slicing_point:]
    ref.append(t)


# for second one
ask = raw_input("file name of sample: ")
f = open("/Users/Ashim/Desktop/python/" + ask, "r")
a = f.readlines()
sample = []
for string in a:
  
    index_j = 0
    comma_count = 0
    for j in string:
        index_j += 1
        
        if j == ',':
            comma_count += 1
            if comma_count == 2:
                
                slicing_point = index_j
                t = string[slicing_point:]
    sample.append(t)


# for third one
ask = raw_input("file name of bg: ")
f = open("/Users/Ashim/Desktop/python/" + ask, "r")
a = f.readlines()
bg = []
for string in a:
  
    index_j = 0
    comma_count = 0
    for j in string:
        index_j += 1
        
        if j == ',':
            comma_count += 1
            if comma_count == 2:
                
                slicing_point = index_j
                t = string[slicing_point:]
    bg.append(t)



# calculating the value
import math
list = []
for i in range(len(ref)):

           
    ans =  (float (ref[i]) - float (sample[i])) / (float(bg[i]) - float(sample[i]))
    base= 10  

    final_ans =  -1 * math.log(ans, base)
    #print "Your absorbance is " + str(final_ans * -1)
    list.append(final_ans)
print list
            
    
