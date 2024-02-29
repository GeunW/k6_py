for value in range(6):
    print(value)
    numbers = list(range(6))
    print(numbers)

    squares = []
    for value in range(1,11):
        #square = value**2
        squares.append(value**2)

        print(squares)
        print(value)

        squares = [value ** 2 for value in range(1,11)] #list

        
        
        a=[1,2]
        b=[3,4]
        #덧셈
        c= a+b
        print(a)
        print(b)
        print(c)
        #빼기
        d = [x for x in c if x not in b]
        d2 = list(set(a)-set(b))
        print(d)
        print(d2)

        a = [10,20,30,40,50]
        b = a[:]
        a[0] = 100
        
        print(b)

        players = ['charles', 'martina', 'florence', 'eil']
        for player  in players[:3]:
            print(player.title())

        

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
print(my_foods)
print(friend_foods)

dimensions = (10, 20)
dimensions[0] = 30  
print(dimensions)
dimensions = (200,50)
print(dimensions)
