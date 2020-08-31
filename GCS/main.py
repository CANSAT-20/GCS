import sqlite3
import traceback
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from decimal import Decimal

from Database.database import Database
from ParseData.parsedata import Parse


conn = sqlite3.connect("test.db")
print('opened successfully')
database = Database()
parse = Parse()
parse1 = Parse()



while(1):
    print('\n1. Create table\n2. Insert data\n3. Display\n4. Drop Table\n5. Parse\n6. Store the data\n7. Plot Graph\n8. Exit\n')
    ch = int(input("Enter ur choice: "));
    if(ch == 1):
        database.create_table(conn)
    elif(ch == 2):
        database.insert_into_table(conn)
    elif(ch == 3):
        database.display_data(conn)
    elif(ch == 4):
        database.drop_table(conn)
    elif(ch == 5):
        count = 0
        flag = False
        cursor = database.pointer_to_rows(conn)
        for rows in cursor:
            count+=1
            print('\nData ',count)
            print('\nAltitude: ',parse.get_altitude(rows[1]))
            print('\nGPS_Latitude: ',parse.get_gps_latitude(rows[1]))
            print('\nGPS_Longitude: ',parse.get_gps_longitude(rows[1]))
            print('\nGPS_Altitude: ',parse.get_gps_altitude(rows[1]))
    elif(ch == 6):
        print("\n1. Store the altitude plots\n2. Store the GPS Latitude plots\n3. Store the GPS Longitude plots\n4. Store the GPS Altitude plots\n")
        ch1 = int(input("\nEnter your sub choice: "))
        if(ch1 == 1):
            count = 0
            f = open("alt_file.txt", "w")
            cursor1 = database.pointer_to_rows(conn)
            for rows1 in cursor1:
                count+=1
                f.write(str(count)+","+str(parse.get_altitude(rows1[1]))+"\n")
        elif(ch1==2):
            count = 0
            f = open("gps_lat_file.txt", "w")
            cursor1 = database.pointer_to_rows(conn)
            for rows1 in cursor1:
                count+=1
                f.write(str(count)+","+str(parse.get_gps_latitude(rows1[1]))+"\n")
        elif(ch1==3):
            count = 0
            f = open("gps_lon_file.txt", "w")
            cursor1 = database.pointer_to_rows(conn)
            for rows1 in cursor1:
                count+=1
                f.write(str(count)+","+str(parse.get_gps_longitude(rows1[1]))+"\n")
        elif(ch1==4):
            count = 0
            f = open("gps_alt_file.txt", "w")
            cursor1 = database.pointer_to_rows(conn)
            for rows1 in cursor1:
                count+=1
                f.write(str(count)+","+str(parse.get_gps_altitude(rows1[1]))+"\n")


    elif(ch == 7):
        print("\n1. Plot Altitude plots\n2. Plot GPS Latitude\n3. Plot GPS Longitude\n4. Plot GPS Altitude \n")
        ch = int(input("\nEnter Sub choice: "))
        if(ch == 1):
            style.use('fivethirtyeight')
            fig = plt.figure()
            fig.suptitle('Altitude')

            axis = fig.add_subplot(1,1,1)
            def animate(i):
                g_data = open('alt_file.txt',"r")
                lines = g_data.readlines()
                xarr = []
                yarr = []
                for line in lines:
                    if len(line) > 1:
                        x = line.split(',')
                        xarr.append(Decimal(x[0]))
                        yarr.append(Decimal(x[1]))
                axis.clear()
                axis.plot(xarr, yarr)
                axis.set_ylabel('Altitude', fontsize=10)
            ani = animation.FuncAnimation(fig, animate, interval=1000)
            plt.show()
        if(ch == 2):
            style.use('fivethirtyeight')
            fig = plt.figure()
            fig.suptitle('GPS Latitude')

            axis = fig.add_subplot(1,1,1)
            def animate(i):
                g_data = open('gps_lat_file.txt',"r")
                lines = g_data.readlines()
                xarr = []
                yarr = []
                for line in lines:
                    if len(line) > 1:
                        x = line.split(',')
                        xarr.append(Decimal(x[0]))
                        yarr.append(Decimal(x[1]))
                axis.clear()
                axis.plot(xarr, yarr)
                axis.set_ylabel('GPS Latitude', fontsize=10)
            ani = animation.FuncAnimation(fig, animate, interval=1000)
            plt.show()
        if(ch == 3):
            style.use('fivethirtyeight')
            fig = plt.figure()
            fig.suptitle('GPS Longitude')
            axis = fig.add_subplot(1,1,1)
            def animate(i):
                g_data = open('gps_lon_file.txt',"r")
                lines = g_data.readlines()
                xarr = []
                yarr = []
                for line in lines:
                    if len(line) > 1:
                        x = line.split(',')
                        xarr.append(Decimal(x[0]))
                        yarr.append(Decimal(x[1]))
                axis.clear()
                axis.plot(xarr, yarr)
                axis.set_ylabel('GPS Longitude', fontsize=10)
            ani = animation.FuncAnimation(fig, animate, interval=1000)
            plt.show()
        if(ch == 4):
            style.use('fivethirtyeight')
            fig = plt.figure()
            fig.suptitle('GPS Altitude')
            axis = fig.add_subplot(1,1,1)
            def animate(i):
                g_data = open('gps_alt_file.txt',"r")
                lines = g_data.readlines()
                xarr = []
                yarr = []
                for line in lines:
                    if len(line) > 1:
                        x = line.split(',')
                        xarr.append(Decimal(x[0]))
                        yarr.append(Decimal(x[1]))
                axis.clear()
                axis.plot(xarr, yarr)
                axis.set_ylabel('GPS Altitude', fontsize=10)
            ani = animation.FuncAnimation(fig, animate, interval=1000)
            plt.show()
    elif(ch == 8):
        break
    else:
        print('Invalid Choice')
        continue
conn.close()
