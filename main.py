print('Это викторина на знание жанров игр. Ответь на вопросы и узнай, насколько хорошо ты разбираешься в компьютерных играх, не расстраивайся если не получилось. Удачи в тесте!')

score = 0

question1 = 'К какому жанру игр относятся футбол, баскетбол? '
question2 = 'К какому жанру игр относятся стрелялки? '
question3 = 'К какому жанру игр относится езда на машинах? '
question4 = 'К какому жанру игр относятся карты? '
question5 = 'К какому жанру игр относятся игры, где ты можешь делать всё? '
question6 = 'К какому жанру игр относятся игры, где есть сюжет? '

true_answer1 = 'спорт'
true_answer2 = 'шутеры'
true_answer3 = 'гонки'
true_answer4 = 'настольные'
true_answer5 = 'игры с открытым миром'
true_answer6 = 'сюжетные'

answer1 = input(question1)
if true_answer1 == answer1:
  score += 1
answer2 = input(question2)
if true_answer2 == answer2:
  score += 1
answer3 = input(question3)
if true_answer3 == answer3:
  score += 1
answer4 = input(question4)
if true_answer4 == answer4:
  score += 1
answer5 = input(question5)
if true_answer5 == answer5:
  score += 1
answer6 = input(question6)
if true_answer6 == answer6:
  score += 1
  
if score >= 3:
  print("Вы набрали много баллов! Вас можно считать экспертом")
else:
  print("Вы набрали не очень много баллов. Расширяйте свой кругозор, вам есть, куда стремиться")