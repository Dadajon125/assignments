data = """MainSt,Downtown,450,100
Broadway,Downtown,300,50
OakAve,Suburbs,100,20
PineRd,Suburbs,50,10
Hwy101,Highway,800,400
Error,Line,Missing,Data
MarketSt,Downtown,500,200"""
with open("traffic_survey.txt", "w") as f:
    f.write(data)
def analyze_traffic_flow(filename):
    district_totals = {}
    congested_streets = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            street, district, car_count, truck_count = parts
            try:
                cars = int(car_count)
                trucks = int(truck_count)
            except ValueError:
                continue
            total = cars + trucks
            district_totals[district] = district_totals.get(district, 0) + total
            if total > 500:
                congested_streets.append((street, total))
    return district_totals, congested_streets
def write_traffic_report(district_totals, congested_streets):
    with open("traffic_report.txt", "w") as f:
        f.write("DISTRICT TRAFFIC VOLUME\n")
        f.write("-----------------------\n")
        for district, total in district_totals.items():
            f.write(f"{district}: {total}\n")
        f.write("\nCONGESTED STREETS (> 500 vehicles)\n")
        f.write("----------------------------------\n")
        for street, total in congested_streets:
            f.write(f"{street} ({total} vehicles)\n")
districts, congested = analyze_traffic_flow("traffic_survey.txt")
write_traffic_report(districts, congested)

with open("traffic_report.txt", "r") as f:
    print(f.read())