import numpy as np

# Bond parameters
face_value = 1000
coupon_rate = 0.10
yield_rate = 0.12
maturity = 5
payments_per_year = 2

# Derived values
coupon_payment = face_value * coupon_rate / payments_per_year
period_yield = yield_rate / payments_per_year
total_periods = maturity * payments_per_year

# Cash flows
cash_flows = [coupon_payment] * total_periods
cash_flows[-1] += face_value

# Present value of cash flows
price = 0
present_values = []

for t, cash_flow in enumerate(cash_flows, start=1):
    pv = cash_flow / (1 + period_yield) ** t
    present_values.append(pv)
    price += pv

# Macaulay duration
weighted_times = []

for t, pv in enumerate(present_values, start=1):
    weighted_times.append(t * pv)

macaulay_duration_periods = sum(weighted_times) / price
macaulay_duration_years = macaulay_duration_periods / payments_per_year

# Modified duration
modified_duration = macaulay_duration_years / (1 + yield_rate / payments_per_year)

# Convexity
convexity_numerator = 0

for t, cash_flow in enumerate(cash_flows, start=1):
    convexity_numerator += (t * (t + 1) * cash_flow) / (1 + period_yield) ** (t + 2)

convexity = convexity_numerator / (price * payments_per_year ** 2)

# Output
print("Bond price:", round(price, 2))
print("Macaulay duration (years):", round(macaulay_duration_years, 4))
print("Modified duration:", round(modified_duration, 4))
print("Convexity:", round(convexity, 4))
