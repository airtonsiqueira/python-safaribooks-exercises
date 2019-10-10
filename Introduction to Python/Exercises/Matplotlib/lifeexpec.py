from matplotlib import pyplot

data = open("Matplotlib/life_expectancies_usa.txt", "r").readlines()

dates = []
males = []
females = []

for line in data:
    date, male, female = line.split(",")
    dates.append(date)
    males.append(male)
    females.append(female)

pyplot.plot(dates, males, "bo-", label="Men")
pyplot.plot(dates, females, "mo-", label="Women")

pyplot.legend(loc="upper left")
pyplot.xlabel("Year")
pyplot.ylabel("Age")
pyplot.title("Life Expectancies for Women and Men in the USA over time")
pyplot.show()
