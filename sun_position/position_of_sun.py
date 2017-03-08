# -*- coding: utf-8 -*-
"""
For help and explanantion of equations, open "postition_of_sun_class.py" 
and look to doc string.

"""
#import "position_of_the_sun_class" module that has all functions 
#for calculating solar position

import position_of_sun_class as ps

#=====================================================================

#Intro

print "\n\n\n     Welcome to The Position of the Sun Calculator!\
        \n\nCan be used for any Planet in the System!   ...and Pluto!\n"
        
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

print "Let's input the necessary information...\n\n\
Make sure to fill in values associated with time and location for when\n\
and where you wish to determine solar position and not current values\n\
for time and location, unless you wish to determine solar\n\
position for your current time and location... or you could\n\
just look out the window, up to you."

#=====================================================================

#Inputs for determining solar position, input prompts describe each input, as well as input format.
#If input incorrectly at any point, restart program


year = int(input ("What is the year (based on Gregorian Calendar)?\n\n")) 

month = int(input ("What is the month (based on Gregorian Calendar)?\n\n\
----Input as number\n\n"))

day = int(input ("What is the day of the month (based on Gregorian\n\
Calendar)?\n\n----Input as number\n\n"))

hour = int(input ("What is the hour?\n\n----Input as military time: example - \
1:00 pm = 13, 0 for Midnight\n\
----Does not account for Daylight Savings\n\
----If not on Earth, will automatically use UTC\n\n"))

minute = int(input ("What is the minute (0 through 59)?\n\n"))

planet = raw_input("What planet are we observing the Sun from?\n\n")

lat = input("What is the location's latitude (negative for south \
example: 45 degrees south equals -45)?\n\n")

if planet == "Earth":
    
    timezone = int(input("How many hours off of GMT (Greenwich Mean Time) is this\n\
location?\n\n----Denote negative value for west of GMT\n\
----For example, CST would be input as: -6\n\
----Does not account for Daylight Savings Time\n\
----Not sure of the timezone? Go here...\n\
----https://www.timeanddate.com/time/map/\n\n"))


    if timezone <= 0:
        
        #hem == hemisphere
        
        hem = False
        
    
    if hem is not True:
        
        lon = int(input("Ahh, I see we are in the Western Hemisphere, what degree west?\n\n"))

        
    else:
        
        lon = int(input("Ahh, I see we are in the Eastern Hemisphere, what degree east?\n\n"))

        lon = lon*(-1)
       
        

#Lines 79 through 143 changes local time to UTC if Earth is the planet selected.
#Will adjust hour, day, month and year as needed
        
    UTC_hour = hour - timezone
    if UTC_hour >= 24:
        UTC_hour = UTC_hour - 24
        UTC_day = day + 1
        if (month == 4 or 6 or 9 or 11) and UTC_day > 30:
            UTC_month = month + 1
            UTC_day = UTC_day - 30
            UTC_year = year
        elif (month == 1 or 3 or 5 or 7 or 8 or 10 or 12) and UTC_day > 31:
            UTC_month = month + 1
            UTC_day = UTC_day - 31
            UTC_year = year
            if UTC_month > 12:
                UTC_month = UTC_month - 12
                UTC_year = year + 1
        elif month == 2 and year%4 == 0 and UTC_day > 29:
            UTC_month = month + 1
            UTC_day = UTC_day - 29
            UTC_year = year
        elif month == 2 and year%4 != 0 and UTC_day > 28:
            UTC_month = month + 1
            UTC_day = UTC_day - 28
            UTC_year = year
        else:
            UTC_month = month
            UTC_year = year
                
    elif UTC_hour < 0:
        UTC_hour = UTC_hour + 24
        UTC_day = day - 1
        if (month == 5 or 7 or 10 or 12) and UTC_day <= 0:
            UTC_month = month - 1
            UTC_day = UTC_day + 30
            UTC_year = year
        elif (month == 2 or 4 or 6 or 8 or 9 or 11 or 1) and UTC_day <= 0:
            UTC_month = month - 1
            UTC_day = UTC_day + 31
            UTC_year = year
            if UTC_month <= 0:
                UTC_month = UTC_month + 12
                UTC_year = year - 1 
        elif month == 3 and year%4 == 0 and UTC_day <= 0:
            UTC_month = month - 1
            UTC_day = UTC_day + 29
            UTC_year = year
        elif month == 3 and year%4 != 0 and UTC_day <= 0:
            UTC_month = month - 1
            UTC_day = UTC_day + 28 
            UTC_year = year
        else:
            UTC_month = month
            UTC_year = year
    else:
        UTC_month = month
        UTC_year = year
        UTC_day = day
        
else:
    
    lon = int(input("Longitudinal degrees on planets \
other than Earth\n\
increase to 360 west of the meridian. What are the\n\
degrees west of the meridian?\n\n"))

    UTC_hour = hour
    UTC_day = day
    UTC_month = month
    UTC_year = year

#=======================================================================

#Starting calculations via functions within position_of_sun_class.py
#descriptions of equations and sources are listed in position_of_sun_class.py

instance = ps.Sun_Position(UTC_month,UTC_day,UTC_year,UTC_hour,minute,planet,lat,lon)

instance.mean_anomaly()
instance.EOC_func()
instance.eclip_coord_func()
instance.equat_coord_func()
instance.sidereal_time()
instance.hour_angle()
instance.altitude()
instance.azimuth()

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

print "\n\n\
Let's see what we got...\n\n\
On  ",month,"/",day,"/",year,"  at  ",hour,":",format(minute,'02d')," at",lat,"degrees latitude\
 and",lon,"degrees west of the longitudinal meridian on",planet,"\n"

if instance.alt >= 0:
    print "The center of the Sun is",instance.alt,"degrees above the horizon and",instance.azim,\
"degrees east of north"

else:
    instance.alt = instance.alt*(-1)
    print "The center of the Sun is not visible but is",instance.alt,"degrees below the horizon and"\
,instance.azim,"degrees east of north"
    
    




        
    
    
    
    



