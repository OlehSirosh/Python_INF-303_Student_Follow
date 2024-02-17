location_list = ['HQ','North','South']
location = ''
while True:
    loc_user = input("Enter HQ, North, or South for a location ")
    if loc_user not in location_list:
        print('Wrong location')
    else:
        loc_user in location_list
        print('Please come')
        location = loc_user
        break
print(f'Enter location: {location}')