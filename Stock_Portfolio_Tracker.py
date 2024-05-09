import yfinance as yf

# Define a class for the stock portfolio tracker
class PortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        """Add a stock to the portfolio."""
        if symbol.upper() in self.portfolio:
            self.portfolio[symbol.upper()] += quantity
        else:
            self.portfolio[symbol.upper()] = quantity

    def remove_stock(self, symbol, quantity):
        """Remove a specified quantity of a stock from the portfolio."""
        if symbol.upper() in self.portfolio:
            if self.portfolio[symbol.upper()] >= quantity:
                self.portfolio[symbol.upper()] -= quantity
                if self.portfolio[symbol.upper()] == 0:
                    del self.portfolio[symbol.upper()]
            else:
                print(f"Not enough {symbol} shares in the portfolio.")
        else:
            print(f"{symbol} not found in the portfolio.")

    def track_portfolio_value(self):
        """Calculate and track the total value of the portfolio."""
        total_value = 0.0
        for symbol, quantity in self.portfolio.items():
            stock = yf.Ticker(symbol)
            current_price = stock.history(period="1d")["Close"].iloc[-1]
            total_value += current_price * quantity
            print(f"{symbol}: {quantity} shares - Current Price: ${current_price:.2f}")

        print(f"Total Portfolio Value: ${total_value:.2f}")

# Main program to interact with the portfolio tracker
def main():
    tracker = PortfolioTracker()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio Value")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            tracker.add_stock(symbol, quantity)
        elif choice == "2":
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity to remove: "))
            tracker.remove_stock(symbol, quantity)
        elif choice == "3":
            tracker.track_portfolio_value()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
