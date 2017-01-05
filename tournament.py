#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM matches;")
    conn.commit()
    cursor.close()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM players;")
    conn.commit()
    cursor.close()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT count(playerId) FROM players;")
    result = cursor.fetchall()[0][0]
    cursor.close()
    conn.close()

    return result

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO players (name) VALUES (%s);", (name,))
    conn.commit()
    cursor.close()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT wins.playerId, name, count(wins.winnerId) as wins, 
        (count(loserId) + count(wins.winnerId)) as matches 
        FROM (SELECT playerId, name, winnerId from players LEFT JOIN matches on playerId = winnerId) 
        AS wins LEFT JOIN matches on wins.playerId = loserId GROUP BY wins.playerId, name
        ORDER BY wins DESC;""")
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO matches (winnerId, loserId) VALUES (%s, %s);", (winner,loser,))
    conn.commit()
    cursor.close()
    conn.close()


 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    
    standings = playerStandings()
    pairings = []

    # Loop to go through the full list of player standings, and create output 
    # pairs from the players closest to each other in the ranking. 
    i = 0 
    for i in range(0,len(standings) - 1, 2):
        pairings.append((standings[i][0],standings[i][1],standings[i+1][0],standings[i+1][1]))
        i = i + 3
    return pairings


