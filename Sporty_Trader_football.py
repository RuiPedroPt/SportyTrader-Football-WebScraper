# ---------------------------------- IMPORTANT ----------------------------------
# ---------------------------------- IMPORTANT ----------------------------------
# ---------------------------------- IMPORTANT ----------------------------------
# This was made By: Rui Pedro O. Paiva

# ---------------------------------- LICENSE ----------------------------------
# Because There is NO LICENSE this code is NOT ALLOWED FOR COMMERCIAL USE.
# This is ONLY FOR EDUCATIONAL PURPOSES for the Community, if you want to improve/optimize the code and update it you can, just ask for a repo update.

# ---------------------------------- NOTES ----------------------------------
# The file is a csv(comma separated values), although, i use ";" to separate values simply because I'm European our numbers use "," for decimals.
# This is pretty simple to solve if you dont want to, you can either specify on your sheets software that when you're importing you wanna use ";" as the separator, or you can change in the code(replace function I used)

# ----------------- Import Libraries -----------------
import requests
from bs4 import BeautifulSoup

# ----------------- Clear the txt file from previous run -----------------
filename = 'BETS.csv'
with open(filename, 'w') as wf:
    wf.write("Date;Teams;Odd 1;Odd X;Odd 2;Arbitrage_Calc" + '\n')

print("\nProgram Started...")   # Pretty self-explanatory
# ----------------- Basic Get request -----------------
url = "https://www.sportytrader.pt/quotas/futebol/"
response = requests.get(url).text
soup = BeautifulSoup(response, "lxml")

# ----------------- Scrape how many Games are in the page -----------------
How_many_games = 0  # Set var as 0 for the "for loop"
for games in soup.find_all("span", class_="font-medium w-full lg:w-1/2 text-center dark:text-white"):   # For Every game in the main div (stores every game data), increment "1" in order to know how many games are in the page
    How_many_games +=1

# ----------------- Variables for the while Loop -----------------
num= 0
x =0

# While Loop that gets all the information from each game
print("Scraping has started now!")
while num != How_many_games:
    x = soup.find_all('div', class_="cursor-pointer border rounded-md mb-4 px-1 py-2 flex flex-col lg:flex-row relative")   # Get All the info, from time to odds
    desired_result = x[num]   # The index Of the Game / Line it is chosen
    date = desired_result.find("span", class_ = "text-sm text-gray-600 w-full lg:w-1/2 text-center dark:text-white").text   # Get the Date of the Game
    teams = desired_result.find("span", class_ = "font-medium w-full lg:w-1/2 text-center dark:text-white").text.strip()    # Get the Teams
    # ----------------- Get the odds -----------------
    odds = desired_result.find_all("span", class_ = "px-1 h-booklogosm font-bold bg-primary-yellow text-white leading-8 rounded-r-md w-14 md:w-18 flex justify-center items-center text-base")
    desired_odd0= odds[0]
    desired_odd1= odds[1]
    desired_odd2= odds[2]
    # ----------------- Arbitrage Calculating Formula -----------------
    perc0 = 1/float(desired_odd0.text)  # Basic formula needed for Arbitrage Betting
    perc1 = 1/float(desired_odd1.text)  # Basic formula needed for Arbitrage Betting
    perc2 = 1/float(desired_odd2.text)  # Basic formula needed for Arbitrage Betting
    total_perc = perc0 + perc1 + perc2  # Add all three odds and if it is under "1" there's an Arbitrage Opportunity
    # ----------------- Store Data as "data" -----------------
    data = (str(date) + ";" + str(teams) + ";" + str(desired_odd0.text.replace(".", ",")) + ";" + str(desired_odd1.text.replace(".", ",")) + ";" + str(desired_odd2.text.replace(".", ",")) + ";" + str(total_perc).replace(".", ","))
    # ----------------- Append data to File -----------------
    with open(filename, 'a') as af:
        af.write(data + '\n')
    num +=1 # For the end of the loop increment one to go for the next game (increments one for the index)

print("\nDone!\n" + str(num) +" games were scraped!")   # When the While Loop ends print that it's done and how many games were scraped
