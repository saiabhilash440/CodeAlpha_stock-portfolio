def stock_portfolio_tracker():
    # Hardcoded dictionary defining stock prices (in USD)
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "MSFT": 420.0,
        "GOOGL": 175.0,
        "AMZN": 185.0
    }

    portfolio = {}
    print("=" * 45)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 45)
    print("Available stocks and prices:")
    for ticker, price in stock_prices.items():
        print(f"  {ticker}: ${price:.2f}")
    print("-" * 45)

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
        if stock == "DONE":
            break

        if stock not in stock_prices:
            print(f"'{stock}' is not in the supported stock list. Please choose from above.")
            continue

        qty_input = input(f"Enter quantity of {stock} shares: ").strip()
        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("Please enter a valid positive integer for quantity.")
            continue

        qty = int(qty_input)
        portfolio[stock] = portfolio.get(stock, 0) + qty

    # Calculate portfolio summary
    print("\n" + "=" * 45)
    print("           PORTFOLIO SUMMARY")
    print("=" * 45)

    total_value = 0.0
    summary_lines = []

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        holding_value = price * qty
        total_value += holding_value
        line = f"{stock:6} | Quantity: {qty:<4} | Price: ${price:<7.2f} | Total: ${holding_value:.2f}"
        summary_lines.append(line)
        print(line)

    print("-" * 45)
    print(f"Total Portfolio Value: ${total_value:.2f}")

    # File handling: save report to text file
    save_choice = input("\nDo you want to save this summary to 'portfolio_summary.txt'? (y/n): ").strip().lower()
    if save_choice == 'y':
        with open("portfolio_summary.txt", "w") as f:
            f.write("STOCK PORTFOLIO SUMMARY\n")
            f.write("=" * 45 + "\n")
            for line in summary_lines:
                f.write(line + "\n")
            f.write("-" * 45 + "\n")
            f.write(f"Total Portfolio Value: ${total_value:.2f}\n")
        print("Portfolio summary saved successfully to 'portfolio_summary.txt'.")

if __name__ == "__main__":
    stock_portfolio_tracker()