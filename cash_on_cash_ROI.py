class CashOnCashROI():

    def __init__(self):
        self.property_cost = input('What is the purchase price of the property? ')

    def income(self):
        self.rental_income = int(input('What is the monthly rental income on this property? '))
        self.laundry_income = int(input('What is the monthly laundry income on this property? '))
        self.storage_income = int(input('What is the monthly storage income on this property? '))
        self.misc_income = int(input('What are the other monthly total miscellaneous incomes on this property '))
        self.total_income = int(self.rental_income + self.laundry_income + self.storage_income + self.misc_income)
        print('The total monthly income on this property is $' + str(self.total_income))

    def expenses(self):
        self.taxes = int(input('What is the monthly tax on this property? '))
        self.insurace = int(input('What is the monthly insurance on this property? '))
        self.utilities = int(input('What is the monthly utility cost on this property? '))
        self.hoa = int(input('What is the monthly HOA fee on this property? '))
        self.lawn_snow = int(input('What is the monthly lawn and snow maintainance cost on this property '))
        self.vacancy = int(input('What is the monthly vacancy cost on this property? '))
        self.repair = int(input('What is the monthly repair cost on this property? '))
        self.capex = int(input('What is the monthly capital expenditure on this property? '))
        self.prop_management = int(input('What is the monthly property management cost on this property? '))
        self.mortgage = int(input('What is the monthly mortgage on this property? '))
        self.total_expenses = int((self.taxes + self.insurace + self.utilities + self.hoa + self.lawn_snow
                               + self.vacancy + self.repair + self.capex + self.prop_management + self.mortgage))
        print('Your total monthly expenses are: ' + str(self.total_expenses))

    def cashFlow(self):
        self.monthly_cash_flow = self.total_income - self.total_expenses
        print('Your monthly cash flow is: $' + str(self.monthly_cash_flow))

    def cashOnCash(self):
        self.downpay_percent = float(input('What percentage will you be putting down on this property? ')) / 100
        self.downpayment = self.downpay_percent * float(self.property_cost)
        print('Your downpayment is: $' + str(self.downpayment))
        self.closing_costs = int(input('What are the closing costs on this property? '))
        self.rehab = int(input('How much will you be putting into the rehab on this property? '))
        self.total_investment = self.downpayment + float(self.closing_costs) + float(self.rehab)
        print('Your total investment on this property is: $' + str(self.total_investment))
        self.annual_cash_flow= 12 * self.monthly_cash_flow
        print('Your total annual cashflow on this property is: ' + str(self.annual_cash_flow))
        self.cash_on_cash_ROI = float(self.annual_cash_flow) / float(self.total_investment)
        print('Your Cash on Cash ROI on this property would be: ' + str((self.cash_on_cash_ROI) * 100) + "%")
        
KrassROI = CashOnCashROI()        

while True:
    run = input('\nThis is a service that will calculate the Cash on Cash ROI of an investment property\nPress [I] to enter incomes: \nPress [E] to enter expenses: \nPress [F] to view your cash flow: \nPress [C] to see your cash on cash ROI: \nPress [Q] to quit: ')
    if run.lower() == 'i':
        KrassROI.income()
    elif run.lower() == 'e':
        KrassROI.expenses()
    elif run.lower() == 'f':
        KrassROI.cashFlow()
    elif run.lower() == 'c':
        KrassROI.cashOnCash()
    elif run.lower() == 'q':
        print("\nThank you, have a nice day")
        break
        