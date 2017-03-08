# -*- coding: utf-8 -*-
"""
Position of Sun Class

Class for Determining the Sun's Position in the Sky from Any Planet in our Solar System (and Pluto)

mean_anomaly function:
    
    Planetary Mean Anomaly Function (within our Solar System)
    Now with Gregorian to Julian Day Number Conversion!!!
        created by Patrick O'Hara
    All equations and values taken from 
        http://aa.quae.nl/en/reken/zonpositie.html 
     
EOC_func function:

    The Equation of Center Function (for planets within our Solar System & Pluto)
    Now determines value for true anomoly!!! -
        created by Patrick O'Hara
    All equations and values taken from 
        http://aa.quae.nl/en/reken/zonpositie.html 
         
eclip_coord_func and equat_coord_func function:

    The Ecliptical & Equatorial Coordinates Functions (for planets within our Solar System & Pluto)
        created by Patrick O'Hara
    All equations and values taken
        from http://aa.quae.nl/en/reken/zonpositie.html 
    Additional website explaining right-ascention and declination
        http://astro.unl.edu/naap/motion1/cec_units.html
        
sidereal_time, hour_angle, altitude and azimuth function:
    
    The Observer Functions - calculating Sidereal Time, Hour Angle, Altitiude & Azimuth  (for planets within our solar system & Pluto)
        created by Patrick O'Hara
    All equations and values taken from
        http://aa.quae.nl/en/reken/zonpositie.html 
"""

#numpy imported for triginometric functions, converting degrees to radians/radians to degrees
#as well as the floor function

