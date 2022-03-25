# zadanie 2
class Worker:
    def __init__(self, number, name, age, salary):
        self.number = number
        self.name = name
        self.age = age
        self.salary = salary


def average_salary(workers):
    num_of_workers = len(workers)
    salary_sum = 0
    for w in workers:
        salary_sum += w.salary
    return salary_sum / num_of_workers


def average_salary_age(workers):
    try:
        below_30 = 0
        below_30_sum = 0
        older = 0
        older_sum = 0

        for w in workers:
            if 2022 - w.age < 30:
                below_30 += 1
                below_30_sum += w.salary
            else:
                older += 1
                older_sum += w.salary
        result = (below_30_sum / below_30) - (older_sum / older)
        if result < 0:
            print('Średnie zarobki osób poniżej 30 roku życia są mniejsze o', "{:.2f}".format(abs(result)))
        elif result > 0:
            print('Średnie zarobki osób poniżej 30 roku życia są większe o', "{:.2f}".format(result))
        else:
            print('Zarobki są równe')
    except ZeroDivisionError:
        print('Jedna z grup wiekowych jest pusta!')


if __name__ == '__main__':
    w1 = Worker(1, 'Adam', 1983, 1500)
    w2 = Worker(2, 'Anna', 1981, 1700)
    w3 = Worker(3, 'Błażej', 1990, 1800)
    w4 = Worker(4, 'Beata', 1993, 1600)
    w5 = Worker(5, 'Czesław', 1980, 2000)
    w6 = Worker(6, 'Cecylia', 1983, 2100)
    w7 = Worker(7, 'Daniel', 1976, 1900)

    workers = [w1, w2, w3, w4, w5, w6, w7]
    print('Średnia pensja:')
    print(average_salary(workers))
    print('Średnia wg wieku:')
    average_salary_age(workers)
