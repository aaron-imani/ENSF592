oclahoma='oclahoma'
oclahoma_set=set(oclahoma)
histogram={i:sum(j==i for j in oclahoma_set) for i in oclahoma}
print(histogram)