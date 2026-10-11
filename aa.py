import pandas as pd

class ExchangeRates: #class defined
    def __init__(self): #rates is the csv file name
        df = pd.read_csv('BankofCanadaExchangeRate.2026.csv') #read the csv file
        self.rate = df['FXAUSDCAD'].iloc[-1] #store the last USD/CAD value on the class

    def convert(self, amount, from_currency): #???
        if from_currency == "USD": #case 1: USD to CAD
            return amount * self.rate #multiply by the rate
        elif from_currency == "CAD": #case 2: CAD to USD
            return amount / self.rate #divide by the rate
        else: #any other case, such as USD to USD
            return ("Invalid conversion. Please try again.") 

USD_to_CAD = ExchangeRates() #

amount = (float)(input("Numerical amount to convert: ")) #ask for the amount and turn the text into a number


from_currency = input("From (please type USD or CAD)").upper()
while from_currency not in ["USD","CAD"]: #while makes it repeat until USD or CAD is given
    from_currency = input("Please type either USD or CAD)").upper()


output = USD_to_CAD.convert(amount, from_currency)
print ('Success! You have now converted into'+ (output))