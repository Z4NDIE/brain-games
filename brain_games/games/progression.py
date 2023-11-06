from random import randint

RULES = 'What number is missing in the progression?'


def make_progression(progression_len,
                     step,
                     min_num, max_num):
    first_num = randint(min_num, max_num)
    progression_step = randint(step)
    progression = [first_num, ]
    for i in range(progression_len):
        next_num = first_num + step
        progression.append(next_num)
        first_num = next_num
    return progression


def question_and_correct_answer():
    progression = make_progression(10, 5, 0, 30)
    random_index = randint(0, (len(progression) - 1))
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)
