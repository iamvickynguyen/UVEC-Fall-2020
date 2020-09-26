def logic(data, user):
    scores = [0] * len(data)
    score_category_name = ['age', 'smoking', 'favoriteMusicGenre', 'highestEducationLevel', 'profession','astrologicalSign']
    score_category_pnts = [10, 9, 8, 7, 6]
    matching_points = [10, 8, 6, 4, 2]
    max_score = 0

    for i in range(len(score_category_pnts)):
        max_score += matching_points[0] * score_category_pnts[i]

    for i in range(len(data)):
        scores[i] += age_score([3, 7, 10, 18], score_category_pnts[0], matching_points, user, data[i])
        scores[i] += smoking_score(score_category_pnts[1], matching_points, user, data[i])
        scores[i] += music_score(score_category_pnts[2], matching_points, user, data[i])
        scores[i] += education_score(score_category_pnts[3], matching_points, user, data[i])
        scores[i] += sign_score(score_category_pnts[4], matching_points, user, data[i])
        
        scores[i] = (scores[i] / max_score) * 100
        data[i]['score'] = round(scores[i], 2)

    return data

def age_score(diff_arr, category_points, matching_points, user, other_user):
    age_cat_name = 'age'

    for i in range(len(diff_arr)):
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
    music_cat_name = 'favoriteMusicGenre'

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
    
    if(user[music_cat_name] == 'Classical'):
        if(other_user[music_cat_name] == 'Jazz'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'R&B'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'Stage & Screen'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'Religious'):
            return category_points * matching_points[3]

    if(user[music_cat_name] == 'Country'):
        if(other_user[music_cat_name] == 'Jazz'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'Religious'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'Rock'):
            return category_points * matching_points[4]
        elif(other_user[music_cat_name] == 'Alternative'):
            return category_points * matching_points[4]

    if(user[music_cat_name] == 'Pop'):
        if(other_user[music_cat_name] == 'Hip-Hip/Rap'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'EDM'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'Latin'):
            return category_points * matching_points[2]

    if(user[music_cat_name] == 'Hip-Hip/Rap'):
        if(other_user[music_cat_name] == 'Pop'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'EDM'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'Latin'):
            return category_points * matching_points[3]

    if(user[music_cat_name] == 'Religious'):
        if(other_user[music_cat_name] == 'Country'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'Classical'):
            return category_points * matching_points[3]
        elif(other_user[music_cat_name] == 'World'):
            return category_points * matching_points[4]
        elif(other_user[music_cat_name] == 'Raggae'):
            return category_points * matching_points[4]
        elif(other_user[music_cat_name] == 'Alternative'):
            return category_points * matching_points[5]

    if(user[music_cat_name] == 'Alternative'):
        if(other_user[music_cat_name] == 'Rock'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'Jazz'):
            return category_points * matching_points[3]
        elif(other_user[music_cat_name] == 'Hip-Hip/Rap'):
            return category_points * matching_points[4]
        elif(other_user[music_cat_name] == 'Religious'):
            return category_points * matching_points[5]

    if(user[music_cat_name] == 'Rock'):
        if(other_user[music_cat_name] == 'Alternative'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'Jazz'):
            return category_points * matching_points[4]
        elif(other_user[music_cat_name] == 'Hip-Hip/Rap'):
            return category_points * matching_points[4]
        elif(other_user[music_cat_name] == 'Classical'):
            return category_points * matching_points[5]
    
    if(user[music_cat_name] == 'Stage & Screen'):
        if(other_user[music_cat_name] == 'Jazz'):
            return category_points * matching_points[2]
        elif(other_user[music_cat_name] == 'R&B'):
            return category_points * matching_points[3]
        elif(other_user[music_cat_name] == 'Classical'):
            return category_points * matching_points[4]

    if(user[music_cat_name] == 'New Age'):
        if(other_user[music_cat_name] == 'World'):
            return category_points * matching_points[1]
        elif(other_user[music_cat_name] == 'Classical'):
            return category_points * matching_points[4]
        elif(other_user[music_cat_name] == 'Raggae'):
            return category_points * matching_points[4]
    return 0

