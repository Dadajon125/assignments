def  parse_tag(tag_string, required_labels):
    if tag_string[-1] != '*':
        return "Error: Read error"
    else:
        n_s = tag_string.strip('*')
        lst = n_s.split('/')
        label_list = []
        value_list = []
        for i in lst:
            parts = i.split('#')
            label = parts[0]
            value = parts[1]

            if label in required_labels:
                label_list.append(label)
                value_list.append(value)
        missing_ls = []
        for i in required_labels:
            if not i in label_list:
                missing_ls.append(i) 
        if missing_ls: 
            return f"Error: Missing labels: {missing_ls}"
    ordered = []
    for i in required_labels:
        ordered.append(value_list[label_list.index(i)])
    return ordered

# Test Case 1: Valid scan
scan1 = "SKU#TX-99/LOC#Row3/BATCH#B7*"
req1 = ["SKU", "LOC", "BATCH"]
print(parse_tag(scan1, req1))

# Test Case 2: Valid scan but missing batch info
scan2 = "SKU#RX-11/LOC#Row1*"
req2 = ["SKU", "LOC", "BATCH"]
print(parse_tag(scan2, req2))

# Test Case 3: Invalid format (missing asterisk)
scan3 = "SKU#ZZ-00/LOC#Dock"
req3 = ["SKU"]
print(parse_tag(scan3, req3))

# Test Case 4: Different order
scan4 = "EXP#2024/SKU#MILK/LOC#Fridge*"
req4 = ["SKU", "LOC", "EXP"]
print(parse_tag(scan4, req4))
