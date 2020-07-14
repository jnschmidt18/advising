def removeHTML(filename):           #function removes html and other noise from file transcript
    transcript= open(filename, 'r')
    transcript= list(transcript)
    for i in range(len(transcript)):        #removes most of the html, and the small script part
        if(transcript[i][0]=='<' or i<22):  #by changing to a temp, and then deleting that later
            transcript[i]='temp'            #so as not to mess up the for loop based on the length
        transcript[i]=transcript[i][:44] 
    transcript= [x for x in transcript if x != 'temp']  #removes temporary terms
    transcript= [x for x in transcript if x != '      TERM . . . . . . . . . . . . . . . . .']
    for i in range(len(transcript)):
        transcript[i]=transcript[i].rstrip()        #removes tab and newline characters
    for i in range(len(transcript)):
        if(transcript[i][0:4]=='    ' or transcript[i][0:4]=='----'):   #removes whitespace 
            transcript[i]='temp'                                        #and dashed lines
    transcript= [x for x in transcript if x != 'temp']                  
    del transcript[2]                                                   #removed lines from 
    del transcript[-1]                                                  #fixed positions
    transcript = [i for i in transcript if i]           #removes empty indices from list
    for i in range(len(transcript)):
        print(transcript[i])
    return transcript

def getGenEds(filename):
    transcript= open(filename, 'r')
    transcript= list(transcript)
    for i in range(len(transcript)):        #removes most of the html, and the small script part
        if(transcript[i][0]=='<' or i<22):  #by changing to a temp, and then deleting that later
            transcript[i]='temp'            #so as not to mess up the for loop based on the length
        substring=transcript[i][44:60]
        transcript[i]=transcript[i].replace(substring, '')
    transcript= [x for x in transcript if x != 'temp']  #removes temporary terms
    transcript= [x for x in transcript if x != '      TERM . . . . . . . . . . . . . . . . .']
    for i in range(len(transcript)):
        transcript[i]=transcript[i].rstrip()        #removes tab and newline characters
    for i in range(len(transcript)):
        if(transcript[i][0:7]=='      T' or transcript[i][0:7]=='      C'  or transcript[i][0:4]=='----' or transcript[i][-1:]==')'):   #removes whitespace 
            transcript[i]='temp'                                        #and dashed lines
    transcript= [x for x in transcript if x != 'temp']                  
    del transcript[2]                                                   #removed lines from 
    del transcript[-1]                                                  #fixed positions
    transcript = [i for i in transcript if i]           #removes empty indices from list
    for i in range(len(transcript)):
        transcript[i]=transcript[i][-4:]
    transcript=transcript[4:]
    transcript=transcript[:-9]
    return transcript
    
def makeCoursesList(filename):   #takes list from removeHTML, and makes a list of passed courses
    compList=removeHTML(filename)
    compList=compList[4:]           #remove unneccesary lines
    for i in range(len(compList)):                          #iterate through to removed gen ed 
        if(compList[i][0]!=' ' or compList[i][-1]=='F' or compList[i][-3:]=='CIP'):    #section and failed courses using the 
            compList[i]='temp'                              #temp method for iteration
    compList= [x for x in compList if x != 'temp']
    for i in range(len(compList)):                  #removes unneccesary whitespace
        compList[i]=compList[i][2:]
    return compList

def genTypesFinished(filename):     #currently unused, but will be needed eventually
    compList=getGenEds(filename)   #this function returns the gen ed section of transcript
    compList=compList[4:]
    for i in range(len(compList)):  #removes unnessecary sections using temp method
        if(compList[i][0]==' '):
            compList[i]='temp'
    compList= [x for x in compList if x != 'temp']
    compList=compList[2:]
    return compList
