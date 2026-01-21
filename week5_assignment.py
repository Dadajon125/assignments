def find_account_index(account_ids, account_id):
    for i in range(len(account_ids)):
        if account_ids[i] == account_id:
            return i 
    return -1    



def process_ledger(initial_accounts, initial_balances, transactions):
    c_accounts = [initial_accounts[:]]
    c_balance = [initial_balances[:]]
    c_t = transactions
    for sublist in c_t:
        if sublist[0] == 'OPEN':
            ind = find_account_index(c_accounts, sublist[1])
            if ind == -1: 
                c_accounts.append(sublist[1])
                c_balance.append(sublist[1])
        elif sublist[0] == 'DEPOSIT':
            ind = find_account_index(c_accounts, sublist[1])
            if ind != -1: c_balance[ind] += sublist[2]
        else:
            ind = find_account_index(c_accounts, sublist[1])

            if ind != -1 and c_balance[ind] >= sublist[2]:c_balance[ind] -= sublist[2]
    final_account_ids_list = c_accounts
    final_account_balance_list = c_balance        
    return final_account_ids_list, final_account_balance_list            


accounts = ["ACC-001", "ACC-002", "ACC-003"]
balances = [500.00, 1200.00, 250.00]
daily_transactions = [
    ["DEPOSIT", "ACC-001", 150.00],
    ["WITHDRAW", "ACC-002", 250.00],
    ["WITHDRAW", "ACC-003", 300.00], 
    ["OPEN", "ACC-004", 1000.00],
    ["DEPOSIT", "ACC-002", 50.00]
]
final_accounts, final_balances = process_ledger(accounts, balances, daily_transactions )
print(f'''Final  Accounts: {final_accounts}
Final Balances: {final_balances}''')