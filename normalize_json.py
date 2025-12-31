import json
import pandas as pd

# Load the original JSON file
with open("sample.json", "r") as file:
    data = json.load(file)

rows = []

# Normalize the JSON data
for customer in data:
    for order in customer["orders"]:
        for item in order["items"]:
            rows.append([
                customer["customer_id"],
                order["order_id"],
                item["product"],
                item["quantity"],
                order["total"]
            ])

# Create DataFrame
df = pd.DataFrame(
    rows,
    columns=["customer_id", "order_id", "product", "quantity", "total"]
)

# Save the normalized DataFrame to a new JSON file
df.to_json("normalized_orders.json", orient="records", indent=2)

print("normalized_orders.json has been created successfully.")