import numpy as np

 
class Sun_Position:
    
    def __init__(self,month,day,year,hour,minute,planet,lat,lon):
        self.month = month
        self.day = day
        self.year = year
        self.hour = hour
        self.minute = minute
        self.planet = planet
        self.lat = lat
        self.lon = lon
 
 
    def mean_anomaly(self):
        
        #for an in-depth description of the mean anomaly and Julian Day Number (JDN)
        #go to http://aa.quae.nl/en/reken/zonpositie.html
     
        a = np.floor((14-self.month)/12)
        y = self.year + 4800 - a #years since March 1, 4801 B.C.
        m = self.month + 12*a - 3 #months since last occurence of March 1st
        t = (self.hour-12.0)/24.0 + self.minute/1440.0 #calculates fraction of day complete for
        #the given time
        
        # Julian Day Number (days since March 1, 4801 B.C.)   
        self.julian = t + self.day + np.floor((153*m+2)/5) + 365*y + np.floor(y/4) - np.floor(y/100) + np.floor(y/400) - 32045 
    
        # epoch = mean anomaly at epoch
        # motion = mean angular motion
    
        epoch = {'Mercury':174.7948,'Venus':50.4161,'Earth':357.5291,'Mars':19.3730,
              'Jupiter':20.0202,'Saturn':317.0207,'Uranus':141.0498,
              'Neptune':256.2250,'Pluto':14.882}
    
        motion = {'Mercury':4.09233445,'Venus':1.60213034,'Earth':0.98560028,'Mars':0.52402068,
              'Jupiter':0.08308529,'Saturn':0.03344414,'Uranus':0.01172834,
              'Neptune':0.00598103,'Pluto':0.00396}
              
    
        # Mean Anomaly Equation were M equals mean anomaly
        # 2451545 is the Julian Day Number at epoch
    
        self.mean_anom = np.deg2rad((epoch[self.planet] + motion[self.planet]*(self.julian - 2451545))%360)
     
     
        return self.mean_anom, self.julian
         
    def EOC_func(self):
        #for an in-depth description of the Equation of Center and true anomaly
        #go to http://aa.quae.nl/en/reken/zonpositie.html
        
    
        #Constants for The Equation of Center 
    
        con_one = {'Mercury':23.4400,'Venus':0.7758,'Earth':1.9148,'Mars':10.6912,
              'Jupiter':5.5549,'Saturn':6.3585,'Uranus':5.3042,
              'Neptune':1.0302,'Pluto':28.3150}
        con_two = {'Mercury':2.9818,'Venus':0.0033,'Earth':0.0200,'Mars':0.6228,
              'Jupiter':0.1683,'Saturn':0.2204,'Uranus':0.1534,
              'Neptune':0.0058,'Pluto':4.3408}
        con_three = {'Mercury':0.5255,'Venus':0,'Earth':0.0003,'Mars':0.0503,
              'Jupiter':0.0071,'Saturn':0.0106,'Uranus':0.0062,
              'Neptune':0,'Pluto':0.9214}
        con_four = {'Mercury':0.1058,'Venus':0,'Earth':0,'Mars':0.0046,
              'Jupiter':0.0003,'Saturn':0.0006,'Uranus':0.0003,
              'Neptune':0,'Pluto':0.2235}
        con_five = {'Mercury':0.0241,'Venus':0,'Earth':0,'Mars':0.0005,
              'Jupiter':0,'Saturn':0,'Uranus':0,
              'Neptune':0,'Pluto':0.0627}
        con_six = {'Mercury':0.0055,'Venus':0,'Earth':0,'Mars':0,
              'Jupiter':0,'Saturn':0,'Uranus':0,
              'Neptune':0,'Pluto':0.0174}
              
        #self.EOC_val = the equation of center value
    
        self.EOC_val = ((np.deg2rad(con_one[self.planet])*np.sin(self.mean_anom))+(np.deg2rad(con_two[self.planet])*np.sin(2*self.mean_anom))+
              (np.deg2rad(con_three[self.planet])*np.sin(3*self.mean_anom))+(np.deg2rad(con_four[self.planet])*np.sin(4*self.mean_anom))+
              (np.deg2rad(con_five[self.planet])*np.sin(5*self.mean_anom))+(np.deg2rad(con_six[self.planet])*np.sin(6*self.mean_anom)))
    
        #self.tru_anom = true anomoly
    
        self.tru_anom = self.mean_anom + self.EOC_val
    
    
        return self.tru_anom, self.EOC_val
        
    def eclip_coord_func(self):
        #for an in-depth description of the Ecliptical Coordinates
        #go to http://aa.quae.nl/en/reken/zonpositie.html
        
        #perihelion = ecliptic longitude of the periheion
        #(the perihelion is the point in orbit when the planet is closest to the sun)
        perihelion = {'Mercury':230.3265,'Venus':73.7576,'Earth':102.9373,'Mars':71.0041,
              'Jupiter':237.1015,'Saturn':99.4587,'Uranus':5.4634,'Neptune':182.2100,'Pluto':184.5484}

        #self.eclip_coord = Ecliptical longitude (ecliptical latitude is negligible) 
        self.eclip_coord = np.deg2rad((np.rad2deg(self.tru_anom) + perihelion[self.planet]+180)%360)
    
        return self.eclip_coord

    def equat_coord_func(self):
        #for an in-depth description of the Equatorial Coordinates
        #go to http://aa.quae.nl/en/reken/zonpositie.html
        
        #equat_obliq = obliquity of the ecliptic
        equat_obliq = {'Mercury':0.0351,'Venus':2.6376,'Earth':23.4393,'Mars':25.1918,
                       'Jupiter':3.1189,'Saturn':26.7285,'Uranus':82.2298,
                       'Neptune':27.8477,'Pluto':119.6075}
        
        #self.right_ascen = right ascention of the Sun
        self.right_ascen = np.arctan2(np.sin(self.eclip_coord)*np.cos(np.deg2rad(equat_obliq[self.planet])),np.cos(self.eclip_coord))

        #self.declination = declination of the Sun
        self.declination = np.arcsin(np.sin(self.eclip_coord)*np.sin(np.deg2rad(equat_obliq[self.planet])))
    
    
        return self.right_ascen, self.declination
        
    def sidereal_time(self):
        #for an in-depth description of Sidereal time
        #go to http://aa.quae.nl/en/reken/zonpositie.html
        
        #theta_zero = sidereal time at epoch
        theta_zero = {'Mercury':132.3282,'Venus':104.9067,'Earth':280.1470,'Mars':313.3827,
              'Jupiter':145.9722,'Saturn':174.3508,'Uranus':29.6474,
              'Neptune':52.4160,'Pluto':122.2370}
        
        #theta_one = rate of sidereal time per day
        theta_one = {'Mercury':6.1385025,'Venus':-1.4813688,'Earth':360.9856235,'Mars':350.89198226,
              'Jupiter':870.5360000,'Saturn':810.7939024,'Uranus':-501.1600928,
              'Neptune':536.3128662,'Pluto':56.3625225}
        
        #self.sreal = sidereal time in degrees
        self.sreal = (theta_zero[self.planet]+(theta_one[self.planet]*(self.julian-2451545))-(self.lon))%360
        
        #converts sidereal time to radians
        self.sreal = np.deg2rad(self.sreal)
        
        return self.sreal
        
    def hour_angle(self):
        #for an in-depth description of hour angle
        #go to http://aa.quae.nl/en/reken/zonpositie.html
        
        #self.h_angle= hour angle in radians
        self.h_angle = self.sreal - self.right_ascen
        
        return self.h_angle
        
    def altitude(self):
        #altitude is the angle the sun is above the horizon
        #for more information go to http://aa.quae.nl/en/reken/zonpositie.html
        
        #self.alt = altitude
        self.alt = np.arcsin((np.sin(np.deg2rad(self.lat))*np.sin(self.declination))+(np.cos(np.deg2rad(self.lat))*np.cos(self.declination)*np.cos(self.h_angle)))
        
       
        #altitude converted back to degrees        
        self.alt = np.rad2deg(self.alt)
        
        return self.alt
        
    def azimuth(self):
        #azimuth is compass position of the sun
        #for more information go to http://aa.quae.nl/en/reken/zonpositie.html
        
        #self.azim = azimuth
        self.azim = np.arctan2(np.sin(self.h_angle),(np.cos(self.h_angle)*np.sin(np.deg2rad(self.lat))-(np.tan(self.declination)*np.cos(np.deg2rad(self.lat)))))
        
        #azimuth function gives radians from south, switch to north and degrees for compass
        #convention
        self.azim = (np.rad2deg(self.azim)+180)%360
        
        return self.azim
        
        
        
        
        
        