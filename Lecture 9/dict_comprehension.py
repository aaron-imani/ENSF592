oclahoma='oclahoma'
oclahoma_set=set(oclahoma)
histogram={i:sum(j==i for j in oclahoma) for i in oclahoma_set}
print(histogram)