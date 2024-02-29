bicycles = ['trek','cannondale','redline','specialized']
message = f'My first bicycle was a {bicycles[-2].title()}.'
print(message)
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('GM')
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)
motorcycles.insert(0,'')
print(motorcycles)
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)
motorcycles.sort(reverse=True)
print(motorcycles)
print(sorted(motorcycles))
print(motorcycles)
print(len(motorcycles))
for motorcycle in motorcycles:
    print(motorcycle)
    print(f"my motorcycle is a {motorcycle.title()}.")
print("리스트 출력완료!")

for motorcycle2 in motorcycle:
    print('my car\n')
    for c2 in motorcycle:
        print()

