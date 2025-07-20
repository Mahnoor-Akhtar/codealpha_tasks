import json
from datetime import datetime
from typing import Dict, Union

class StockPortfolioTracker:
    """
    A professional stock portfolio tracking system that calculates investment value
    and maintains portfolio records.
    """
    
    def __init__(self, stock_prices: Dict[str, float]):
        """
        Initialize the portfolio tracker with current stock prices.
        
        Args:
            stock_prices: Dictionary mapping stock symbols to current prices
        """
        self.stock_prices = stock_prices
        self.portfolio = {}
        self.transaction_history = []
        
    def add_stock(self, symbol: str, quantity: int) -> None:
        """
        Add stocks to the portfolio with validation.
        
        Args:
            symbol: Stock symbol (e.g., 'AAPL')
            quantity: Number of shares
            
        Raises:
            ValueError: If invalid symbol or negative quantity
        """
        symbol = symbol.upper()
        
        if symbol not in self.stock_prices:
            raise ValueError(f"Invalid stock symbol: {symbol}")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
            
        self._record_transaction(symbol, quantity, 'BUY')
        
    def calculate_portfolio_value(self) -> float:
        """Calculate total value of the current portfolio."""
        return sum(
            self.stock_prices[symbol] * quantity
            for symbol, quantity in self.portfolio.items()
        )
    
    def _record_transaction(self, symbol: str, quantity: int, action: str) -> None:
        """Record transaction details with timestamp."""
        transaction = {
            'timestamp': datetime.now().isoformat(),
            'symbol': symbol,
            'quantity': quantity,
            'price': self.stock_prices[symbol],
            'action': action,
            'value': self.stock_prices[symbol] * quantity
        }
        self.transaction_history.append(transaction)
    
    def save_portfolio_report(self, filename: str = 'portfolio_report.json') -> None:
        """
        Save comprehensive portfolio report to JSON file.
        
        Args:
            filename: Output file name/path
        """
        report = {
            'as_of': datetime.now().isoformat(),
            'stock_prices': self.stock_prices,
            'holdings': self.portfolio,
            'portfolio_value': self.calculate_portfolio_value(),
            'transactions': self.transaction_history
        }
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
            
    def display_summary(self) -> None:
        """Display formatted portfolio summary."""
        print("\n" + "="*40)
        print("PORTFOLIO SUMMARY".center(40))
        print("="*40)
        
        for symbol, quantity in self.portfolio.items():
            price = self.stock_prices[symbol]
            value = price * quantity
            print(f"{symbol}: {quantity} shares @ ${price:.2f} = ${value:,.2f}")
            
        print("-"*40)
        print(f"TOTAL VALUE: ${self.calculate_portfolio_value():,.2f}".rjust(40))
        print("="*40 + "\n")

def main():
    # Initialize with current market prices
    current_prices = {
        "AAPL": 180.25,
        "TSLA": 250.75,
        "GOOGL": 140.50,
        "AMZN": 120.30
    }
    
    tracker = StockPortfolioTracker(current_prices)
    
    print("Stock Portfolio Tracker")
    print("Enter stock symbols and quantities. Type 'done' when finished.\n")
    
    while True:
        try:
            symbol = input("Stock symbol (or 'done'): ").strip().upper()
            if symbol == 'DONE':
                break
                
            quantity = int(input("Quantity: "))
            tracker.add_stock(symbol, quantity)
            
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return
            
    tracker.display_summary()
    
    try:
        tracker.save_portfolio_report()
        print("Portfolio report saved to 'portfolio_report.json'")
    except IOError as e:
        print(f"Warning: Could not save report - {e}")

if __name__ == "__main__":
    main()
