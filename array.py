friends  = [("sabita ",12),
            ("madhuma ",19),
            ("afsar",21)]
age  = lambda data:data[1]>=18
drive_age =list( filter(age,friends))
for i in drive_age:
    print(i)
