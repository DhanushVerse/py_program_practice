# Multi Currency Calculator

def convert_to_usd(ruppees):
    convert_usd = ruppees / 83
    return convert_usd

amount_in_inr = int(input('Enter a amount in INR:'))
result_in_usd = convert_to_usd(amount_in_inr)
print('Your amount in USD is:',result_in_usd)



