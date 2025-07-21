import pyshark
import datetime

interfaces = ['en0', 'awdl0', 'llw0', 'utun0', 'utun1', 'utun2', 'utun3', 'utun4', 'lo0', 'ap1', 'en1', 'en2', 'en4', 'en3', 'bridge0', 'gif0', 'stf0', 'ciscodump', 'randpkt', 'sshdump', 'udpdump', 'wifidump']
for inter in interfaces:
    print("------------------------------- "+inter+" -------------------------------")
    tmp = inter+".pcap"
    capture = pyshark.LiveCapture(interface='Wi-Fi', output_file=tmp)
    capture.sniff(timeout=10)
    shows = pyshark.FileCapture(tmp)
    for i in capture:
        print(i)
    
        

