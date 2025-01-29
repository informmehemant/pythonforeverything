import time 
nemo  = ['nemo']

everyone = ['dory','bruce','marlin','nemo','gill','bloat','squirt','darla']

large = ['nemo' for i in range(100000)]

def find_nemo(array):
    t0= time.time()
    for i in range(0,len(array)):
        if array[i] == 'nemo':
            print("Found Nemo!!")
        t1 = time.time()
        print(f'The Search took {t1 - t0} seconds')

find_nemo(nemo)
find_nemo(everyone)
find_nemo(large)
   
def funChallenge(input):
    temp = 10 #o(1)
    temp = temp + 50 #o(1)
    for i in range(len(input)): #o(n)
        var = True #n*o(1)
        temp +=1 #n*O(1)
    return temp #O(1)


funChallenge(nemo)
funChallenge(everyone)
funChallenge(large)