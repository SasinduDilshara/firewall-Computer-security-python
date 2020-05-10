from functions.file_reader import FileReader
import socket,struct,os

class Convert:
    @staticmethod
    def convert(selection = 1):
        results = []
        data = FileReader.read(selection)
        for i in range(0,len(data),54):
            ip_header = data[i+14:i+34]
            ip_hdr= struct.unpack("!BBHHHBBH4s4s",ip_header)
            tcp_header = data[i+34:i+54]
            tcp_hdr = struct.unpack("!HH9ss6s",tcp_header)
            sa = socket.inet_ntoa(ip_hdr[8])
            da = socket.inet_ntoa(ip_hdr[9])
            sp = tcp_hdr[0]
            dp = tcp_hdr[1]
            if(ip_hdr[6] == 6):
                protocol = 'TCP'
            else:
                protocol = 'UDP'
            results.append([protocol,str(sa),str(da),str(dp)])
        return results