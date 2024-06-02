def human_years_cat_years_dog_years(human_years):
    cat = 0
    dog = 0
    
    if human_years < 2:
        cat = human_years *15
        dog = cat
    elif human_years < 3:
        cat = 15 + 9
        dog = cat
    else:
        cat = ((human_years -2) *4) +24
        dog = ((human_years -2) *5) +24
        
    return [human_years, cat, dog]