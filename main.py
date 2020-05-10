from functions.file_reader import FileReader
from functions.filter import FilterActions
from datetime import datetime
from functions.convert import Convert


def main():
    # print(FileReader.read_config())
    # print(Convert.convert())

    # print(FileReader.read(2))
    input_,result,accepted_data = FilterActions.filter()
    FileReader.write_file(accepted_data)
    for i in range(len(result)):
        print("Source PROTOCOL "+input_[i][0]+"\n"+"Source IP "+input_[i][1]+"\n"+"Destination IP "+input_[i][2]+"\n"+"Destination PORT "+input_[i][3])
        print("RESULT : -" + result[i]+"\n")
if __name__ == "__main__":
    output = main()
































