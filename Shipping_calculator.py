def ground_shipping(weight):
    if weight <= 2:
        cost = weight * 1.50 + 20.00
        return cost
    elif weight > 2 and not weight >= 6:
        cost = weight * 3.00 + 20.00
        return cost
    elif weight > 6 and not weight >= 10:
        cost = weight * 4.00 + 20.00
        return cost
    elif weight > 10:
        cost = weight * 4.75 + 20.00
        return cost

premium_ship_ground = 125.00

def drone_shipping(weight):
    if weight <= 2:
        cost = weight * 4.50 + 00.00
        return cost
    elif weight > 2 and not weight >= 6:
        cost = weight * 9.00 + 00.00
        return cost
    elif weight > 6 and not weight >= 10:
        cost = weight * 12.00 + 00.00
        return cost
    elif weight > 10:
        cost = weight * 14.25 + 00.00
        return cost

def calculate_shipping(weight):
    x = ground_shipping(weight)
    y = premium_ship_ground
    z = drone_shipping(weight)

    if x < y and x < z:
        print ("Ground shipping is the cheapest i.e. $" + str(x))
    elif y < x and y < z:
        print ("Premium shipping is the cheapest i.e. $" + str(y))
    elif z < x and z < y:
        print ("Premium shipping is the cheapest i.e. $" + str(y))

print(calculate_shipping(4.8))
print(calculate_shipping(41.5))
print(calculate_shipping(17))

