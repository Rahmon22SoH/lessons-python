studends_sorces = [2,5,5,4,2,3] 

avg_score = 0
for score in studends_sorces:
    print('До', avg_score)
    avg_score = avg_score + score
    print('После', avg_score)

class_avg = avg_score / len(studends_sorces)
print('Средн оценка ', class_avg)

