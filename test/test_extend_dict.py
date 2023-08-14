towns1 = {
    "New York": (40.7128, -74.0060),
    "San Francisco": (37.7749, -122.4194),
    "Los Angeles": (34.0522, -118.2437),
}
towns2 = {
    "Los Angeles": (34.0522, -118.2437),
    "London": (51.5074, -0.1278),
    "Paris": (48.8566, 2.3522),
    "Tokyo": (35.6895, 139.6917),
    "Ontario": (34.0522, -118.2437),
}
# towns1.update(towns2)
# towns2.update(towns1)

inv_towns = {v: [k] for k, v in towns2.items()}

print(towns2)
matching_values = {}
keys_inv = list(inv_towns.keys())
matches = []

for k1, v1 in towns2.items():
    if v1 not in matching_values:
        matching_values[v1] = [k1]
    else:
        matching_values[v1].append(k1)
    # matches.append(k2)
    # print(matches)

print(matching_values)
