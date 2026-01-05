cargos = {
    "C1": 1234,
    "C2": 4352,
    "C3": 3321,
    "C4": 2456,
    "C5": 5123,
    "C6": 1879,
    "C7": 4987,
    "C8": 2050,
    "C9": 3678,
    "C10": 5432,
}

tanks = {
    "T1": 3034,
    "T2": 2952,
    "T3": 3010,
    "T4": 4532,
    "T5": 3876,
    "T6": 6050,
    "T7": 2500,
    "T8": 4000,
    "T9": 2010,
}

# Sort cargos and tanks by size (descending)
sorted_cargos = sorted(cargos.items(), key=lambda x: x[1], reverse=True)
sorted_tanks = sorted(tanks.items(), key=lambda x: x[1], reverse=True)

allocation = []
total_loaded = 0
tank_index = 0

# Assign cargos to tanks
for cargo_id, cargo_volume in sorted_cargos:
    remaining_volume = cargo_volume

    while remaining_volume > 0 and tank_index < len(sorted_tanks):
        tank_id, tank_capacity = sorted_tanks[tank_index]

        load = min(remaining_volume, tank_capacity)

        allocation.append({
            "tank": tank_id,
            "cargo": cargo_id,
            "loaded_volume": load
        })

        total_loaded += load
        remaining_volume -= load
        tank_index += 1

    if tank_index >= len(sorted_tanks):
        break

# -----------------------------
# Output
# -----------------------------
print("Final Cargo-to-Tank Allocation:\n")
for a in allocation:
    print(f"{a['tank']} -> {a['cargo']} : {a['loaded_volume']}")

print("\nTotal Loaded Volume:", total_loaded)
