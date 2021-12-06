def lol(start_investment, interest, number_of_years):
    year_interest = start_investment
    for i in range(1, number_of_years + 1):
        year_interest = year_interest + (year_interest * interest)
        print(year_interest)

lol(100, 0.05, 4)