import os
from company import Company
from dailyData import dailyData

'''

    FILE EXTRACTION:

    What do I have: Files with structured data.
    What I need: Matrix to store that data contents one by one

    What do I have : Stock data
    What I need: An array to store entire market data


    STORAGE:

    1) Make a class, should contain company name, company index in matrix, sector and industry, time period (maybe start and end date)

    Note - Time period is important, because that would define the indices in the general stock data.

    When computing the general stock data, I would define indices corresponding to the dates, maybe just a simple map(date: index),

    so using start and end dates in my object, I can decide what indices I need stock, industry and sector data for.

    Note, these indices might be different for corresponding stocks and sectors.

'''

def extract_stock_data(directory):

    '''
        Figure out array size. So,
    '''

    path, dirs, files = os.walk(directory).__next__()
    file_count = len(files)

    print(file_count)

    companyIndex = 0
    for filename in os.listdir(directory):

        if filename.endswith(".txt"):

            '''
            Initialize company object,
            increment companyIndex

            For i = 1, add start date
            For i = last, add end date

            Leave sector and industry blank for now
            '''

            f = open(directory + "/" + filename)
            lines = f.read()

            lines = lines.splitlines()

            if (len(lines) == 0):
                continue
            companyIndex += 1
            company = Company(filename, companyIndex, "", "", "", "")



            header = lines[0]

            print(header)

            end = 1001
            if(end > len(lines)):
                end = len(lines)

            for i in range(1, end):



                currentLine = lines[i].split(",")

                if (i == 1):
                    print(lines[i])
                    company.start_date = currentLine[0]

                if(i == end - 1):
                    company.end_date = currentLine[0]

                curData = dailyData(currentLine[0], currentLine[1], currentLine[2], currentLine[3], currentLine[4], currentLine[5])
        else:
            continue

'''
    Delegate entirety of stock extraction to that function. It returns an 2-d matrix containing the stock data and
    and array of company objects to main.



    if __name__ == "__main__":
         main()
'''

def main():

    stock_directory="C:/Users/admin/Documents/stockAnalysis/SourceData/Stocks"
    extract_stock_data(stock_directory)


if __name__ == "__main__":
     main()
