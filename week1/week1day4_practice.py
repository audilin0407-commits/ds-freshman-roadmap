def clean_and_analyze():
    raw_scores = [78, 90, None, 55, -10, 102, 88, None]
    clean_scores = [
        cs 
        for cs in raw_scores 
        if cs is not None 
        if 0 <= cs <= 100  
    ]

    print(clean_scores)



    normalized = [
        n / 100 
        for n in clean_scores
    ]

    print(normalized)
    if len(clean_scores) > 0:
        Average = [sum(clean_scores) / len(clean_scores)]
    else:
        print("No valid data")
    Max = max(clean_scores)
    Min = min(clean_scores)
    print("Average : ",Average)
    print("Max : ",Max)
    print("Min : ",Min)
