def create_permit_index(authorized_list):
    return {item['plate_num']: item['owner_name'] for item in authorized_list}

def scan_lot(permit_index, current_plates):
    permit_plates = set(permit_index.keys())
    current_set = set(current_plates)
    un_permits = permit_plates - current_set
    vio_cars = current_set - permit_plates
    return un_permits, vio_cars

def report_empty_spots(permit_index, unused_set):
    sorted_plates = sorted(unused_set, key=lambda plate: permit_index[plate])
    report = [
        f"EMPTY SPOT: Reserved for {permit_index[plate]} ({plate})"
        for plate in sorted_plates
    ]
    return report
permits = [
    {'plate_num': "ABC-123", 'owner_name': "Dr. House"},
    {'plate_num': "XYZ-789", 'owner_name': "Prof. X"},
    {'plate_num': "LMN-456", 'owner_name': "Sherlock"}
]
in_lot = ["ABC-123", "LMN-456", "BAD-CAR"]
permit_index = create_permit_index(permits)
unused, violators = scan_lot(permit_index, in_lot)
report = report_empty_spots(permit_index, unused)

print(f"Unused Permits: {unused}")
print(f"Violators: {violators}")
print("Report:", report)
