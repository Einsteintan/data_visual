import csv
from datetime import datetime

def read_date_max_min_temp(filename):
    ''' read date, maximum and minimum data from .csv file '''
    with open(filename,'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # print(header_row)

        '''
        for index,column_header in enumerate(header_row):
            print(index,column_header)
        '''

        dates = []
        highs,lows = [],[]
        for row in reader:
            try:
                current_date = datetime.strptime(row[0],'%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date,'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates,highs,lows