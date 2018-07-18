# Encyclogenia

ENCYCLOGENIA UPDATE GUIDE

Step 1: Acquire the name of the publication from Prof. Schroeder

Step 2: Search for the publication on NCBI: https://www.ncbi.nlm.nih.gov/pmc/

Step 3: Click on the GEO Datasets link

 

Step 4: Download the Series Matrix text file

 

Step 5: Download the tar.gz file and uncompress it to get the raw txt file

 

Step 6: Use excel to import the txt file into a formatted csv file. Click on the Data tab, choose the “From Text” import option and press enter to skip through the formatting steps

 

Step 7: Manually enter the information from the file into a new excel file. Have each sheet represent a sample and use the format shown. Not all matrix files may have their information in the same format but it should be similar to the example below

DO NOT WORRY ABOUT GETTING THE ATGMXXXX LOCUS VALUE. THE ASSOCAITION TABLE FOR LOCUS TO PROBE VALUE IS BUILT INTO THE DATABASE AND WILL HANDLE EVERYTHING AS LONG AS YOU FOLLOW FORMATTING

Matrix file from GEO:

 





Formatted file that you will make: 

 

Step 8: After formatting everything into their respective csv files, use a software of your choice (I used SQLizer.io) to convert the csv file into SQL insert statements. The database is built using MySQL although the variant should not matter.

One example of a valid software for conversion: https://sqlizer.io/#/

The software should return a .SQL file with content like the following:

 

Step 9: SSH into the server and enter the command “mysql -u root -p” and enter the password “4aGuP.Ta” to access the MySQL database. Enter “use gene_dictionary;” to enter the specific data base. Create a table matching the name of the publication you are entering the data for. You can look up the command for table creation and other simple SQL commands anywhere online. 

Standard table variable formats for the database:

 

Step 10: Once the table has been created with the proper name and formatting, copy and paste the entire contents of each .SQL file into the MySQL prompt. This will populate the database and each full insert will take some time. This is a good step to do in the background of other work. Maybe put on a movie or something

Step 11: Once the database has been populated, you will need to create corresponding query statements within the python script so that these databases will be properly queried when the script is run

Block of code responsible for query commands (follow the template):

 



Block of code responsible for writing each query result to a csv file:

 
