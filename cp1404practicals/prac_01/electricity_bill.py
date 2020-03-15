TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity Bill Estimator")

tariff_choice = input("Which tariff? 11 or 31: ")
if tariff_choice == 11:
    price_per_kwh_in_cents = 0.244618
else:
    price_per_kwh_in_cents = 0.136928

daily_use_in_kwh = input("Enter daily use in kWh: ")
number_of_days = input("Enter number of billing days: ")
estimated_bill = float(price_per_kwh_in_cents) * float(daily_use_in_kwh) * float(number_of_days)
print("Estimated bill: $", estimated_bill)
