import requests

API_KEY = "92ec1d691e81aeeece31c995fc15ba33"
BASE_URL = "https://v3.football.api-sports.io"

def get_data(league_id, season):
    url = BASE_URL + "/standings"
    headers = {
        "x-apisports-key": API_KEY}
    query = {
        "league": league_id,
        "season": season}
    try:
        response = requests.get(url, headers=headers, params=query)
        data = response.json()
        return data
    except:
        print("Error: Cannot connect to API.")
        return None

def process_data(data, limit):
    teams = []
    try:
        standings = data["response"][0]["league"]["standings"][0]
        for item in standings:
            rank = item["rank"]
            name = item["team"]["name"]
            points = item["points"]
            team_info = [rank, name, points]
            teams.append(team_info)
        teams.sort()
        return teams[:limit]
    except:
        print("Error: No data found.")
        return []

def display_results(teams):
    print("\nLeague Standings")
    print("----------------")
    file = open("standings.txt", "w")
    for team in teams:
        rank = team[0]
        name = team[1]
        points = team[2]
        line = str(rank) + ". " + name + " - " + str(points) + " points"
        print(line)
        file.write(line + "\n")
    print("\nResults saved to standings.txt")

print("Football League Standings Program")
print("---------------------------------")
league_id = input(
    "Enter league ID (39=Premier League, 140=LaLiga, 135=Serie A, 61=Ligue 1): "
)
season_input = input("Enter season year (example: 2023 or 2024): ")
limit_input = input("How many top teams to show? ")
print("\nChecking input...")
if season_input.isdigit() and limit_input.isdigit():
    season = int(season_input)
    limit = int(limit_input)
    print("Fetching data from API...")
    data = get_data(league_id, season)
    if data != None:
        print("Processing data...")
        teams = process_data(data, limit)
        if len(teams) > 0:
            display_results(teams)
        else:
            print("No results available for this season.")
    else:
        print("Data not received from API.")
else:
    print("Invalid input. Please enter numeric values only.")
print("\nProgram finished.")
