def analyze_transactions(transactions):
    categorized = {
        "normal": [],
        "large": [],
        "high_risk": [],
        "invalid": []
    }

    # Step 1: Classification
    for amount in transactions:
        if amount <= 0:
            categorized["invalid"].append(amount)
        elif amount <= 500:
            categorized["normal"].append(amount)
        elif amount <= 2000:
            categorized["large"].append(amount)
        else:
            categorized["high_risk"].append(amount)

    # Step 2: Clean valid data using list comprehension
    valid_data = [x for x in transactions if x > 0]

    total = sum(valid_data)
    count = len(transactions)

    # Tuple summary
    summary = (total, count)

    # Step 3: Pattern checks
    is_frequent = count > 5
    is_heavy_spend = total > 5000
    is_suspicious = len(categorized["high_risk"]) >= 3

    # Step 4: Risk evaluation (priority logic)
    if is_suspicious:
        risk_level = "High Risk"
    elif is_heavy_spend and is_frequent:
        risk_level = "Moderate Risk"
    elif is_heavy_spend or is_frequent:
        risk_level = "Moderate Risk"
    else:
        risk_level = "Low Risk"

    # Step 5: Additional Insight (UNIQUE TOUCH)
    high_risk_ratio = (
        len(categorized["high_risk"]) / count * 100
        if count > 0 else 0
    )

    # Output
    print("\n--- Transaction Report ---")
    print("Categories:", categorized)
    print("Total Value:", summary[0])
    print("Transaction Count:", summary[1])
    print("High-Risk Percentage:", round(high_risk_ratio, 2), "%")
    print("Final Risk Level:", risk_level)

    return categorized, summary, risk_level


# Sample Run
transactions = [120, 700, 2500, 50, 3000, 1200, -10]
analyze_transactions(transactions)