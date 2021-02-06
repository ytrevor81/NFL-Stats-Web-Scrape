# NFL-Stats-Web-Scrape
This web scraper gathers basic statistics and career statistics provided by the NFL on their official website for active players and all 40,000+ retired players.

## How to run the code
After installing the requirements from requirements.txt, open your preferred terminal, navigate into the Scraper directory and type the command "python Activate.py"

## Summary
There are three parts to this code:

1. Gathering individual player links, in order to access their profile page
2. Gathering basic stats for each player (ex. name, college, height, weight, etc)
3. Gathering career stats for each player

## Files and Explanation
- Activate.py
- Players.py
- Urls.py
- Scraper_Functions
  1. Basic_Stats_Functions
  2. Career_Stats_Functions.py
  3. CSV_Handler.py
  4. Gather_Player_Urls.py

### <i>Activate.py</i>
This is where the core functions of the code are executed, gathering and processing query urls, player urls, and creating the appropriate CSV files to store data.

### <i>Classes: Players.py and Urls.py</i>
In Players.py, three classes are used to store player data: <i>ActivePlayer</i>, <i>RetiredPlayer</i>, and <i>Player_CareerStats</i>. <i>ActivePlayer</i> and <i>RetiredPlayer</i> are initialized once, so that only one instance is used in the data scraping process, and are used to store and process basic stats of individual players. <i>Player_CareerStats</i> is initialized everytime a new player's career stats are processed, both active and retired. If any player does not have any stats tables present in their webpage, then they will be skipped and thus not recorded in any career stats CSV file.

The <i>Urls</i> class holds all player query links for active players and retired players, and aids in processing those links and other links.

### <i>Gather_Player_Urls.py</i>
Only two functions are in this file, one of which is essential for all other functions in the code. The <i>Extract_Individual_Player_Links</i> function gathers all individual player links from each player query page. The links for each query page are located in the <i>Urls</i> class. Each query page holds 100 individual player links.

The <i>Get_HTML_Document</i> function gathers the "soup" of all links pasted through this function. This function is used often throughout the code.

### <i>CSV_Handler.py</i>
All functions creating, appending, and writing CSV files are held in this file.

### <i>Basic_Stats_Functions.py</i>
This file handles extracting basic profile stats for all players, but active players and retired players are processed in separate functions. A lot of information available for active players are not available for retired players, due to the massive amount of retired players as compared to active players. Also, the code records whether or not a retired player is in the Hall Of Fame. 

### <i>Career_Stats_Functions.py</i>
These functions handle both active and retired players. Most likely the sloppiest code in this web scraper is in the function <i>Player_Stats</i>, even though it works as expected. Each player's stats table has no particular class or identifier separating, for example, a "Passing" table from a "Punting" table from player to player (it makes more sense when you compare the HTML source code of two or more players with each other). So this was the best way I found at the time to get around that obstacle.

If a player does not have any stats tables in their webpage, then the player is not recorded in the career stats CSV files.
