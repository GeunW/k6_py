#def describe_pet(animal_type, pet_name):
def describe_pet(pet_name, animal_type='dog'):
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet()
print("********************************")
describe_pet('harry')
print("********************************")
describe_pet(pet_name='harry')
print("********************************")
describe_pet(pet_name='harry', animal_type='hamster')

def get_formatted_name(first_name, last_name, middle_name):
    """실제 이름 형식"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
    
print("********************************")
#musician = get_formatted_name('Jimi','hexdrix')
#print(musician)
print("********************************")
musician = get_formatted_name('Jimi','hexdrix','L')
print(musician)
