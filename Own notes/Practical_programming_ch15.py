# Practical Programming Chapter 15 notes

# A database is a structure for storing and searching data, controlling who can view
# and modify data, and ensuring that data are correctly formatted.

# Database is a broad term for a bunch of different types of structures. Most
# popular are relational databases.

# The big picture
# A relational database is a collection of tables, each of which has a fixed
# number of columns and a variable number of rows. Each column in a table
# has a name and contains values of the same data type, such as integer or
# string. Each row contains values that are related to each other, such
# as a particular patient's hospital record.
# While each database table superficially looks like a spreadsheet, the database
# is doing a lot of work behind the scenes to keep track of which values are
# where and how the tables relate to one another. Oracle and MySQL are examples
# of databases.

# A database is usually stored in a file, or in a collection of files. You
# interact with the database either by:
# 1. Typing commans into a GUI, just as you type commands into a Python
# interpreter. This is only good for simple tasks.
# 2. Writing programs in Python (or another language).

# Database libraries work either by manipulating the database directly (rare!)
# or through a separate program called the database management system (DBMS).
# Python tries to hide the disparity between the two approaches by having
# every database-specific library implement the same application programming
# interface (API) - i.e., the same set of functions provided for programs to call.

# For example,
import sqlite3 as dbapi

# means "Find version 3 of the SQLite library, and import version 2 of the 
# database API from it using the name dbapi." We can change this to:
import MySQLdb as dbapi

# without affecting anything else in the program (all function are the same).

# To put data into or get data out of databases, we need to write SQL commands.
# However, each database has their own specific SQL dialect.

import sqlite3 as dbapi

# Create connection to database
con = dbapi.connect('population.db')

# Create cursor to keep track of where we are in the database.
cur = con.cursor()

# Creating a table
cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')

# Insert data into table
cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", 743112)')
cur.execute('INSERT INTO PopByRegion VALUES("Northern Africa", 1037463)')
cur.execute('INSERT INTO PopByRegion VALUES("Southern Asia", 2051941)')
cur.execute('INSERT INTO PopByRegion VALUES("Asia Pacific", 785468)')
cur.execute('INSERT INTO PopByRegion VALUES("Middle East", 687630)')
cur.execute('INSERT INTO PopByRegion VALUES("Eastern Asia", 1362955)')
cur.execute('INSERT INTO PopByRegion VALUES("South America", 593121)')
cur.execute('INSERT INTO PopByRegion VALUES("Eastern Europe", 223427)')
cur.execute('INSERT INTO PopByRegion VALUES("North America", 661157)')
cur.execute('INSERT INTO PopByRegion VALUES("Western Europe", 387933)')
cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')

# Commit the changes to memory
con.commit()

# Retrieving data
cur.execute('SELECT Region, Population FROM PopByRegion')

# Print one row at a time
print cur.fetchone() # Print text as unicode
con.text_factory = str
print cur.fetchone() # Print text as string

# Print all rows
cur.execute('SELECT Region, Population FROM PopByRegion')
print cur.fetchall()

# Print with ordering by column
cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Region')
print cur.fetchall()
cur.execute('SELECT Region, Population FROM PopByRegion ORDER BY Population DESC')
print cur.fetchall()

cur.execute('SELECT Region FROM PopByRegion')
print cur.fetchall()

cur.execute('SELECT * FROM PopByRegion')
print cur.fetchall()

# Query conditions (filtering by rows)
cur.execute('SELECT Region FROM PopByRegion WHERE Population > 1000000')
print cur.fetchall()

cur.execute('SELECT Region FROM PopByRegion WHERE Population > 1000000 \
AND Region < "L"')
print cur.fetchall()

# Updating and deleting
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
print cur.fetchone()
cur.execute('UPDATE PopByRegion SET Population = 100600 WHERE Region = "Japan"')
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
print cur.fetchone()

cur.execute('DELETE FROM PopByRegion WHERE Region < "L"')
cur.execute('SELECT * FROM PopByRegion');
print cur.fetchall()

cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')
cur.execute('DROP TABLE PopByRegion')

# Using NULL for Missing Data
cur.execute('INSERT INTO PopByRegion VALUES ("Mars", NULL)')
cur.execute('CREATE TABLE Test (Region TEXT NOT NULL, Population INTEGER)')
cur.execute('INSERT INTO Test VALUES (NULL, 456789)') # Will throw an error

# Use NULL with caution due to how it is interpreted with operations and
# across different databases.

# Using joins to combine tables
# Let's first recreate the PopByRegion table after dropping it
cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')

cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", 743112)')
cur.execute('INSERT INTO PopByRegion VALUES("Northern Africa", 1037463)')
cur.execute('INSERT INTO PopByRegion VALUES("Southern Asia", 2051941)')
cur.execute('INSERT INTO PopByRegion VALUES("Asia Pacific", 785468)')
cur.execute('INSERT INTO PopByRegion VALUES("Middle East", 687630)')
cur.execute('INSERT INTO PopByRegion VALUES("Eastern Asia", 1362955)')
cur.execute('INSERT INTO PopByRegion VALUES("South America", 593121)')
cur.execute('INSERT INTO PopByRegion VALUES("Eastern Europe", 223427)')
cur.execute('INSERT INTO PopByRegion VALUES("North America", 661157)')
cur.execute('INSERT INTO PopByRegion VALUES("Western Europe", 387933)')
cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')
con.text_factory = str
cur.execute('SELECT * FROM PopByRegion')
print cur.fetchall()

con.commit()

# Create a new table
cur.execute('CREATE TABLE PopByCountry(Region TEXT, Country TEXT, \
Population INTEGER)')
countries = [("Eastern Asia", "DPR Korea", 24056), 
             ("Eastern Asia", "Hong Kong (China)", 8764),
             ("Eastern Asia", "Mongolia", 3407),
             ("Eastern Asia", "Republic of Korea", 41491),
             ("Eastern Asia", "Taiwan", 1433),
             ("North America", "Bahamas", 368),
             ("North America", "Canada", 40876),
             ("North America", "Greenland", 43),
             ("North America", "Mexico", 126875),
             ("North America", "United States", 493038)]
for c in countries:
    cur.execute('INSERT INTO PopByCountry VALUES (?, ?, ?)',
                (c[0], c[1], c[2]))
con.text_factory = str
cur.execute('SELECT * FROM PopByCountry')
print cur.fetchall()

# Getting the names of the countries in regions where projected population 
# > 1000000

cur.execute('''
SELECT PopByRegion.Region, PopByCountry.Country
FROM PopByRegion INNER JOIN PopByCountry
WHERE (PopByRegion.Region = PopByCountry.Region)
AND (PopByRegion.Population > 1000000)
''')
print cur.fetchall()

# What regions have a country that accounts for more than 10% of overall
# population?
cur.execute('''
SELECT PopByRegion.Region
FROM PopByRegion INNER JOIN PopByCountry
WHERE (PopByRegion.Region = PopByCountry.Region)
AND ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)
''')
print cur.fetchall()

# The same command getting rid of duplicates
cur.execute('''
SELECT DISTINCT PopByRegion.Region
FROM PopByRegion INNER JOIN PopByCountry
WHERE (PopByRegion.Region = PopByCountry.Region)
AND ((PopByCountry.Population * 1.0) / PopByRegion.Population > 0.10)
''')
print cur.fetchall()

# Keys
cur.execute('CREATE TABLE PopByRegion (Region TEXT NOT NULL, \
Population INTEGER NOT NULL, PRIMARY KEY (Region))')

# Key made up from multiple columns (no two rows will have the same value
# for region and country)

cur.execute('''
CREATE TABLE PopByCountry(
Region TEXT NOT NULL,
Country TEXT NOT NULL
Population INTEGER NOT NULL,
CONSTRAINT Country_Key PRIMARY KEY (Region, Country))
''')

# Foreign keys are keys that are not guaranteed to be unique in this table
# but are unique in another table (e.g., hospital name in patient table versus
# hospital table).

# Aggregation
# E.g., calcuate the total projected world population for the year 2300.
cur.execute('SELECT SUM (Population) FROM PopByRegion')
print cur.fetchone()

# Grouping
cur.execute('SELECT SUM (Population) FROM PopByCountry GROUP BY Region')
print cur.fetchall()

# Self-joins
# E.g., finding pairs of countries whose populations are close to one another

cur.execute('''
SELECT A.Country, B.Country
FROM PopByCountry A INNER JOIN PopByCountry B
WHERE (ABS(A.Population - B.Population) <= 1000)
AND (A.Country != B.Country)
''')
print cur.fetchall()

# OR (getting rid of duplicates):
cur.execute('''
SELECT A.Country, B.Country
FROM PopByCountry A INNER JOIN PopByCountry B
WHERE (ABS(A.Population - B.Population) <= 1000)
AND (A.Country < B.Country)
''')
print cur.fetchall()

# Nested queries

cur.execute('''
SELECT DISTINCT Region
FROM PopByCountry
WHERE Region NOT IN
(SELECT DISTINCT Region
FROM PopByCountry
WHERE (PopByCountry.Population = 8764))
''')
print cur.fetchall()