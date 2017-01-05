-- Create players table 
-- Table to store all player information for players enrolled 
-- in the current tournament. Table consists out of two columns:
-- 1: playerId data type serial and the tables primary keyt
-- 2: name     data type text

CREATE TABLE players (
	playerId serial primary key,
	name text
);

-- Create matches table
-- Table to store the results of all matches played during the tournament.
-- The table consists of three columns:
-- 1: matchId data type serial and the primary key
-- 2: winnerId data type int (refering to playerId in players table)
-- 2: loserId data type int (refering to playerId in players table)

CREATE TABLE matches (
	matchID serial primary key,
	winnerId int references players (playerId),
	loserId int references players (playerId)
);


