print("Enter start year")
startyear=int(input())
print("Enter last year")
endyear=int(input())
print("list of leap year")
for year in range(startyear,endyear):
    if(0==year%4)and(0!=year%100)or(0==year%400):
        print(year)
