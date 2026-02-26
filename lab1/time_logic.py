totalseconds = int(input("Enter a large integer representing a total number of seconds "))
hours = totalseconds // 3600
minutes = (totalseconds % 3600) // 60
seconds = totalseconds % 60
print(str(totalseconds) + " seconds is " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds")
