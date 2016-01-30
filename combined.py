#!/usr/bin/env python
import os
import numpy
import matplotlib.pyplot as plt
from Tkinter import *
import tkFileDialog as filedialog
import FileDialog

root = Tk()
root.withdraw()
try:
    print "Select the heated sample"
    ask = filedialog.askopenfilename(title = 'Heated_Sample; Simply press close button if it is not heated experiment')
    f = open( ask, "r")
    a = f.readlines()
    sample = []
    for string in a:
      
        index_j = 0
        comma_count = 0
        for j in string:
            index_j += 1
            
            if j == ',':
                comma_count += 1
                if comma_count == 1:
                    
                    slicing_point = index_j
                    t = string[slicing_point:]
        sample.append(t)

    print "select the reference: "
    ask = filedialog.askopenfilename(title = 'Reference: Select the reference')
    f = open( ask, "r")
    a = f.readlines()

    g = open("absorbance.txt", "w")
    h = open("Energy.txt", "w")

    ref = []
    for string in a:
      
        index_j = 0
        comma_count = 0
        for j in string:
            index_j += 1
            
            if j == ',':
                comma_count += 1
                if comma_count == 1:
                    
                    slicing_point = index_j
                    t = string[slicing_point:]
        ref.append(t)


    print "Select the background ( reference or normal background)"
    ask = filedialog.askopenfilename(title = 'reference_BG or normal_background')
    f = open( ask, "r")
    a = f.readlines()
    bg = []
    wavelength = []
    for string in a:
      
        index_j = 0
        comma_count = 0
        for j in string:
            index_j += 1
            
            if j == ',':
                comma_count += 1
                if comma_count == 1:
                    
                    slicing_point = index_j
                    t = string[slicing_point:]
                    new_str = string[:(slicing_point- 1)]
                    new_energ = (float(1239.842 / int (float(new_str))) * 8065.54)
                    print >>h, new_energ
                    
        bg.append(t)
        wavelength.append(new_energ)

    # for fourth one, heated background
    print "Select the heated background, i.e. BkgHT file"
    ask = filedialog.askopenfilename(title = 'heated_background ie.BKgHT_file')

    f = open( ask, "r")
    a = f.readlines()
    hbg = []
    for string in a:
      
        index_j = 0
        comma_count = 0
        for j in string:
            index_j += 1
            
            if j == ',':
                comma_count += 1
                if comma_count == 1:
                    
                    slicing_point = index_j
                    t = string[slicing_point:]
        hbg.append(t)



    # calculating the value
    import math
    list = []
    for i in range(len(ref)):

               
        try:
            ans = ((float (ref[i]) - float (bg[i])) / (float(sample[i]) - float(hbg[i])))
            #print ans
            #print >>g, ans
            base= 10  


            final_ans =  (math.log(ans, base))
        except:
            ans = -1 * ((float (ref[i]) - float (bg[i])) / (float(sample[i]) - float(hbg[i])))
            #print ans
            #print >>g, ans
            base= 10  


            final_ans =  (math.log(ans, base))
        #print "Your absorbance is " + str(final_ans * -1)
        print >>g, final_ans
        list.append(final_ans)
    #print list
    g.close()
    h.close()

    combined = open("Combined_heated.txt","w")    
    with open(r'Energy.txt', "rU") as EnergyLine:
        with open(r'Absorbance.txt', "rU") as AbsorbanceLine:
            for line in EnergyLine:
                Eng = line[:-1]
                
                for line2 in AbsorbanceLine:
                    Abs = line2[:-1]
                    
                    combined.write("%s,%s\n" %(Eng,Abs))
                    break
    combined.close()

    plt.plot(wavelength, list)
    plt.show()
    os.remove('absorbance.txt')
    os.remove('Energy.txt')


except:
    print "select the reference"
    ask = filedialog.askopenfilename(title = 'Reference')
    f = open( ask, "r")
    a = f.readlines()

    g = open("absorbance.txt", "w")
    h = open("Energy.txt", "w")








    ref = []
    for string in a:
      
        index_j = 0
        comma_count = 0
        for j in string:
            index_j += 1
            
            if j == ',':
                comma_count += 1
                if comma_count == 1:
                    
                    slicing_point = index_j
                    t = string[slicing_point:]
        ref.append(t)
    #print ref


    # for second one
    print "Select the sample"
    ask = filedialog.askopenfilename(title = 'Select the Sample')
    f = open( ask, "r")
    a = f.readlines()
    sample = []
    for string in a:
      
        index_j = 0
        comma_count = 0
        for j in string:
            index_j += 1
            
            if j == ',':
                comma_count += 1
                if comma_count == 1:
                    
                    slicing_point = index_j
                    t = string[slicing_point:]
        sample.append(t)
    #print sample


    # for third one
    print "Select the bg"
    ask = filedialog.askopenfilename(title = 'Select the background ie.BG')
    f = open( ask, "r")
    a = f.readlines()
    bg = []
    wavelength = []
    for string in a:
      
        index_j = 0
        comma_count = 0
        for j in string:
            index_j += 1
            
            if j == ',':
                comma_count += 1
                if comma_count == 1:
                    
                    slicing_point = index_j
                    t = string[slicing_point:]
                    new_str = string[:(slicing_point- 1)]
                    new_energ = (float(1239.842 / int (float(new_str))) * 8065.54)
                    print >>h, new_energ
                    
        bg.append(t)
        wavelength.append(new_energ)
    #print bg
    #print wavelength



    # calculating the value
    import math
    list = []
    for i in range(len(ref)):

               
        try:
            ans = ((float (ref[i]) - float (bg[i])) / (float(sample[i]) - float(bg[i])))
            #print ans
            #print >>g, ans
            base= 10  


            final_ans =  (math.log(ans, base))
        except:
            ans = -1 * ((float (ref[i]) - float (bg[i])) / (float(sample[i]) - float(bg[i])))
            #print ans
            #print >>g, ans
            base= 10  


            final_ans =  (math.log(ans, base))
        #print "Your absorbance is " + str(final_ans * -1)
        print >>g, final_ans
        list.append(final_ans)
    #print list
    g.close()
    h.close()

    combined = open("Combined.txt","w")    
    with open(r'Energy.txt', "rU") as EnergyLine:
        with open(r'Absorbance.txt', "rU") as AbsorbanceLine:
            for line in EnergyLine:
                Eng = line[:-1]
                print Eng
                for line2 in AbsorbanceLine:
                    Abs = line2[:-1]
                    print Abs
                    combined.write("%s,%s\n" %(Eng,Abs))
                    break
    combined.close()

    plt.plot(wavelength, list)
    plt.show()
    os.remove('absorbance.txt')
    os.remove('Energy.txt')

