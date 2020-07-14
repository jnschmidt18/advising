import transcriptHandler as th                        #import functions for transcript handling

def validateEcon(filename):                                   
    coursesTaken=th.makeCoursesList(filename) #grab courses taken from th lib
    complete= True                                    #complete initalally true, set false if 
    regComplete= True                                 #any condition is not met
    quantComplete= True
    returnString=''
    for i in range(len(coursesTaken)):                #cut courses list down to just abbr and num
        coursesTaken[i]=coursesTaken[i][:7]
    if('ECO 101' not in coursesTaken):                #validate basic requirements
        returnString+='Student must take ECO 101\n'
        complete= False
    if('ECO 241' not in coursesTaken):
        returnString+='Student must take ECO 241\n'
        complete= False
    if('ECO 242' not in coursesTaken):
        returnString+='Student must take ECO 242\n'
        complete= False
    if('ECO 243' not in coursesTaken):
        returnString+='Student must take ECO 243\n'
        complete= False
    if('ECO 498' not in coursesTaken):
        returnString+='Student must take ECO 498\n'
        complete= False
    if('ECO 499' not in coursesTaken):
        returnString+='Student must take ECO 499\n'
        complete= False
    returnString+=('Regular Economics Track:\n')                 #validate regular econ track completion
    remReqHigh=3
    remReq=6
    prevTaken=['101','241','242','243','498','499']
    for i in range(len(coursesTaken)):                #iterate through taken courses for 3/400 level, of which 3 must be taken, and 3 other econ
        if((coursesTaken[i][:5]=='ECO 3' or coursesTaken[i][:5]=='ECO 4') and coursesTaken[i][4:7] not in prevTaken):
            remReqHigh-=1
        if((coursesTaken[i][:3]=='ECO' and coursesTaken[i][4:7] not in prevTaken) or coursesTaken[i]=='PHL 123'):
            remReq-=1
    if(remReqHigh>0):                                    #if number of remaining courses is over 0, more courses are required
        regComplete= False
        returnString+=('Student must take ' + str(remReqHigh) + ' more economics courses at a the 3/400 level for the regular track\n')
    if(remReq>0):
        regComplete= False
        returnString+=('Student must take ' + str(remReq) + ' more economics courses total for the regular track\n')
    returnString+=('Quantitative Economics Track:\n')           #validate quantitative econ track completion
    threeOfFour=4                                    #this solution for the 3/4 problem is a little janky, but it works, uses a lot of lines but 
    if('ECO 338' in coursesTaken):                   #isn't horribly runtime inefficient
        threeOfFour-=1
        prevTaken.append('338')
    if('ECO 341' in coursesTaken):
        threeOfFour-=1
        prevTaken.append('341')
    if('ECO 352' in coursesTaken):
        threeOfFour-=1
        prevTaken.append('352')
    if('ECO 353' in coursesTaken):
        threeOfFour-=1
        prevTaken.append('353')
    if(threeOfFour>1):                              #if less than 3 of these classes have been taken, the var will be >1
        quantComplete= False
        returnString+=('Student must take ' + str(threeOfFour-1) + ' more classes from ECO 338, 341, 352, 353\n')
    remEcon=2
    remMath=3
    for i in range(len(coursesTaken)):              #validate remaining 2 econ courses and 3 math courses, with coverage for previous
        if((coursesTaken[i][:3]=='ECO' and coursesTaken[i][4:7] not in prevTaken) or coursesTaken[i]=='PHL 123'):
            if(remEcon!=0):
                remEcon-=1
        if(coursesTaken[i][:3]=='MTH' and int(coursesTaken[i][4:7])>110):
            if(remMath!=0):
                remMath-=1
    if(remEcon>0 or remMath>0):                     #if not both of the requirements are met, quantitative is not complete
        quantComplete= False
        returnString+=('Student needs to take ' + str(remEcon) + ' additional economics courses and ' + str(remMath) + ' more math courses for the quantitative track\n')
    if(not(regComplete or quantComplete)):          #if neither the regular nor the quantitative tracks are met, then not complete
        complete= False
    if(complete):
        returnString+=('Student has completed the Economics major\n')
    if(not complete):
        returnString+=('Student has not completed the Economics major\n')
    return returnString
