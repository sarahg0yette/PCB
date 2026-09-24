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
        
def viewer(cid, processList): 
    for i in processList: 
        if i.id == cid: 
            print("Process ID", cid, "Information: ")
            print("ID:", cid, "Memory:", i.memory, "Arrival Time:", i.arrival_time, "CPU Required:", i.CPU_required)

def storeList(processList): 
    with open("output.txt", "w", encoding="utf-8") as file:
        for i in processList: 
            file.write(f"{i.id} {i.memory} {i.arrival_time} {i.CPU_required} {i.Quantum} {i.ContextSwitch_Penalty}\n")
    
def viewList(processList,idList,totalMem): 
    print("Process List:")
    
    if len(processList) > 0: 
        for i in processList: 
            print("Active Process id: ", i.id)
    else: 
        print("No Processes")
    
    print("1. View a Process")
    print("2. Exit Section")
    vResult = int(input("Please Input Your Choice (1, or 2): "))
    if vResult == 1: 
        cid = eval(input("Please Input Process ID: "))
        if cid in idList:
            viewer(cid, processList)
        else: 
            print("Not a Valid ID")
        viewList(processList, idList, totalMem)  #returning them to this menu
        
    elif vResult == 2:
        mainMenu(processList,idList,totalMem) #returning to main menu
        
    else: 
        print("Not a Valid Choice")
        viewList(processList, idList, totalMem)  #returning to this menu

def manuallyInput(processList, idList, total_mem):
    print("You are manually inputting your new process.")
    print("Please Enter a unique process id, memory, start time, CPU required, Quantum, and Context Switch Penalty")
    try:
        result = input("Please Input Integers Separated by Spaces: ")
        new = createProcess(result, processList, idList, total_mem)
    except (ValueError, IndexError):
        print("Invalid input: please enter exactly 6 integers separated by spaces.")
        new = None
        
    if new is not None:
        processList.append(new)
        idList.append(new.id)
        total_mem = total_mem + new.memory
    else:
        print("Not Valid. Please Check Active Processes")

    return processList, idList, total_mem

def reading(file,processList, idList): 
    current_mem = 0 
    
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            clean_line = line.rstrip('\n') #removing the \n from the file
            new = createProcess(clean_line,processList,idList,current_mem)  
            
            if new is not None: #ensuring there is a new process
                processList.append(new)
                idList.append(processList[-1].id) #will add the lastest name to the list
                current_mem = current_mem + processList[-1].memory 
    return processList, current_mem, idList

def mainMenu(processList,idList,totalMem): 
    
    print("Welcome to your Process Manager! Please select an option from the following")
    print("1. Select an import a file")
    print("2. Manually Enter Data")
    print("3. View PCB list data") 
    print("4. Write data to new file")
    print("5. Exit")
    result = int(input("Please Input Your Choice (1, 2, 3, 4, or 5): "))
    
    if result == 1: #selecting a file
        processList = [] #resetting each time
        idList = []
        try:
            print("Please input file name, include .txt")
            userFile = (input("File Name: "))
            processList,totalMem,idList = reading(userFile,processList,idList)
            print("Valid Process Data Added")
            print(totalMem)
            if totalMem > 15000: 
                print("ALERT: Total Memory Exceeds 15,000. Memory currently: ", totalMem) 
            mainMenu(processList,idList,totalMem)
        except: 
            print("Not a Valid File")
            mainMenu(processList,idList,totalMem)
    
    elif result == 2:
        processList, idList, totalMem = manuallyInput(processList, idList, totalMem)
        if totalMem > 15000:
            print("ALERT: Total Memory Exceeds 15,000. Memory currently: ", totalMem)
        mainMenu(processList, idList, totalMem)
        
    elif result == 3: #viewing the process list
        viewList(processList,idList,totalMem)

    elif result == 4: 
        print("4")
        storeList(processList)
        mainMenu(processList,idList,totalMem)
        
    elif result == 5: 
        return ()
    
    else: 
        print("Not a Valid Choice")
    
    return processList  
    
def main(): #theres an issue tracking the memory
    processList = []
    idList = []
    totalMem = 0
    mainMenu(processList,idList,totalMem)

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

