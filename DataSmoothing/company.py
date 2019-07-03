class Company:

    def __init__(self, name, index, sector, industry, start_date, end_date):
        self.name = name
        self.index = index
        self.sector = sector
        self.industry = industry
        self.start_date = start_date
        self.end_date = end_date


    def __str__(self):
         return str(self.name) + " " + str(self.index)

#Make a class, should contain company name, company index in matrix, sector and industry, time period (maybe start and end date)
#At sector and industries could also be represented as objects

if __name__ == "__main__":
     main()
