print "Tip Calculator"
bill = raw_input ("Enter your bill: $")
tip = raw_input ('Enter the tip in %: ')
bill_divided_by_tip = float(tip)/100.0
bill_times_tip = float(bill) * float(bill_divided_by_tip)
total = float(bill_times_tip) + float(bill)
total_in_dollars = '$' + str(total)
print format(total_in_dollars, '.10s')