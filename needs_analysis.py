def assess_needs(profile):
    stage = profile['life_stage']
    if stage == 'Young Single':
        return ['Health']
    elif stage == 'Family':
        return ['Life', 'Health']
    elif stage == 'Pre-Retirement':
        return ['Retirement']
    else:
        return ['Life']
