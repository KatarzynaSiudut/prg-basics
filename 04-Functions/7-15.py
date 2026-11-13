def f(detector):
    current_people = 0
    
    for x in detector:
        if x == '+':
            current_people += 1  
        elif x == '-':
            current_people -= 1  
        if current_people >= 3:
            return True
            
    return False

print(f("+-+++-+---"))   
print(f("+-+-+-+-"))     
print(f("+-++-+--"))     
print(f("+-++-++-+---"))










    
    
