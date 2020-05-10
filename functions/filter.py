from functions.file_reader import FileReader

from datetime import datetime
from functions.convert import Convert


class FilterActions:

    @staticmethod
    def filter():
        rules = FileReader.read_config()
        data_,data_list = Convert.convert()
        # print(len(data_))
        checked = []
        accepted_data = []
        result = False
        count = 0
        for data in data_:
            for rule in rules[:-1]:
                for element in range(1,len(rule)):
                    if (element == 1 and rule[element] == data[element-1]):
                        result = True
                    elif(element in [2,3]):
                        # print(rule[element],data[element-1],FilterActions.checkIP(rule[element],data[element-1]))
                        result = result and FilterActions.checkIP(rule[element],data[element-1])
                    else:
                        # print(rule[element],data[element-1],FilterActions.checkport(rule[element],data[element-1]))
                        result = result and FilterActions.checkport(rule[element],data[element-1])
                if(result == True):
                    # print(result,rule[0])
                    checked.append(rule[0])
                    accepted_data.append(data_list[count])
                    
                    break
            else:
                # print(result,rules[-1][0])
                checked.append(rules[-1][0])
            count+=1
        return data_,checked,accepted_data

    @staticmethod
    def checkIP(ip1,ip2):
        # try:
        if(ip1 == ip2):
            return True
        ip1 = ip1.split(".")
        ip2 = ip2.split(".")
        if("*" not in ip1):
            return False
        if (ip1[3] != ip2[3] and ip1[3] != "*"):
            return False
        elif (ip1[2] != ip2[2] and ip1[3] != "*"):
            return False
        elif (ip1[1] != ip2[1] and ip1[3] != "*"):
            return False
        elif (ip1[0] != ip2[0] and ip1[3] != "*"):
            return False
        else:
            return True
        # except Exception as e:
        #     print(e)
        #     return False

    @staticmethod
    def checkport(p1,p2):
        # try:
        # print("\n")
        # print(p1,p2)
        if(p1 == p2):
            return True
        p1 = p1.split("-")
        if(len(p1) == 2):
            if(int(p1[1]) >= int(p2) >= int(p1[0])):
                return True
            return False
        else:
            return False
        # except Exception as e:
        #     print(e)
        #     return False
