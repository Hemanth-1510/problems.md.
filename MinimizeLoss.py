def minimize_loss(prices):
    indexed_prices = [(price, i) for i, price in enumerate(prices)]
    sorted_prices = sorted(indexed_prices)  # Ascending price order

    min_loss = float('inf')
    buy_year = sell_year = -1
    price_index_map = {price: idx for idx, price in indexed_prices}

    for i in range(1, len(sorted_prices)):
        higher_price, higher_year = sorted_prices[i]
        lower_price, lower_year = sorted_prices[i-1]

        # Buy at higher price, sell at lower price but only if buy year is before sell year
        if price_index_map[higher_price] < price_index_map[lower_price]:
            loss = higher_price - lower_price
            if loss < min_loss:
                min_loss = loss
                buy_year = price_index_map[higher_price] + 1
                sell_year = price_index_map[lower_price] + 1

    return buy_year, sell_year, min_loss

# Input
n = int(input())
prices = list(map(int, input().split()))
buy, sell, loss = minimize_loss(prices)
print(f"Buy Year: {buy}, Sell Year: {sell}, Loss: {loss}")
