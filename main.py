nric = input('Enter an NRIC number: ').upper()
prefix = nric[0] in "STFG"
nums = nric[1:8].isdecimal()
suffix = nric[-1]

if nums:
  total_weight = int(nric[1]) * 2 + int(nric[2]) * 7 + int(nric[3]) * 6 + int(nric[4]) * 5 + int(nric[5]) * 4 + int(nric[6]) * 3 + int(nric[7]) * 2
else:
  total_weight = 0
if nric[0] in "TG":
  total_weight += 4


check_ST = "JZIHGFEDCBA"
check_FG = "XWUTRQPNMLK"

if nric[0] in "ST" and suffix == check_ST[total_weight % 11]:
  check_digit = True
elif nric[0] in "FG" and suffix == check_FG[total_weight % 11]:
  check_digit = True
else:
  check_digit = False

if prefix and nums and check_digit:
  print("NRIC is valid.")
else:
  print("NRIC is invalid.")
