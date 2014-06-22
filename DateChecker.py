"""Implementation of the Python Date Formatter """
from __builtin__ import len
import time

def date_checker(date_str):
    """ Format the date"""
    delimiter = ['-','/',' '] # Add any delimiter that you want
    format_d = ['%d','%e','%m','%b','%B','%y', '%Y',] #DateTIme Formats
    return_list = []
    if not date_str:
        print "Enter a date String"
    else:
        for dem in delimiter:    
            date_list = date_str.split(dem)
            if len(date_list)==3:
                val1 =date_list[0]
                val2 =date_list[1]
                val3 =date_list[2]
                for i in format_d:
                    for j in format_d:
                        for k in format_d:
                            try:
                                dt = time.strptime("%s %s %s" % (val1, val2, val3), "%s %s %s"%(i, j, k))
                                if dt:
                                    print time.strftime("%d %b %Y", dt)
                                    return_list.append(time.strftime("%d %b %Y", dt)) 
                            except:
                                continue
    return return_list
 

if __name__ == "__main__":
    ### Inputs ### 
    string_1 = raw_input("Enter a Date Ex: (4-5-45) or Just Hit Enter Key to see the date for (7 2 1998)")
    if not string_1:
        string_1 = "11-12-89"
    date_checker(string_1)

    