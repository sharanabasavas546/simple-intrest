p-float(input("Enter Principle amount:"))
r-float(input("Enter rate of interest:"))
t-int(input("Enter time (in years):"))
si-(p*t*r)/100
print("Simple interest is:",si)
ci=p*((1+r/100)**t)-p
print("compund interest is :",ci)
