data_log = [
    "Sales;Alice;500",
    "Engineering;Bob;1200",
    "Sales;Charlie;300",
    "HR;David;150",
    "Engineering;Eve;800",
    "HR;Frank;100"
]
def track_usage(data_log):
    result = {}
    for item in data_log:
        item = item.split(';')
        department = item[0]
        user = item[1]
        megabytes = item[2]
        megabytes = int(megabytes)
        if department not in result:
            result[department] = []
        result[department].append((user, megabytes))
    return result

network_result = track_usage(data_log)
def audit_departments(network_dict):

    for i , j in network_dict.items():
        count = 0
        for user in j:
            count += user[1]
        print(f"{i}: {count} MB total")
    
audit_departments(network_result)