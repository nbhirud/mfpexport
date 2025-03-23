import myfitnesspal

client = myfitnesspal.Client()

day = client.get_date(2013, 3, 2)
print("********** day ***********")
print(day)
print("********** day.meals ***********")
print(day.meals)
print("********** dinner ***********")
dinner = day.meals[2]
print(dinner)
print("********** dinner entries ***********")
print(dinner.entries)
print("********** dinner first entry ***********")
spaghetti = dinner.entries[0]
print(spaghetti.name)
print("********** daily summary of your nutrition information ***********")
print(day.totals)
print("********** Dinner summary of your nutrition information ***********")
print(dinner.totals)
print("********** dinner first entry summary ***********")
print(spaghetti.totals)
print("********** meal headings ***********")
# Day objects act as dictionaries
print(day.keys())
print("********** meal headings ***********")
# Meal objects act as lists
print(len(dinner))
miser_wat = lunch[0]
print(miser_wat)
print("********** entry headings ***********")
# Entry objects act as dictionaries
print(miser_wat['calories'])

# since the measurement units returned are not necessarily very intuitive, 
# you can enable or disable unit awareness using the unit_aware keyword argument.

client = myfitnesspal.Client(unit_aware=True)
day = client.get_date(2013, 3, 2)
lunch = day['lunch']
print(lunch)
# >> [<Generic - Ethiopian - Miser Wat (Red Lentils), 2 cup {'sodium': Weight(mg=508), 'carbohydrates': Weight(g=76), 'calories': Energy(Calorie=346), 'fat': Weight(g=2), 'sugar': Weight(g=0), 'protein': Weight(g=12)}>,
miser_wat = lunch[0]
print(miser_wat['calories'])
# >> Energy(Calorie=346)