
import csv
import re


def parser():

   with open("C:/PAYMENT31/PAYMENT31_LoadT6_Run2/PAYMENT31_LoadT6_Run2/back1_performance.log",'r') as f_input, open('back1.csv', 'w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(['Timestamp', 'freememory-heap','freememory-young','freememory-tenured'])
    Tag = 'kyriba.technical.performance.memory.diagnostics'
    regex = r"(?P<timestamp>\d{2}:\d{2}:\d{2}.\d{3}).*" \
        r"freememory-heap=(?P<frequency_heap>\d+).*" \
        r"freememory-young=(?P<frequency_young>\d+).*" \
        r"freememory-tenured=(?P<frequency_tenured>\d+)"

    for line in f_input:
         if Tag in line:
             re_values = re.findall(regex,line,re.MULTILINE)
        #print (re_values)

             if re_values:
                 csv_output.writerows(re_values)
   
  

def main():
    parser()


if __name__ == "__main__":
     main()        