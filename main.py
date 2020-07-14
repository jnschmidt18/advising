import paths  #paths for requirments, implements transcriptHandler
import GUI    #basic TK gui

def main():
    filename=GUI.getfile()      #use OS dialog to get file extension
    GUI.writeToWindow(paths.validateEcon(filename)) #write to GUI window
    
main()  #execute main
