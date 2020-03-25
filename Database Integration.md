# Database Integration  
[Static Data](#static-data)  
[Interface](#interface)  
[Tables](#tables)  
[Joins](#joins)  
[Connection string](#connection-string)  
[Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)  
[Back to README.md](/README.md)

## Static Data  
Once a clean data was obtained, parsed and sorted, it made it clear what types of tables could be useful for the project. Tables were then built in PostgreSQL to store static data. An ERD with a schema was first constructed and helped shape how and what questions we wanted the database to answer or insights to generate. Eventually, multiple tables were built to store static data.  

## Interface  
The database interfaces with our python notebook file where all the data loading and cleaning occurred. This was achieved by importing create_engine from sqlaclchemy; the information that sqlaclchemy needs to create a database engine.  

## Tables  
Multiple tables were generated to store static data as the project evolved. Tables include combined_ca_data, ca_analysis, housing_and_income, analysis_info, just to mention a few. For example, the ca_analysis table stores static data of all CA who moved to selected states between a given period, ordered by ascending order. Similarly, the analysis_info table stores median housing cost(monthly) data for all states.  

* Example - California Migration to All Other States (2010 -2018)

![](https://github.com/JVChermak/Leaving_California/blob/master/pics/allYear_table.png)


## Joins  
A left join using the database is performed on selected states from 2017 and 2018, left joining on the States which is a column found in both data sets.  

* Left Join Table (On 2017 by selected States)

![](https://github.com/JVChermak/Leaving_California/blob/master/pics/leftjoin_table.png)

## Connection string  
A connection string using SQLAlchemy connects our python to our PostgreSQL.  

## Entity Relationship Diagram (ERD)  
<img align="center" width="700" src="/pics/Migration_FlowDB(2).png"><br/>
<br/>
<br/>
<br/>
<br/>  

[Back to Top](#database-integration)  
[Back to README.md](/README.md)

## Other: Plots & Graphs

* Bar Graph: Housing by Name

![](https://github.com/JVChermak/Leaving_California/blob/master/pics/bar%20graph_by%20Name.png)


* Bar Graph: Housing by Year

![](https://github.com/JVChermak/Leaving_California/blob/master/pics/bar%20graph_by%20Year.png)

* Line Plot: Top 5 CA Migrated States

![](https://github.com/JVChermak/Leaving_California/blob/master/pics/Line%20Plot.png)
