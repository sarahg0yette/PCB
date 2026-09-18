class PCB: 
    def __init__(self,id,memory,arrival_time,CPU_required,Quantum,ContextSwitch_Penalty):
        self.id = id 
        self.memory = memory 
        self.arrival_time = arrival_time
        self.CPU_required = CPU_required
        self.Quantum = Quantum
        self.ContextSwitch_Penalty = ContextSwitch_Penalty

def createProcess(line,processList,idList,current_mem): 
    split_line = [int(x) for x in line.split()]  #here we take the line and split it to store it's variables, then we convert them to ints
    newP = PCB(split_line[0],split_line[1],split_line[2],split_line[3],split_line[4],split_line[5])
    
    if newP.memory > 0 and newP.arrival_time >= 0 and newP.CPU_required > 0 and newP.Quantum > 0 and newP.ContextSwitch_Penalty > 0: 
        #checking all are greater than 0, do not need to check against each other 
        if len(processList) == 0: #here there are unique steps if it's the only item in the list
                return newP
        else: 
            if newP.id not in idList and newP.Quantum == processList[0].Quantum and newP.ContextSwitch_Penalty == processList[0].ContextSwitch_Penalty: 
                return newP
            #ensuring it's a unique id, quantum and context switch should be the same for all
        
    
def reading(file,processList): #need to fix id list so it doesnt reset everytime. # !!
    current_mem = 0 #what the memory is at currently 
    process_list = [] #where the process' will be stored
    idList = []
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            clean_line = line.rstrip('\n') #removing the \n from the file
            processList.append(createProcess(clean_line,processList,idList,current_mem))
            if processList[-1] is not None: 
                idList.append(processList[-1].id) #will add the lastest name to the list
                current_mem = current_mem + processList[-1].memory 
    return processList, current_mem

def mainMenu(processList): 
    print("Welcome to your Process Manager! Please select an option from the following")
    print("1. Select an import a file")
    print("2. Manually Enter Data")
    print("3. View PCB list data") 
    print("4. Write data to new file")
    print("5. Exit")
    result = eval(input("Please Input Your Choice (1, 2, 3, 4, or 5)"))
    
    if result == 1: 
        print("Please input file name, include .txt")
        userFile = (input("File Name: "))
        processList,totalMem = reading(userFile,processList)
        print("Valid Process Data Added")
        mainMenu(processList)
    
    elif result == 3: 
        for i in processList: 
            print("Active Process id: ", i.id)
        
    else: 
        print("Not a Valid Choice")
    
    return processList  
    
def main(): 
    processList = []
    mainMenu(processList)

    '''processList,totalMem = reading("DataSet1.txt",processList)
    if totalMem > 15000: 
        print("ALERT: Total Memory Exceeds 15,000. Memory currently: ", totalMem) 
    for i in processList: 
        print("Active Process id: ", i.id)
    #print(processList)'''
    
    
if __name__ == "__main__":
    main()
    





#going to have an array of the pcb blocks  
#ok we're going to be restarting each time

#something that looks at the PCBs and ensures memory isn't going 
# over 15000 for each new PCB in the PCB array

#import a PCB file + verify info

#manually add  PCB info

#------------------------------------------------------------------------------------
    #add a greeter menu that lets you 1. Select an import a file 2. Manually Enter Data 3. View PCB list data 4. Write data to new file

