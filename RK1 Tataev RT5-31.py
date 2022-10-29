from operator import itemgetter
 
class Teacher:
    def __init__(self, id, fio, sal, course_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.course_id = course_id
 
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class TC:
    def __init__(self, course_id, teacher_id):
        self.course_id = course_id
        self.teacher_id = teacher_id

courses = [Course(1, "Мат. анализ"),
           Course(2, "Ораторское мастерство"),
           Course(3, "Линейная алгебра"),
           Course(4, "Прикладная ритуалистика и оккультные технологии")]

teachers = [Teacher(1, "Гжегож Бженчишчикевич", 30000, 2),
            Teacher(2, "Жак Ле-Вак", 15000, 1),
            Teacher(3, "GORUDA SUMITH", 999999, 4)]

tc = [TC(1, 2),
      TC(2, 1),
      TC(3, 2),
      TC(4, 3)]

def main():
    otm = [(t.fio, t.sal, c.name) 
        for t in teachers 
        for c in courses 
        if t.course_id==c.id]
    
    mtm_temp = [(c.name, _.course_id, _.teacher_id) 
        for c in courses 
        for _ in tc 
        if c.id==_.course_id]
    
    mtm = [(t.fio, t.sal, course_name) 
        for course_name, course_id, teacher_id in mtm_temp
        for t in teachers if t.id==teacher_id]
 
    print('Задание E1')
    word = 'н'
    result1 = [c.name for c in courses if word in c.name]
    result2 = [t[0] for t in otm if t[2] in result1]
    print(result1, result2)

    print('\nЗадание E2')
    result = []
    for c in courses:
        sals = [s[1] for s in otm if s[2] == c.name]
        if sals:
            avsal = round(sum(sals)/len(sals), 2)
        else:
            avsal = 0
        result.append((c.name, avsal))
    print(sorted(result, key=itemgetter(1), reverse=True))
    
    print('\nЗадание E3')
    char3 = "Ж"
    print([(t.fio,[m[2] for m in mtm if m[0]==t.fio]) for t in teachers if t.fio[0] == char3])
    
if __name__ == '__main__':
    main()
