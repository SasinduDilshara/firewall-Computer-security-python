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







































# from datetime import datetime
# import socket,struct,os

# def packet_filter(src_ip,des_ip,des_port,dic_acc,dic_drop,protocol):
#   try:
#     for key, value in dic_drop.items():
#       if(key[0] != '!'and value[1].isdigit()):
#         if(src_ip == key and des_ip == value[0] and des_port == value[1]): print (src_ip + ' rejected')
#       elif(key[0] == '!'and value[1].isdigit()):            
#         if('.'.join(src_ip.split('.')[0:3]) != '.'.join(key.split('.')[0:3]) and des_ip == value[0]and des_port == value[1]): print (src_ip + ' rejected')
#       elif(key[0] != '!'and not value[1].isdigit()):
#         x,y = value[1].split('-')
#         if(src_ip == key and des_ip == value[0] and  int(x) <= int(des_port) <= int(y)): print (src_ip + ' rejected')
#       elif(key[0] == '!'and not value[1].isdigit()):
#         x,y = value[1].split('-')
#         if('.'.join(src_ip.split('.')[0:3]) != '.'.join(key.split('.')[0:3]) and des_ip == value[0] and  int(x) <= int(des_port) <= int(y)): print (src_ip + ' rejected')
              
#     for key, value in dic_acc.items():
#       if(key[0] != '!'and value[1].isdigit()):
#         if(src_ip == key and des_ip == value[0] and des_port == value[1]): 
#           print (src_ip + ' accepted')
#           output_interface(protocol,src_ip,des_ip,des_port)
#       elif(key[0] == '!'and value[1].isdigit()):
#         if('.'.join(src_ip.split('.')[0:3]) == '.'.join(key.split('.')[0:3]) and des_ip == value[0]and des_port == value[1]): 
#           print (src_ip + ' accepted')
#           output_interface(protocol,src_ip,des_ip,des_port)
#       elif(key[0] != '!'and not value[1].isdigit()):
#         x,y = value[1].split('-')
#         if(src_ip == key and des_ip == value[0] and  int(x) <= int(des_port) <= int(y)): 
#           print (src_ip + ' accepted')
#           output_interface(protocol,src_ip,des_ip,des_port)
#       elif(key[0] == '!'and not value[1].isdigit()):
#         x,y = value[1].split('-')
#         if('.'.join(src_ip.split('.')[0:3]) == '.'.join(key.split('.')[0:3]) and des_ip == value[0] and  int(x) <= int(des_port) <= int(y)): 
#           print (src_ip + ' accepted')
#           output_interface(protocol,src_ip,des_ip,des_port)
#   except KeyboardInterrupt:
#             print("interrupted")


# def read_config(protocol):
#   filepath = '/content/drive/My Drive/firewall/config.txt'
#   try:
#     with open(filepath,'r') as cred_in: 
#       lines = cred_in.readlines() 
#       dic_drop = {}
#       dic_acc = {}
#       for line in lines: 
#         data = line.rstrip('\n').split(' ')
#         if(data[1] == protocol or data[1] == 'any'):
#           if(data[0] == 'DROP'):
#             dic_drop[data[2]]= [data[3],data[4]]
#           else:
#             dic_acc[data[2]]= [data[3],data[4]]
#       return dic_acc,dic_drop
#   except FileNotFoundError:
#     return False


# def input_interface():
#   filepath = '/content/drive/My Drive/firewall/input.txt'
#   try:
#     with open(filepath,'r') as cred_in: 
#       lines = cred_in.readlines() 
#       l = []
#       for line in lines: 
#         data = int(line.rstrip('\n'))
#         l.append(data.to_bytes(52,byteorder='big'))
#       return l
#   except FileNotFoundError:
#     return False
# def output_interface(protocol,src_ip,des_ip,des_port):
#   filepath = '/content/drive/My Drive/firewall/output.txt'
#   try:
#     with open(filepath,'a') as packets_out: 
#       packets_out.write('%s %s %s %s\n'%(src_ip,des_ip,des_port,protocol))
#   except FileNotFoundError:
#     return False


# def main():
#     l = read_input()
#     packet_header = {}
#     for i in l:
#             packet = i
#             ip_header = packet[0:20]
#             iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)
#             src_ip = socket.inet_ntoa(iph[8])
#             des_ip = socket.inet_ntoa(iph[9])
#             protocol = str(iph[6])

#             tcp_udp_header = packet[20:40]
#             tcp_udp_hdr = struct.unpack("!HH9ss6s",tcp_udp_header)
#             des_port = str(tcp_udp_hdr[1])
#             packet_header[src_ip] = [des_ip,des_port,protocol]
#             print('SRC_IP: ' + src_ip + '  DES_IP: ' + des_ip + '  DES_PORT: ' + des_port+' PROTOCOL: '+protocol)
#             if (int(protocol) == socket.IPPROTO_TCP):
#               packet_filter('TCP',src_ip,des_ip,des_port)
#             else:
#               packet_filter('UDP',src_ip,des_ip,des_port)

# main()

























