# Udacity-Project-Tournament-Results
Code project as part of the Udacity Nanodegree introduction to programming. Consists of a database schema to store the game matches between players. And code to query this data and determine the winners of various games.

## Files
* tournament.py > implementation of a Swiss-system tournament
* tournament.sql > table definitions for the tournament project
* tournament_test.py > Test cases for tournament.py

## Running the program
\* Prerequisite(s) have vagrant and virtualbox installed on your machine.

1. Connect to your VM by running the 'vagrant up' and 'vagrant ssh' commands in your terminal (in the vagrant folder)
2. Connect to PostgreSQL by running the 'psql' command
3. Create a database called 'tournament' by running the following psql query: 'CREATE DATABASE tournament;'
4. Connect to the newly created database by running '\c tournament'
5. Run the script in tournament.sql to create the database tables by running '\i tournament.sql'
6. Leave the psql environment and come back to the vagrant VM to run the tournament_test.py by running the following command 'python tournament_test.py'
7. The results of the test will be printed to your terminal window.
