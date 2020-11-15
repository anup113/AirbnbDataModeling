
"""
@author: anup adhikari
"""

import mysql.connector
import csv

# database credentials goes here
hostname = "localhost"
username = "root"
password = "Root@123"
dbname = "airbnb"


# establish a database conneciton
mydb = mysql.connector.connect(
    host = hostname,
    user = username,
    passwd = password,
    database = dbname
)

#set a cursor
mycursor = mydb.cursor()

"""
Let's create the tables
    1. address table: contains all the address which are either mentioned in either host loacation
        host neighborhood or listing neighborhood 
    2. host table: contains information about each host
    3. listing table: contains information about each listing

    Note: while creating the table please maintain the following order
"""

# Drop table in following order
mycursor.execute("DROP TABLE IF EXISTS Listing")
mycursor.execute("DROP TABLE IF EXISTS Host")
mycursor.execute("DROP TABLE IF EXISTS Address")

# cteate address table
sql_create_address_table = """
    CREATE TABLE Address(
        addressId int NOT NULL,
        addressName varchar(55),
        PRIMARY KEY(addressId)
    )
"""
mycursor.execute(sql_create_address_table)
print("----------------------Address Table Created----------------------")

# creata host table
sql_create_host_table = """
    CREATE TABLE Host(
        hostId int NOT NULL, 
        hostName varchar(60) NOT NULL, 
        hostSince datetime, 
        hostResponseRate float, 
        hostIdentityVerified boolean, 
        hostHasProfilePic boolean, 
        hostLocationId int, 
        hostAbout varchar(1050), 
        hostAcceptanceRate float, 
        hostIsSuperHost boolean,
        hostNeighborhoodId int,
        hostCTL int, 
        PRIMARY KEY(hostId),
        FOREIGN KEY(hostLocationId) REFERENCES Address (addressId),
        FOREIGN KEY(hostNeighborhoodId) REFERENCES Address (addressId))
"""
mycursor.execute(sql_create_host_table)
print("-----------------------Host table Created------------------------")

# create listing table
sql_create_listing_table = """
    CREATE TABLE Listing(
        listingId int NOT NULL, 
        listingUrl varchar(150), 
        pictureUrl varchar(150), 
        description varchar(1000), 
        latitude float, 
        longitude float, 
        propertyType varchar(55),
        roomType varchar(50),
        accommodates int, 
        bedroom float, 
        price float,
        minimumNights int,
        reviewScoresRating float,
        reviewScoresAccuracy float,
        reviewScoresValue float,
        instantBookable boolean,
        reviewPerMonth float,
        neighborhoodCleansedId int,
        hostId int,
        PRIMARY KEY(listingId),
        FOREIGN KEY(hostId) REFERENCES Host(hostId),
        FOREIGN KEY(neighborhoodCleansedId) REFERENCES Address (addressId))
"""
# execute create table
mycursor.execute(sql_create_listing_table)
print("----------------------Listing Table Created----------------------")

hostpath = './host-airbnb.csv'
listingpath = './listing-airbnb.csv'
addresspath = './address-airbnb.csv'

# function to populate address table
def insert_data_address(path, mydb):
    with open(path) as csvfile:
        loaddata = csv.reader(csvfile, delimiter=',')

        first = True

        #sql statement to insert data into address table
        sql_insert = ("INSERT INTO Address"
        "(addressId, addressName)"
        "VALUES(%s, %s)"
        )

        # populate address table
        for row in loaddata:
            # do nothing for first row
            if first == True:
                first = False
                print(row)
                print(len(row))
                continue
            else:
                # checking
                # some rows are corrupted
                if(len(row)) == 2:
                    # print(row)
                    record = []
                    record.append(int(row[0]))
                    record.append(row[1])
                    # crs = mydb.cursor()
                    # crs.execute(sql_insert, record)
                    try:
                        crs = mydb.cursor()
                        crs.execute(sql_insert, record)
                        mydb.commit()
                    except:
                        print("Exception Occured")
                        continue
                else:
                    continue
        print("----------------Data populated in Address Table----------------")

#
def insert_data_host(path, mydb):
    with open(path) as csvfile:
        loaddata = csv.reader(csvfile, delimiter=',')

        first = True

        # sql statement to insert data into host table
        sql_insert = ( "INSERT INTO Host "
        "( hostId, hostName, hostSince, hostResponseRate, hostIdentityVerified, hostHasProfilePic, hostAbout, hostAcceptanceRate, hostIsSuperhost, hostCTL, hostLocationId, hostNeighborhoodId)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )

        # load data in host table
        for row in loaddata:
            # do nothing for first row
            if first == True:
                first = False
                print(row)
                continue
            else:
                if len(row) == 12:
                    record = []
                    record.append(int(row[0]))
                    record.append(row[1])
                    record.append(row[2])
                    record.append(float(row[3]))
                    record.append(bool(row[4]))
                    record.append(bool(row[5]))
                    record.append(row[6])
                    record.append(float(row[7]))
                    record.append(bool(row[8]))
                    record.append(int(row[9]))
                    record.append(float(row[10]))
                    record.append(float(row[11]))
                    try:
                        crs = mydb.cursor()
                        crs.execute(sql_insert, record)
                        mydb.commit()
                    except:
                        print("Exception Occured")
                        continue
                else:
                    continue
        print("----------------Data populated in Host Table----------------")

def insert_data_listing(path, mydb):
    with open(path) as csvfile:
        loaddata = csv.reader(csvfile, delimiter=',')

        first = True

        # sql statement to insert data into host table
        sql_insert = (" INSERT INTO Listing "
        "(listingId, listingUrl, pictureUrl, description, latitude, longiture, propertyTyoe, roomType, accommodates, bedrooms, beds, price"
        "minimumNights, reviewScoresRating, reviewScoresAccuracy, reviewScoresValue, instantBookable, reviewPerMonth, hostId, neighborhoodCleansedId)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )

        # load data in host table
        for row in loaddata:
            # do nothing for first row
            if first == True:
                first = False
                print('First time')
                print(len(row))
                continue
            else:
                if len(row) == 20:
                    record = []
                    record.append(int(row[0]))
                    record.append(row[1])
                    record.append(row[2])
                    record.append(row[3])
                    record.append(float(row[4]))
                    record.append(float(row[5]))
                    record.append(row[6])
                    record.append(row[7])
                    record.append(int(row[8]))
                    record.append(float(row[9]))
                    record.append(float(row[10]))
                    record.append(float(row[11]))
                    record.append(int(row[12]))
                    record.append(float(row[13]))
                    record.append(float(row[14]))
                    record.append(float(row[15]))
                    record.append(bool(row[16]))
                    record.append(float(row[17]))
                    record.append(int(row[18]))
                    record.append(int(row[19]))
                    try:
                        crs = mydb.cursor()
                        crs.execute(sql_insert, record)
                        mydb.commit()
                    except:
                        print("Exception Occured")
                        continue
                else:
                    continue
        print("----------------Data populated in Listing Table----------------")


# populate Address table at first
insert_data_address(addresspath, mydb)
# populate Host table at second
insert_data_host(hostpath, mydb)
# finally, populate lisitng table
insert_data_listing(listingpath, mydb)


# # fetch the data into cursor
# mycursor.execute('SELECT * FROM Host')

# # iterate over the cursor to print the fetched data
# for i in mycursor:
#     print(i)
#     break


