import numpy as np


def loadM5(max_probability=95):
    retval_V = list()
    retval_I = list()
    ID_list = list()
    temp = [0,0]
    FILE = open('HW4/data/M5_1.dat','r')
    lines = FILE.readlines()[54:3127]
    for i in range(len(lines)):
        if len(lines[i]) < 2 or lines[i][0:2] != '15':
            continue
        splitline=lines[i].replace('       ',' @ ').strip().split()

        if len(splitline) < 10:#8:
            continue

        ID=splitline[6]

        if ID not in ID_list:
            ID_list.append(ID)
        if ID in ID_list and temp[0] != 0 and temp[1] != 0:
            retval_V.append(temp[0])
            retval_I.append(temp[1])
            temp = [0,0]
            continue #Just ignore re-writing points
        probability=splitline[7]
        #print ID,len(splitline)
        if probability != '@' and float(probability) >= max_probability*0.01:
            if len(splitline) == 10:
                V = splitline[9]
                I = '@'
            elif len(splitline) == 11:
                V = '@'
                I = splitline[10]
#            print "foo",V,I
            if V != '@' or I != '@':
                if V != '@' and temp[0] == 0:
                    temp[0] = float(V)
                elif I != '@' and temp[1] == 0:
                    temp[1] = float(I)
                ID_list.append(ID)
    FILE.close()
    FILE = open('HW4/data/M5_2.dat','r')
    lines = FILE.readlines()[39:10447]
    for i in range(len(lines)):
        splitline = lines[i].strip().split()
        probability = float(splitline[2])
        if probability >= max_probability*0.01:
            retval_V.append(float(splitline[0]))
            retval_I.append(float(splitline[1]))

    FILE.close()

    FILE = open('HW4/data/M5_3.dat','r') #relatively useless
    lines = FILE.readlines()[47:178]
    for i in range(len(lines)):
        splitline = lines[i].strip().split()
        if len(splitline) < 9:
            continue
        probability = float(splitline[6])
        if probability >= max_probability*0.01:
            V = float(splitline[7])
            I = V-float(splitline[8])
            retval_V.append(V)
            retval_I.append(I)

    FILE.close()
    return np.array(retval_V), np.array(retval_I)



def loadM45(max_probability=95):
    retval_V = list()
    retval_I = list()
    FILE = open('HW4/data/M45.dat','r')
    lines = FILE.readlines()[11:3289]
    for i in range(len(lines)):
        splitline = lines[i].strip().split()
        probability = splitline[2]
        if probability != '~' and int(probability) >= max_probability:
            V = splitline[-2]
            I = splitline[-1]
            if V != '~' and I != '~':
                retval_V.append(float(V))
                retval_I.append(float(I))
    FILE.close()
    return np.array(retval_V), np.array(retval_I)




def loadM67(max_probability=95):
    retval_V = list()
    retval_I = list()
    FILE = open('HW4/data/M67.dat','r')
    lines = FILE.readlines()[47:2456]
    for i in range(len(lines)):
        splitline = lines[i].replace('       ',' @ ').strip().split()
        probability = int(splitline[-1])
        if probability >= max_probability:
            V = splitline[7]
            I = splitline[8]
            if V != '@' and I != '@':
                retval_V.append(float(V))
                retval_I.append(float(I))
    FILE.close()
    return np.array(retval_V), np.array(retval_I)



def loadMS(age):
    data = np.loadtxt('HW4/data/outputiso.dat')
    data = np.transpose(data)
    inds = np.where(np.logical_and(np.abs(data[0]-age)<0.001,data[4]<10))[0] #M<10 Msun
    retval_V = data[9][inds]
    retval_I = data[11][inds]
    return retval_V, retval_I


def loadZAMS():
    return loadMS(age=7.0)
