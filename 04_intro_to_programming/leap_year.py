#newyear = int(input("Please enter a year: "))
for newyear in range(1900,2021):

    if newyear % 400 == 0 or (newyear % 4 == 0 and newyear % 100 != 0):  
        #print()
        print(f"The year {newyear} is  a  ==leaf year==")
    #else:
        #sleep (0)
        #print()
        #print(f'The year {newyear} is  NOT a  leaf year')
