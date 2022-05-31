from posixpath import split


for num in range(3):
    print(f"Номер {num}")

for letter in 'Python':
    print(letter)

my_string = "Привет я учу Пайтон"

for word in my_string.split():
    print(f"Длинна слова {word}: {len(word)}")

studends_sorces = [1,5,5,4,2,3] 

avg_score = 0
for score in studends_sorces:
    avg = avg_score + score
    print(avg)

