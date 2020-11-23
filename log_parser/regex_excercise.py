from csv import writer
import re

# my_string = "####<2020/04/21 00:00:10.977 +0200> <kfrfpr_d> <back1> <141> <INFO> 
# <guest> <kyriba.technical.performance.memory.diagnostics> <traceId: "", spanId: "" backSessionId: "", 
# jsessionid: ""> $<Memory load: type=diagnostics; 
# freememory-heap=1122970264 (1G 46M 970k 664 bytes)
#  (48.25%); freememory-young=479464528 (457M 259k 80 bytes)
#   (66.90%); freememory-tenured=643505736 (613M 711k 584 bytes) 
#   (39.95%);. Metrics [name=free_memory, value=1070; name=free_tenuredgen_memory, value=613; ]."

#"(?P<timestamp>\d{2}:\d{2}:\d{2}.\d{3}).*freememory-heap=(?P<frequency_heap>\d+).*freememory-young=(?P<frequency_young>\d+).
# *freememory-tenured=(?P<frequency_tenured>\d+)"

#Timestamp ==2020/04/21 00:00:10.977 +0200
#back server = back1
# freememory-heap=1122970264
# freememory-young=479464528
# freememory-tenured=643505736

def parser():
    with open(r'C:\Users\akash.tripathi\Desktop\python1.0\log_parser\Test_GC.txt','r') as input_file:
        with open(r'C:\Users\akash.tripathi\Desktop\python1.0\log_parser\log_parser_op.csv','w') as output_file:
            csv_writer = writer(output_file)
            csv_writer.writerow(["timestamp","freemeory-heap","freemeory-young","freemeory-tenured"])
            Tag = 'kyriba.technical.performance.memory.diagnostics'
            regex = r"(?P<timestamp>\d{2}:\d{2}:\d{2}.\d{3}).*" \
                r"freememory-heap=(?P<frequency_heap>\d+).*" \
                r"freememory-young=(?P<frequency_young>\d+).*" \
                r"freememory-tenured=(?P<frequency_tenured>\d+)"
            for line in input_file:
                if Tag in line:
                    find_values = re.findall(regex,line)
                    csv_writer.writerow(list(find_values[0]))

     


if __name__ == "__main__":
    parser()