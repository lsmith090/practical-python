dollar_bill_thickness = 1.1 * 0.0001 #meters
sears_tower_height = 443 #meters
pile_of_dollars = 1
day = 1

while pile_of_dollars * dollar_bill_thickness <= sears_tower_height:
    print(day, pile_of_dollars, pile_of_dollars * dollar_bill_thickness)
    pile_of_dollars = pile_of_dollars * 2
    day = day + 1

print('Number of days', day)
print('Number of bills', pile_of_dollars)
print('Final height', pile_of_dollars * dollar_bill_thickness)