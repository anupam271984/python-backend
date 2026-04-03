from time import gmtime, strftime

timeNow = strftime("%H")
timeNowInt = int(timeNow)
print('current time is inINT ',{timeNowInt})

match timeNowInt :
    case timeNowInt if 6<= timeNowInt < 12:
        print('----- Good Morning -----')

    case timeNowInt if 12<= timeNowInt < 15:
        print('----- Good Noon -----')

    case timeNowInt if 15<= timeNowInt < 18:
        print('----- Good After Noon -----')

    case timeNowInt if 18<= timeNowInt < 21:
        print('----- Good Evening -----')

    case timeNowInt if 21<= timeNowInt < 4:
        print('----- Good Night -----')