## Collatz Sequence

## Idea from Al Sweigart's 'Automate the Boring Stuff'

def collatz():
    global over
    over = False
    print("Lets Explore the Collatz Sequence")
    print("Often called the simplest impossible math problem,")
    print("the premise is simple, but the results are confusing!")
    print("Lets start and see if you can catch on...")
    
    c = ''
    while c == '':
        try:
            c = int(input("Type in any integer: "))
        except ValueError:
            print("Thats very funny but its NOT an integer")
            
    while c != 1:
        if c % 2 == 0:
            c = c // 2
            print(c)
        elif c % 2 == 1:
            c = (3 * c) + 1
            print(c)
            
    if c == 1:
        print("Do you get it?")
        print("For ANY real integer, you can reduce it down to 1 using the Collatz Sequence")
        print("If the number is even, take n/2")
        print("If the number is odd, take 3n+1")
        print("Follow that sequence with your answers until you reach 1")
    
    print()    
    print("Lets keep going")
    print("Type 0 at any point to return to the Games screen")
    
    while over == False:
        newc = ''
        while newc != 0:
            try:
                print("-" * 65)
                newc = int(input("Type in any number: "))
            except ValueError:
                print("Thats very funny but its NOT a number")
            
            if newc == 0:
                over = True
                break
            
            
            while newc != 1:
                if newc % 2 == 0:
                    newc = newc // 2
                    print(newc)
                elif newc % 2 == 1:
                    newc = (3 * newc) + 1
                    print(newc)
        
