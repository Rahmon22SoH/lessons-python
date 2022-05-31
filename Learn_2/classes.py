classes = [
    {'name': '3А', 'scores': [3,5,4,5,4,4]},
    {'name': '3Б', 'scores': [3,5,4,5,1,1]},
    {'name': '3В', 'scores': [3,5,4,5,1,1]},
]

def class_count_avg(student_scores):
    scores_sum = 0                    # Для чего переменная ?
    for scores in student_scores:
        scores_sum += scores
    return scores_sum / len(student_scores) # Почему не на 'classes'

school_avg_sum = 0
for one_class in classes:
    class_avg = class_count_avg(one_class['scores'])
    print(f"Средняя оценка в классе {one_class['name']}: {round(class_avg)} ")
    school_avg_sum += class_avg

school_avg = round(school_avg_sum / len(classes),2)
print(f"Средняя оценка по Школе {school_avg}")
        