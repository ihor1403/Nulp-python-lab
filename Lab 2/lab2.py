def total_with_discount(prices):

  total = 0
  discount = 0.4
  for i, price in enumerate(prices):
    if (i + 1) % 3 == 0:
      total += price - (price * discount)
    else:
      total += price
  return total

# prices = [100, 400, 300, 600, 500]
#
# total_without_discount = sum(prices)
# total_with_discount = total_with_discount(prices)
#
# print(f"Без знижки: {total_without_discount}")
# print(f"Зі знижкою: {total_with_discount}")
# print(f"Економія: {total_without_discount - total_with_discount}")