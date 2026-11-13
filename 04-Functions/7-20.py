def f(n):
    licznik = 0
    kandydat = 1
    
    while licznik < n:
        kandydat += 1
        
        czy_pierwsza = True
        for i in range(2, kandydat):
            if kandydat % i == 0:
                czy_pierwsza = False
                break
                
        if czy_pierwsza:
            licznik += 1
            
    return kandydat