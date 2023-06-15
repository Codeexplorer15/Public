class Profile:
    def __init__(self, age, food_pref, location, birth_control_cert, income):
        self.age = age
        self.food_pref = food_pref
        self.location = location
        self.birth_control_cert = birth_control_cert
        self.income = income

def check_profile(profile, min_age, food_pref, location, birth_control_cert_required, min_income):
    if not (profile.age >= min_age and \
            food_pref in profile.food_pref and \
            profile.location == location and \
            profile.birth_control_cert == birth_control_cert_required and \
            profile.income >= min_income):
        print(f"Slide right for profile: {profile}")
    else:
        print(f"swipe rigth")

# Define your filter criteria
min_age = 18
food_pref = 'Subway sandwich'
your_location = 'florida'
birth_control_cert_required = 'Yes'
min_income = 10000

# Create the profile
user_profile = Profile(20, 'Subway sandwich', 'florida', 'Yes', 15000)

# Check the profile
check_profile(user_profile, min_age, food_pref, your_location, birth_control_cert_required, min_income)
