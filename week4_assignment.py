def calculate_delivery_revenue(order_type, deliveries_completed, time_period):
    rate = 0
    if order_type == "express":
        if time_period == "morning":
            rate = 8
        elif time_period == "lunch":
            rate = 12
        elif time_period == "dinner":
            rate = 18
        else:
            print("Invalid time period.")
            return 0
    elif order_type == "regular":
        if time_period == "morning":
            rate = 5
        elif time_period == "lunch":
            rate = 8
        elif time_period == "dinner":
            rate = 12
        else:
            print("Invalid time period.")
            return 0
    elif order_type == "bulk":
        if time_period == "morning":
            rate = 15
        elif time_period == "lunch":
            rate = 22
        elif time_period == "dinner":
            rate = 30
        else:
            print("Invalid time period.")
            return 0
    else:
        print("Invalid order type.")
        return 0

    revenue = rate * deliveries_completed
    return revenue


def calculate_completion_rate(driver_months, baseline_orders, completed_orders):
    expected_orders = 1000 + (driver_months * 100)
    order_capacity = expected_orders - baseline_orders

    if order_capacity <= 0:
        return 0

    completion_percent = ((completed_orders - baseline_orders) / order_capacity) * 100
    return round(completion_percent, 2)


def determine_driver_tier(completion_percent):
    if completion_percent < 50:
        return "Starter Tier"
    elif completion_percent < 60:
        return "Bronze Tier"
    elif completion_percent < 70:
        return "Silver Tier"
    elif completion_percent < 85:
        return "Gold Tier"
    else:
        return "Elite Tier"

def calculate_total_earnings(revenue, deliveries, tier):
    base_earnings = revenue * 0.05 + deliveries * 2
    if tier == "Starter Tier":
        tier_bonus = 0.5
    elif tier == "Bronze Tier":
        tier_bonus = 1.0
    elif tier == "Silver Tier":
        tier_bonus = 1.2
    elif tier == "Gold Tier":
        tier_bonus = 1.5
    elif tier == "Elite Tier":
        tier_bonus = 1.8
    else:
        tier_bonus = 1.0
    final_earnings = base_earnings * tier_bonus
    return round(final_earnings, 1)


def needs_route_optimization(delivery_days, total_deliveries, avg_completion):
    if delivery_days >= 6 and avg_completion < 50:
        return True
    elif total_deliveries < 100 and avg_completion < 60:
        return True
    elif delivery_days >= 4 and avg_completion < 40:
        return True
    else:
        return False

def generate_delivery_summary(driver_name, order_type, deliveries, time_period, driver_months, baseline_orders, completed_orders, delivery_days):
    revenue = calculate_delivery_revenue(order_type, deliveries, time_period)
    completion_percent = calculate_completion_rate(driver_months, baseline_orders, completed_orders)
    tier = determine_driver_tier(completion_percent)
    total_earnings = calculate_total_earnings(revenue, deliveries, tier)
    optimization_needed = needs_route_optimization(delivery_days, deliveries, completion_percent)

    print(f"\n--- Delivery Summary for {driver_name} ---")
    print(f"Order Type: {order_type.capitalize()} | Time Period: {time_period.capitalize()}")
    print(f"Deliveries Completed: {deliveries}")
    print(f"Revenue: ${revenue}")
    print(f"Completion Rate: {completion_percent}%")
    print(f"Driver Tier: {tier}")
    print(f"Total Earnings: ${total_earnings}")
    print(f"Route Optimization Needed: {'Yes' if optimization_needed else 'No'}")
    print("-------------------------------------------")




generate_delivery_summary("Drew", "bulk", 45, "dinner", driver_months=3, baseline_orders=800, completed_orders=1150, delivery_days=3)
generate_delivery_summary("Ellis", "regular", 60, "lunch", driver_months=5, baseline_orders=900, completed_orders=1300, delivery_days=5)
generate_delivery_summary("Frankie", "express", 30, "morning", driver_months=8, baseline_orders=850, completed_orders=950, delivery_days=7)