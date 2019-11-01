import itertools
# from numpy import zeros
import numpy as np

ST = np.load('final_table_species_tree.npy')
#print(ST)
f=open('all_combinations.txt')
lines=f.readlines()
fileToWrite= open("tripletsfromSpeciesTreeMatrix.txt","w+")
for row in ST:
    count_col=0
    for col in row:
        count_col = count_col+1
        #print(col)
        #print("------------------------")
        idx = -1
        count_page = 0
        for page in col:
            count_page = count_page+1
            if page == 1.0:
                idx = count_page
        str = lines[(count_col-1)*6+2+idx]

        splitstr = str.split(':')
       # print (splitstr[0])
        splitstr2 = splitstr[0].split(',')
        finalstr = splitstr2[0] + '|'+ splitstr2[1]+ ','+splitstr2[2]
        fileToWrite.write(finalstr)
        fileToWrite.write("\n")

fileToWrite.close()
