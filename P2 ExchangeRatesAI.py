import csv

class ExchangeRates:
    """
    A class to read USD/CAD exchange rates from a CSV file
    and convert amounts between USD and CAD.
    """

    def __init__(self, filename):
        """
        Initialize the ExchangeRates object with the CSV file name.
        Reads the latest FXAUSDCAD rate (CAD per 1 USD) from the file.
        """
        self.filename = filename
        self.usd_to_cad_rate = None
        self._load_latest_rate()

    def _load_latest_rate(self):
        """
        Read the CSV file using the csv module (encoding utf-8-sig),
        and store the FXAUSDCAD rate from the last row.
        """
        with open(self.filename, mode="r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            last_row = None

            # Iterate through all rows; the last one will be the latest rate
            for row in reader:
                last_row = row

            if last_row is None:
                raise ValueError("No data rows found in the exchange rate file.")

            # FXAUSDCAD is Canadian dollars per 1 US dollar
            self.usd_to_cad_rate = float(last_row["FXAUSDCAD"])

    def convert(self, amount, from_currency, to_currency):
        """
        Convert the given amount between USD and CAD.

        - If from USD to CAD: multiply by the rate.
        - If from CAD to USD: divide by the rate.
        - If same currency: return the amount unchanged.
        """
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        # Same currency: no conversion needed
        if from_currency == to_currency:
            return amount

        # USD to CAD: multiply by rate
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.usd_to_cad_rate

        # CAD to USD: divide by rate
        if from_currency == "CAD" and to_currency == "USD":
            return amount / self.usd_to_cad_rate

        # If currencies are not USD or CAD, raise an error
        raise ValueError("Supported currencies are only USD and CAD.")


if __name__ == "__main__":
    # Main block: interact with the user

    # Create an ExchangeRates object using the Bank of Canada CSV file
    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

    # Ask the user for the amount to convert
    amount_str = input("Enter the amount you want to convert: ").strip()

    try:
        # Convert the input string to a float
        amount = float(amount_str)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        exit(1)

    # Ask the user for the currency to convert from (USD or CAD)
    from_currency = input("Convert FROM (USD or CAD): ").strip().upper()

    # Ask the user for the currency to convert to (USD or CAD)
    to_currency = input("Convert TO (USD or CAD): ").strip().upper()

    try:
        # Perform the conversion using the convert method
        result = rates.convert(amount, from_currency, to_currency)
    except ValueError as e:
        # Handle unsupported currency or other conversion errors
        print(f"Error: {e}")
        exit(1)

    # Format the amounts with dollar signs, commas, and 2 decimal places
    formatted_input = f"${amount:,.2f} {from_currency}"
    formatted_output = f"${result:,.2f} {to_currency}"

    # Print the final result in the required format
    print(f"{formatted_input} = {formatted_output}")
