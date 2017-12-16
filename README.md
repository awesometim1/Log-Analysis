# Log Analysis 
---
## Summary

Log Analysis is a tool for a fictional news site sql database. It uses relationships between tables within the database to extract the exact information that an end user needs. For example, the first functionality is implemented using subqueries and relating articles to log and accessing the number of get requests made for a certain sub domain. It does this by first extracting the article "slug" from log and using that subquery to count how many views a certain article received. A visual diagram of this database can be found below.

## Main Functions of this tool

1. Finds the number of views for each article and lists them in order (most popular first)

2. Finds the number of views that each author received and lists them in order(most views first)

3. Finds a date where more than 1% of the requests led to errors


**The SQL Database Diagram**

**News** (Main)

| Name    |
|:---:   |
|articles|
|authors |  
|log     |

**Articles**

| Name| Type | 
|:---:|:---:|
|author| integer|
|title | text|
|slug| text|
|lead| text|
|body| text|
|time | timestamp|
|id | integer|

**Authors**

| Name| Type | 
|:---:|:---:|
|name| text|
|bio | text|
|id | integer|

**Log**

| Name| Type | 
|:---:|:---:|
|path| text|
|ip| inet|
|method| text|
|status| text|
|time | timestamp|
|id | integer|

## Installation 

Log Analysis uses `psql`, `python`, and the `psycopg2` module for python

### Required Files and Programs
1. Vagrant  --- [Download Here](https://www.vagrantup.com/downloads.html)
2. FSND-Virtual-Machine.zip --- [Download here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
3. newsdata.sql --- [Download here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
**Place the newsdata.sql file into the FSND-Virtual_Machine folder created by unzipping the zip file.**

To Install:

1. `pip install psql`
2. `pip install python3`
3. `pip install psycopg2`



## Usage 

To Use:

1. Open Terminal
2. Navigate to the FSND-Virtual-Machine Folder
3. Navigate to the vagrant folder (Use `cd`)
4. Use the command `vagrant up` 
5. Then log in using `vagrant ssh`
6. `cd` into the vagrant directory and use this command to create and load the news database: `psql -d news -f newsdata.sql`
7. Type in the following command: `python3 news.py`

If done correctly, you will see the intended output! (**sample output can be found in this repository as a file named loganalysisoutput.txt**)

## Program Design 

1. Python: 

	Connected to psql database using python's psycopg module and commands such as:
	1. connect()
	2. cursor()
	3. execute()
	4. fetchall()
	5. close()

2. SQL: 

#### Finding the top 3 article rankings
	1. Subquery that finds the accessed path and extracts article "slug".

	2. Main query to count where the accessed slug matches article slug and group by title of the article order by count descending.

#### Finding author rankings
	1. Subquery that finds the accessed path and extracts article "slug".

	2. Main query that counts where the article slug matches the extracted slug and where the article author matches author's id, grouped by author name and ordered by num descending.

#### Finding dates with error percentage of more than 1%
	1. Subquery that extracts date from the timestamp and also sums up the http requests by their type (only 2: 200 OK and 404 NOT FOUND) then groups them by date requested.

	2. Main Query that first converts the date extracted to Mont, DD YYYY format and performs an arithmetic that goes as follows: 404 Requests / (TOTAL# OF REQUESTS) then groups them by date and percentage values and orders by percentage values descending. Also limits to the top 1 result.


## --Tim Lee--

Finalized: December 11, 2017
Edited: December 12, 2017

