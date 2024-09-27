This file is an example of how to web scrape data and save the data to a related azure sql database.

For the code to work you will have needed to set up an azure sql server, sql database and additionally create a .env file with the following variables

SERVER=XXX
DRIVER={ODBC Driver 18 for SQL Server} // or different driver you have installed and is set in the azure portal on the database.
DATABASE=XXX
USERNAME=XXX
PASSWORD=XXX
