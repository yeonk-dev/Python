1.
score=[(100,100),(95,90),(55,60),(75,80),(70,70)]
def get_avg(score):

    for i in score:
        print(i)

        num=1
        total=0
        for j in range(len(i)):
            total=total+i[j]
        print('{}번 평균 {}'.format(num,total/2))
        num+=1
get_avg(score)

2.
score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

def get_avg(score):
  for i, v in enumerate(score):
    print(f'{i + 1} 번, 평균 : {sum(v) / 2}')

get_avg(score)

3.
def get_avg(score):
	score_avg = []
	for i in range(len(score)):
		avg = (score[i][0] + score[i][1]) / 2
		print(i, "번, 평균 :", avg)
	return
