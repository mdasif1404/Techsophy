def determine_life_stage(age, marital_status, dependents):
    if age < 30 and marital_status == 'Single':
        return 'Young Single'
    elif marital_status == 'Married' and dependents > 0:
        return 'Family'
    elif age > 55:
        return 'Pre-Retirement'
    else:
        return 'Mid-Life'


def profile_customer(row):
    return {
        'id': row['id'],
        'life_stage': determine_life_stage(row['age'], row['marital_status'], row['dependents']),
        'income': row['income'],
        'risk_score': 0.5  # placeholder for ML-based score
    }
