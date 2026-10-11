import pandas as pd

class ExchangeRates: #class defined
    def __init__(self): #rates is the csv file name
        df = pd.read_csv('BankofCanadaExchangeRate.2026.csv') #read the csv file
        self.rate = df['FXAUSDCAD'].iloc[-1] #store the last USD/CAD value on the class

    def convert(self, amount, from_currency, to_currency): #???
        if from_currency == "USD" and to_currency == "CAD": #case 1: USD to CAD
            return amount * self.rate #multiply by the rate
        elif from_currency == "CAD" and to_currency == "USD": #case 2: CAD to USD
            return amount / self.rate #divide by the rate
        else: #any other case, such as USD to USD
            return ("Invalid conversion. Please try again.") 

xx = ExchangeRates() #

amount = (float)(input("Numerical amount to convert: ")) #ask for the amount and turn the text into a number


from_currency = input("From which currency? (USD or CAD)").upper()
to_currency = input("To which currency? (USD or CAD)").upper()

output = xx.convert(amount, from_currency, to_currency)
print ('Success! You have completed the conversion from', amount, from_currency, 'to', round(output, 2), to_currency)