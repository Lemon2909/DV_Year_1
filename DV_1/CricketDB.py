win = {
    1975: "West Indies",
    1979: "West Indies",
    1983: "India",
    1987: "Australia",
    1992: "Pakistan",
    1996: "Sri Lanka",
    1999: "Australia",
    2003: "Australia",
    2007: "Australia",
    2011: "India",
    2015: "Australia",
    2019: "England",
    2023: "Australia"
}
l = list(win.values())
s = set(l)
high = 0 
max_country = "None"
for i in s : 
    count = 0
    for j in l : 
        if ( i == j):
            count += 1 
    if ( count > high ) : 
        max_country = i 
        high = count
print (max_country,"got the most wins")
print("A unique list of countries is given below : ")
for i in s : 
    print(i)

