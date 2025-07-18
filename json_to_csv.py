import json
import csv

# Input and output filenames
input_file = "user-wallet-transactions.json"
output_file = "output.csv"

# Read JSON data from file
with open(input_file, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Flatten the data
flattened_data = []
for entry in json_data:
    flat = {
        "_id": entry["_id"]["$oid"],
        "userWallet": entry["userWallet"],
        "network": entry["network"],
        "protocol": entry["protocol"],
        "txHash": entry["txHash"],
        "logId": entry["logId"],
        "timestamp": entry["timestamp"],
        "blockNumber": entry["blockNumber"],
        "action": entry["action"],
        "actionData.type": entry["actionData"].get("type"),
        "actionData.amount": entry["actionData"].get("amount"),
        "actionData.assetSymbol": entry["actionData"].get("assetSymbol"),
        "actionData.assetPriceUSD": entry["actionData"].get("assetPriceUSD"),
        "actionData.poolId": entry["actionData"].get("poolId"),
        "actionData.userId": entry["actionData"].get("userId"),
        "__v": entry.get("__v"),
        "createdAt": entry["createdAt"]["$date"],
        "updatedAt": entry["updatedAt"]["$date"]
    }
    flattened_data.append(flat)

# Write to CSV
with open(output_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=flattened_data[0].keys())
    writer.writeheader()
    writer.writerows(flattened_data)

print(f"CSV file '{output_file}' has been created.")
