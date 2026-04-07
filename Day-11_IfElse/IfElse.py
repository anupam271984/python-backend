from time import gmtime, strftime
strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
print(strftime) # <built-in function strftime>
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())) # Fri, 20 Mar 2026 04:03:31 +0000 
print(strftime("%a, %d %b %Y %H:%M:%S +0000")) #  Fri, 20 Mar 2026 09:44:16 +0000

currentTime = strftime("%I,%H:%M:%S")
#currentTimeInt = int(currentTime)
print('current time is ',{currentTime})

timeNow = strftime("%H")
timeNowInt = int(timeNow)
print('current time is inINT ',{timeNowInt})

if timeNowInt >= 6 and timeNowInt <= 12:
    print('Good Morning')

elif 12 > timeNowInt < 15 :
    print('Good Noon')

elif 15 <= timeNowInt < 18:
    print('Good After Noon')

elif 18 <= timeNowInt < 21:
    print('Good Evening')

else: 21 <= timeNowInt < 4 
print('Good Night')
