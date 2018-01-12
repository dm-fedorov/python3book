def func(a, b=5, c=10): 
    print('a равно', a, ', b равно', b, ', а c равно', c) 

func(3, 7) # a=3, b=7, c=10
func(25, c=24) # a=25, b=5, c=24
func(c=50, a=100) # a=100, b=5, c=50
