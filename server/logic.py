def logic(data, user):
    scores = [0 * len(data)]
    score_category_name = ['age', 'smoking', 'favoriteMusicGenre', 'favoriteAnimal', 'highestEducationLevel', 'profession','astrologicalSign']
    score_category_pnts = [10, 9, 8, 7, 6, 5, 4]
    matching_points = [10, 8, 6, 4, 2]

    for i in len(data):
        for j in len(score_category_name):
            scores[i] += age_score([3, 7, 10, 18], score_category_pnts[0], matching_points, user, data[i])
            scores[i] += smoking_score(score_category_pnts[0], matching_points, user, data[i])
            

            
            # else, the age is unrelaistic to match by
    return scores

def age_score(diff_arr, category_points, matching_points, user, other_user):
    age_cat_name = 'age'

    for i in len(diff_arr):
        if(abs(other_user[age_cat_name] - user[age_cat_name]) <= diff_arr[i]):
            return category_points * matching_points[i]

    return 0

def smoking_score(category_points, matching_points, user, other_user):
    smoking_cat_name = 'smoking'

    if(user[smoking_cat_name] == other_user[smoking_cat_name]):
        return category_points * matching_points[0] # max
    elif((user[smoking_cat_name] == 'none' and other_user[smoking_cat_name] != 'none') or 
        (user[smoking_cat_name] != 'none' and other_user[smoking_cat_name] == 'none')):
        return 0 # smoker and non-smoker don't really match
    elif((user[smoking_cat_name] == 'tobacco' or user[smoking_cat_name] == 'vape') and 
        (other_user[smoking_cat_name] == 'tobacco' or other_user[smoking_cat_name] == 'vape')):
        return matching_points[1] * category_points
    elif(((user[smoking_cat_name] == 'tobacco' or user[smoking_cat_name] == 'vape') and other_user[smoking_cat_name] == 'cannabis') or
        ((other_user[smoking_cat_name] == 'tobacco' or other_user[smoking_cat_name] == 'vape') and user[smoking_cat_name] == 'cannabis')):
        return matching_points[3] * category_points

def music_score(category_points, matching_points, user, other_user):
    music_cat_name = 'smoking'

    if(user[music_cat_name] == other_user[music_cat_name]):
        return category_points * matching_points[0]

    if(user[music_cat_name] == 'R&B'):
        if(other_user[music_cat_name] == 'Jazz'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'Classical'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'World'):
            return category_points * matching_points[3]

    if(user[music_cat_name] == 'World'):
        if(other_user[music_cat_name] == 'New Age'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'Classical'):
            return category_points * matching_points[3]
        elif(other_user[music_cat_name] == 'Religious'):
            return category_points * matching_points[3]
    
    if(user[music_cat_name] == 'Jazz'):
        if(other_user[music_cat_name] == 'R&B'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'Classical'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'Country'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'World'):
            return category_points * matching_points[3]
        elif(other_user[music_cat_name] == 'Reggae'):
            return category_points * matching_points[4]
    
    if(user[music_cat_name] == 'Latin'):
        if(other_user[music_cat_name] == 'Reggae'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'EDM'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'Pop'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'Hip-Hop/Rap'):
            return category_points * matching_points[3]
                
    if(user[music_cat_name] == 'Reggae'):
        if(other_user[music_cat_name] == 'Latin'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'Pop'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'EDM'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'World'):
            return category_points * matching_points[3]
        elif(other_user[music_cat_name] == 'New Age'):
            return category_points * matching_points[3]
    
    if(user[music_cat_name] == 'EDM'):
        if(other_user[music_cat_name] == 'Pop'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'Latin'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'Hip-Hop/Rap'):
            return category_points * matching_points[2]
    
    
