# Python SQL API

### The following code is used to connect to online postgresql called elephantSQL 

## Pre-requisites
python >= 3.0

pip

## Dependencies used
psycopg2 (for database connection)


## Steps to use
Clone the project into your folder.

Create a new account in elephant sql site the link is https://customer.elephantsql.com/login

Create free account and you will the the url of the database account. Use this credential to create your own free database that is hosted online

Create a table in the online database named "utstudents" the sql command is as follows

`CREATE TABLE utstudents (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    address VARCHAR(100),
    city VARCHAR(50),
    course_enrolled VARCHAR(50)
);`

After the database is successfully created you can call the API endpoints to perform CRUD operattions the API endpoints are as follows

`http://127.0.0.1:8000/students` GET method to read all the records

`http://127.0.0.1:8000/students/:id` GET method to read a single record

`http://127.0.0.1:8000/students/:id` GET method to read a single record

`http://127.0.0.1:8000/students/:id` PUT method to edit a single data into the table

`http://127.0.0.1:8000/students/:id` DELETE method to remove a single data into the table


## POSTMAN file
Download the postman collection file to import and use the postman 

The collection contains all the environments already set up to test the API endpoints