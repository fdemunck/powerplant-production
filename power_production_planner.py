def calculate_cost(plant, fuels):
    if plant['type'] == 'windturbine':
        return 0  # Wind turbines have zero cost
    elif plant['type'] == 'gasfired':
        # Calculate cost using fuel, efficiency, and CO2
        gas_cost = fuels['gas'] * (1 / plant['efficiency'])
        co2_cost = fuels['co2'] * 0.3  # Assuming 0.3 tons of CO2 per MWh
        return gas_cost + co2_cost
    elif plant['type'] == 'turbojet':
        # Calculate cost using kerosine
        kerosine_cost = fuels['kerosine'] * (1 / plant['efficiency'])
        return kerosine_cost

def calculate_production_plan(load, fuels, powerplants):
    # Sort powerplants by cost (merit order)
    sorted_plants = sorted(powerplants, key=lambda x: calculate_cost(x, fuels))

    production_plan = {}
    total_power_needed = load

    for plant in sorted_plants:
        if total_power_needed <= 0:
            break
        # Allocate power within the range of Pmin and Pmax
        power_to_generate = min(total_power_needed, plant['pmax'])
        power_to_generate = max(power_to_generate, plant['pmin'])

        production_plan[plant['name']] = power_to_generate
        total_power_needed -= power_to_generate

    # Ensure total power matches the load
    if total_power_needed > 0:
        # Allocate remaining power to the most flexible plants (like wind)
        for plant in sorted_plants:
            if plant['type'] == 'windturbine' and total_power_needed > 0:
                power_to_generate = min(plant['pmax'], total_power_needed)
                production_plan[plant['name']] = power_to_generate
                total_power_needed -= power_to_generate

    # Return the final production plan
    return production_plan