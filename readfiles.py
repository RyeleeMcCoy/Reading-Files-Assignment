#-----------------------------
#reading_files.py
#Ryelee McCoy
#To show an example for accessing and reading external files such as .txt
#text files that are in the same folder as the python file are easily found
#other text files stored in their own folder will need a path to thier location
#-----------------------------


#----------------------Functions-------------------------
def read_all():
    #import a file for reading
    file  = open('days.txt', 'r')

    #save the entire file to the variable all_lines
    all_lines = file.read()
    
    #print the variable (and the whole document)
    print(all_lines)
    
    #Closes the file
    file.close()

def list_file():
    file = open('days.txt', 'r')
    #saves the file to a list
    days_list = file.readlines()
    print(days_list)
    
    #saves an index of the list days_list into weekday
    weekday = (days_list[3])
    print("The fourth day of the week is", weekday)
    
    #closes the file
    file.close()

def read_linebyline():
    file = open('days.txt', 'r')
    #saves one line to the variable line
    line = file.readline()
    print(line)
    
    #since the file has been opened, and read once, it will automatically skip to the next line
    line2 = file.readline()
    print(line2)
    
    #you could use a for loop to iterate through the lines if you wish
    file.close()

def main():
    read_all()
    list_file()
    read_linebyline()


#----------------------Main Code-------------------------

main()