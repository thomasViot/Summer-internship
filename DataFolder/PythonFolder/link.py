import os
import shutil
import time

from matplotlib.pyplot import suptitle


# -------- global parameters ------ #

global_data = "../DatFolder/globalData"
specific_data = "../DatFolder/specificData"
folder_destination_global_Data = '../DatFolder/OnlyLinkedGlobalData'
folder_destination_specific_Data = "../DatFolder/OnlyLinkedSpecificData"
# --------------------------------- #

def removeFiles(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def changeFileName(list, startPoint):
    for i in list:
        num = list.index(i)
        i = i.replace('_',' ')
        i = i.replace('.dat','')
        i = i.replace(i[:startPoint],'')
        list[num] = i;
    
    return list


def writeDate(date):
    file = open("DayMonthYear.txt", "a",encoding="UTF-8")
    file.write(str(date))
    file.write('\n')
    file.close()
    

def moveFiles(list1,list2, list1_original, list2_original):
    for k in list1:
        for h in list2:
            if h == k:
                shutil.copy(global_data + '/'+ list1_original[list1.index(k)], folder_destination_global_Data)
                shutil.copy(specific_data + '/'+ list2_original[list2.index(h)], folder_destination_specific_Data)


def renameFile(folder, startPoint):
    list = os.listdir(folder)
    list_original = list
    index = 0
    for i in list:
        i = i.replace('_',' ')
        i = i.replace('.dat','')
        i = i.replace(i[:startPoint],'')
        os.rename(folder + '/'+ list_original[index], folder + "/" + str(i) + ".dat")
        index = index + 1


def getNewNames(folder):
    list = os.listdir(folder)

    for i in list:
        writeDate(i[0:19])

    if os.path.exists("../TextFolder/bigFiles/DayMonthYear.txt"):
        os.remove("../TextFolder/bigFiles/DayMonthYear.txt")
        print("removing the file")

    shutil.move("DayMonthYear.txt", "../TextFolder/bigFiles")

def main():

    list1 = os.listdir(global_data)  # find all files in a directory
    list2 = os.listdir(specific_data)

    list1_original = os.listdir(global_data)  
    list2_original = os.listdir(specific_data)

    number_global_files = len(list1)
    number_specific_files = len(list2)

    print("The number of global files is : " + str(number_global_files))
    print("The number of specific files is : " + str(number_specific_files) + '\n')
   
    removeFiles(folder_destination_specific_Data)
    removeFiles(folder_destination_global_Data)

    list1 = changeFileName(list1, 18)
    list2 = changeFileName(list2, 13)

    moveFiles(list1,list2, list1_original, list2_original)

    renameFile(folder_destination_global_Data,18)
    renameFile(folder_destination_specific_Data,13)

    getNewNames(folder_destination_global_Data)

if __name__ == "__main__":
    main()

