import os
from company import Company
from dailyData import dailyData

'''

    STORAGE:

    1) Make a class, should contain company name, company index in matrix, sector and industry, time period (maybe start and end date)

    Note - Time period is important, because that would define the indices in the general stock data.
    When computing the general stock data, I would define indices corresponding to the dates, maybe just a simple map(date: index),
    so using start and end dates in my object, I can decide what indices I need stock, industry and sector data for.
    Note, these indices might be different for corresponding stocks and sectors.

    Input: Directory where all the data files are stored

    Output: List of company objects and list of lists, where the first list corresponds to the company and the second list
            is a list of <dailyData> objects.

    Note: <dailyData> is a object contained the open, close, low, high, volume and date data for a given data.

    Key Idea: For market data, sector data and industry data, I would have to maintain separately hashMaps from (date: index)
              in their given list. Maybe instead of having a hashmap, I could just store these as a dictionary from
              (date: <dailyData>) object

'''

def extract_stock_data(directory):

    '''
        Figure out array size.

            Let's make a list of lists.

            Initial list - It would have file_count number of rows corresponding to each company
            Every element in the list would contain a list of objects of yype dailyData
    '''

    path, dirs, files = os.walk(directory).__next__()
    file_count = len(files)

    companyStockList = []
    companyList = []
    companyIndex = 0

    for filename in os.listdir(directory):

        if filename.endswith(".txt"):

            dataList = []
            f = open(directory + "/" + filename)
            lines = f.read()

            lines = lines.splitlines()

            if (len(lines) == 0):
                continue

            company = Company(filename, companyIndex, "", "", "", "")
            companyIndex += 1

            header = lines[0]

            end = 1001
            if(end > len(lines)):
                end = len(lines)

            for i in range(1, end):

                currentLine = lines[i].split(",")

                if (i == 1):
                    company.start_date = currentLine[0]

                if(i == end - 1):
                    company.end_date = currentLine[0]

                curData = dailyData(currentLine[0], currentLine[1], currentLine[2], currentLine[3], currentLine[4], currentLine[5])
                dataList.append(curData)

            companyStockList.append(dataList)
            companyList.append(company)

        else:
            continue
    return companyList, companyStockList

def main():

    stock_directory="C:/Users/admin/Documents/stockAnalysis/SourceData/Stocks"
    companyList, companyStockList = extract_stock_data(stock_directory)

if __name__ == "__main__":
     main()
