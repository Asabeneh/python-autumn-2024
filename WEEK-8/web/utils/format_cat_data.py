def format_cat_data():
    lst = []
    for cat in data:
        mn, mx = cat['life_span'].split(' - ')
        average_life_span = (int(mn) + int(mx)) / 2
        min_weight, max_weight = cat['weight']['metric'].split(' - ')
        average_weight = (int(min_weight) + int(max_weight)) / 2
        
        dct = {
            'name':cat['name'],
            'country':cat['origin'],
            'description':cat['description'],
            'life_span':average_life_span,
            'weight':average_weight
        }
    