def education_score(category_points, matching_points, user, other_user):
    education_cat_name = 'highestEducationLevel'

    if(user[education_cat_name] == other_user[education_cat_name]):
        return category_points * matching_points[0]

    if(user[education_cat_name] == 'PhD'):
        if(other_user[education_cat_name] == 'none'):
            return category_points * matching_points[5]
        elif(other_user[education_cat_name] == 'high school'):
            return category_points * matching_points[4]
        else:
            return category_points * matching_points[1]
    elif(user[education_cat_name] == 'master\'s degree'):
        if(other_user[education_cat_name] == 'none'):
            return category_points * matching_points[5]
        elif(other_user[education_cat_name] == 'high school'):
            return category_points * matching_points[4]
        else:
            return category_points * matching_points[1]
    elif(user[education_cat_name] == 'undergraduate degree'):
        if(other_user[education_cat_name] == 'none'):
            return category_points * matching_points[4]
        elif(other_user[education_cat_name] == 'high school'):
            return category_points * matching_points[3]
        else:
            return category_points * matching_points[2]
    elif(user[education_cat_name] == 'high school'):
        if(other_user[education_cat_name] == 'none'):
            return category_points * matching_points[2]
        else:
            return category_points * matching_points[3]
    else:
        if(other_user[education_cat_name] == 'high school'):
            return category_points * matching_points[2]
        else:
            return category_points * matching_points[3]

def sign_score(category_points, matching_points, user, other_user):
    sign_cat_name = 'astrologicalSign'

    if(user[sign_cat_name] == 'Aries' or user[sign_cat_name] == 'Leo' or user[sign_cat_name] == 'Sagittarius'): # Fire
        if(other_user[sign_cat_name] == 'Aries' or other_user[sign_cat_name] == 'Leo' or other_user[sign_cat_name] == 'Sagittarius'): #Fire
            return category_points * matching_points[0]
        elif(other_user[sign_cat_name] == 'Aquarius' or other_user[sign_cat_name] == 'Gemini' or other_user[sign_cat_name] == 'Libra'): #Air
            return category_points * matching_points[1]
        else:
            return 0
    elif(user[sign_cat_name] == 'Aquarius' or user[sign_cat_name] == 'Gemini' or user[sign_cat_name] == 'Libra'): # Air
        if(other_user[sign_cat_name] == 'Aquarius' or other_user[sign_cat_name] == 'Gemini' or other_user[sign_cat_name] == 'Libra'): #Air
            return category_points * matching_points[0]
        elif(other_user[sign_cat_name] == 'Aries' or other_user[sign_cat_name] == 'Leo' or other_user[sign_cat_name] == 'Sagittarius'): #Fire
            return category_points * matching_points[1]
        else:
            return 0
    elif(user[sign_cat_name] == 'Scorpio' or user[sign_cat_name] == 'Cancer' or user[sign_cat_name] == 'Pisces'): # Water
        if(other_user[sign_cat_name] == 'Scorpio' or other_user[sign_cat_name] == 'Cancer' or other_user[sign_cat_name] == 'Pisces'): #Water
            return category_points * matching_points[0]
        elif(other_user[sign_cat_name] == 'Taurus' or other_user[sign_cat_name] == 'Virgo' or other_user[sign_cat_name] == 'Capricorn'): #Earth
            return category_points * matching_points[1]
        else:
            return 0
    elif(user[sign_cat_name] == 'Taurus' or user[sign_cat_name] == 'Virgo' or user[sign_cat_name] == 'Capricorn'): #Earth
        if(other_user[sign_cat_name] == 'Taurus' or other_user[sign_cat_name] == 'Virgo' or other_user[sign_cat_name] == 'Capricorn'): #Earth
            return category_points * matching_points[0]
        elif(other_user[sign_cat_name] == 'Scorpio' or other_user[sign_cat_name] == 'Cancer' or other_user[sign_cat_name] == 'Pisces'): #Water
            return category_points * matching_points[1]
        else:
            return 0