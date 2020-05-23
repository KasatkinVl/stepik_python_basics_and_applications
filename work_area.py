import csv, collections, time

with open("C:\\Users\\User\\Downloads\\Crimes.csv") as Cr:
    crime_list = list(csv.DictReader(Cr))
    # print(crime_list)

    res = []

    for i in range(len(crime_list)):
        # print(crime_list[i]['Date'])
        crime_list[i]['Date'] = time.strptime(crime_list[i]['Date'], "%m/%d/%Y %H:%M:%S %p")
        if crime_list[i]['Date'][0] == 2015:
            res.append(crime_list[i])

ans = []
for i in range(len(res)):
    del res[i]['Date']
    ans.append(res[i]['Primary Type'])
    # print(res)
    # print(collections.Counter(res[i]['Primary Type']).most_common(1))

# print(ans)


print(collections.Counter(ans).most_common(1))

