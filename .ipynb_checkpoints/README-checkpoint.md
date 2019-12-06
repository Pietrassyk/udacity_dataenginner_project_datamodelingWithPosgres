# Project relational song Daatabase

In this Database Modeling Project a relational Database is is used to store songs and event logs.

Consult subsection *#CREATE Tables* in *sql_queries.py* for an overview of the Entity and Attribute Definitions.

How To Use:

1. Run *create_tables.py* to reset the DataBase and Create empty Tables as specified in *sql_queries.py* section *#CREATE Tables*
2. Run *etl.py* to recursively iterate through the song data and log data in the *data* folder extract relevant information, transform it into the specified formats and load it to the database.
3. Run Queries in *test.ipynb* to see the results.