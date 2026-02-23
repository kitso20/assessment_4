##################
#   Question 1   #
##################

def batch_api_dispatcher(user_ids: list | tuple) -> list:
    user_ids = list(user_ids)
    li = []
    while len(user_ids) > 0:
        fist = user_ids[:5]
        li.append(fist)
        del user_ids[0:5]


    return  li


##################
#   Question 2   #
##################

def winning_streak(streak):
    joined = ''.join(streak)
    dtlpit = joined.split('L')
    return max(len(item) for item in dtlpit)

##################
#   Question 3   #
##################

def peak_finder(temperatures):
    dsds = []
    for i in range(len(temperatures) - 1):
        dd = temperatures[i]
        if dd < temperatures[i +1]:
            if temperatures[i + 1] > temperatures[i + 2]:
                dsds.append(temperatures[i + 1])

    return dsds



##################
#   Question 4   #
##################
def stage_summary(records):
    pi = {k:v for item in records for k,v in item.items()}
    num = pi['stage']
    
    kei = f'stage {num}'
    return {kei: pi["duration_hours"]}


##################
#   Question 5   #
##################

def draw_triangle(height):

  

    return ""

 