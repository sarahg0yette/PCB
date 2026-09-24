#Sarah G and Kate V PCB Project

class PCB: #creating a class that acts as our data structure for processes
    def __init__(self,id,memory,arrival_time,CPU_required,Quantum,ContextSwitch_Penalty):
        self.id = id 
        self.memory = memory 
        self.arrival_time = arrival_time
        self.CPU_required = CPU_required
        self.Quantum = Quantum
        self.ContextSwitch_Penalty = ContextSwitch_Penalty

def createProcess(line, processList, idList, current_mem): #this is how we make a new process
    split_line = [int(x) for x in line.split()]
    newP = PCB(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5]) #assigning parts of the input to a new pcb

    # Check each field individually to ensure it meets basic requirements 
    if newP.memory <= 0:
        print(f"Rejected process {newP.id}: memory must be greater than 0.")
        return None
    if newP.arrival_time < 0:
        print(f"Rejected process {newP.id}: arrival time cannot be negative.")
        return None
    if newP.CPU_required <= 0:
        print(f"Rejected process {newP.id}: CPU required must be greater than 0.")
        return None
    if newP.Quantum <= 0:
        print(f"Rejected process {newP.id}: Quantum must be greater than 0.")
        return None
    if newP.ContextSwitch_Penalty <= 0:
        print(f"Rejected process {newP.id}: Context Switch Penalty must be greater than 0.")
        return None

    # First process in the list — nothing to compare against yet
    if len(processList) == 0:
        return newP

    if newP.id in idList: #otherwise, we need to check it's an individual id
        print(f"Rejected process {newP.id}: a process with this ID already exists.")
        return None
    if newP.Quantum != processList[0].Quantum: #checking the new processes have the same quantum 
        print(f"Rejected process {newP.id}: Quantum ({newP.Quantum}) does not match "
            f"the existing Quantum ({processList[0].Quantum}).")
        return None
    if newP.ContextSwitch_Penalty != processList[0].ContextSwitch_Penalty: #and the same context_switch
        print(f"Rejected process {newP.id}: Context Switch Penalty ({newP.ContextSwitch_Penalty}) "
        f"does not match the existing value ({processList[0].ContextSwitch_Penalty}).")
        return None

    return newP #if it passes these checks, a new pcb is returned! 

def viewer(cid, processList): #this is if an option is selected to view an individual process in the process list
    for i in processList: 
        if i.id == cid: 
            print("Process ID", cid, "Information: ")
            print("ID:", cid, "Memory:", i.memory, "Arrival Time:", i.arrival_time, "CPU Required:", i.CPU_required)

def storeList(processList): #writing all the processes to a file 
    fileName = input("Please Type File Name. Include .txt: ")
    with open(fileName, "w", encoding="utf-8") as file:
        for i in processList: 
            file.write(f"{i.id} {i.memory} {i.arrival_time} {i.CPU_required} {i.Quantum} {i.ContextSwitch_Penalty}\n")
    
def viewList(processList, idList, totalMem): #viewing all active ids 
    while True:
        print("Process List:")

        if len(processList) > 0:
            for i in processList:
                print("Active Process id: ", i.id)
        else:
            print("No Processes")

        print("1. View a Process")
        print("2. Exit Section")

        try:
            vResult = int(input("Please Input Your Choice (1, or 2): "))
        except ValueError:
            print("Not a Valid Choice")
            continue

        if vResult == 1: #getting to a specific process
            try:
                cid = int(input("Please Input Process ID: "))
            except ValueError:
                print("Not a Valid ID")
                continue

            if cid in idList:
                viewer(cid, processList)
            else:
                print("Not a Valid ID")
            # loop back to top of this menu

        elif vResult == 2:
            return  # go back to mainMenu's loop

        else:
            print("Not a Valid Choice")
            # loop back to top of this menu

def manuallyInput(processList, idList, total_mem): #allowing a user to manually input data 
    print("You are manually inputting your new process.")
    print("Please Enter a unique process id, memory, start time, CPU required, Quantum, and Context Switch Penalty")
    try:
        result = input("Please Input Integers Separated by Spaces: ")
        new = createProcess(result, processList, idList, total_mem)
    except (ValueError, IndexError):
        print("Invalid input: please enter exactly 6 integers separated by spaces.")
        new = None
        
    if new is not None: #if the input is valid
        processList.append(new)
        idList.append(new.id)
        total_mem = total_mem + new.memory
    else:
        print("Not Valid. Please Check Active Processes")

    return processList, idList, total_mem

def reading(file,processList, idList, current_mem): #reading from a file
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            clean_line = line.rstrip('\n')
            new = createProcess(clean_line, processList, idList, current_mem)

            if new is not None: #if a process is valid 
                processList.append(new)
                idList.append(processList[-1].id)
                current_mem = current_mem + processList[-1].memory
    return processList, current_mem, idList

def mainMenu(processList, idList, totalMem): #our nav menu
    while True:
        print()
        print()
        print("Welcome to your Process Manager! Please select an option from the following")
        print("1. Select an import a file")
        print("2. Manually Enter Data")
        print("3. View PCB list data")
        print("4. Write data to new file")
        print("5. Exit")

        try:
            result = int(input("Please Input Your Choice (1, 2, 3, 4, or 5): "))
        except ValueError:
            print("Not a Valid Choice")
            continue

        if result == 1:  # selecting a file
            try:
                print("Please input file name, include .txt")
                userFile = input("File Name: ")
                processList, totalMem, idList = reading(userFile, processList, idList, totalMem)
                print("Valid Process Data Added")
                print(totalMem)
                if totalMem > 15000: #alerting it goes over total memory
                    print("ALERT: Total Memory Exceeds 15,000. Memory currently: ", totalMem)
            except (FileNotFoundError, ValueError, IndexError):
                print("Not a Valid File")

        elif result == 2:
            processList, idList, totalMem = manuallyInput(processList, idList, totalMem)
            if totalMem > 15000:
                print("ALERT: Total Memory Exceeds 15,000. Memory currently: ", totalMem)

        elif result == 3:  # viewing the process list
            viewList(processList, idList, totalMem)

        elif result == 4:
            print("4")
            storeList(processList)

        elif result == 5:
            return processList

        else:
            print("Not a Valid Choice")

def main(): #initializing and running
    processList = []
    idList = []
    totalMem = 0
    mainMenu(processList,idList,totalMem)
    
    
if __name__ == "__main__":
    main()