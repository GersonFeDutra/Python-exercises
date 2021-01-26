from datetime import date

age: int = date.today().year - int(input('What year were you born? '))

if age <= 9:
    print('\033[37mLITTLE\033[m')

elif age <= 14:
    print('\033[36mCHILDISH\033[m')

elif age <= 19:
    print('\033[35mJUNIOR\033[m')

elif age <= 20:
    print('\033[34mSENIOR\033[m')

else:
    print('\033[33mMASTER\033[m')
