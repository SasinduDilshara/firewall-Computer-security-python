import os

class FileReader:
        
    @staticmethod
    def read(selection = 1 ,word_separator="\t\t"):
        '''
        Read the data from a txt file
        '''
        # print(selection)
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "../data/input_interface_"+str(selection)+".txt"
        filename = os.path.join(script_dir, rel_path)
        # Open a file
        fo = open(filename, "rb")
        data = fo.read()
        # Close opend file
        fo.close()
        return data

    @staticmethod
    def read_config(word_separator="\t\t"):
        '''
        Read the data from a txt file
        '''
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "../Config/config"+".txt"
        filename = os.path.join(script_dir, rel_path)
        # Open a file
        fo = open(filename, "r")
        data = fo.readlines()
        # Close opend file
        fo.close()
        return FileReader.getList(data)
    
    def getList(rules,word_separator="\t\t"):
        '''
        Get the rules into a list
        '''
        rule_list = []
        for rule in rules:
            rule_list.append(rule.strip().split(word_separator))
        return rule_list

    def write_file(list_,selection = 2):
        # print('list',list_)
        try:
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "../data/input_interface_"+str(selection)+".txt"
            filename = os.path.join(script_dir, rel_path)
            # Open a file
            fo = open(filename, "ab")
            for i in list_:
                fo.write(i)
            # Close opend file
            fo.close()
            return True
        except Exception as e:
            print(e)
            return False




