def full_line(userchr):
    for i in range(0,120):
        print(userchr,end='')
    print()
    
def border(userchr):
    print(userchr,end='')
    print(userchr,end='')
    for i in range(2,118):
        print(' ',end='')
    print(userchr,end='')
    print(userchr,end='')
    print()

def title_screen_newgame(userchr):
    for i in range(0,2):
        full_line(userchr)
        
    for i in range(2,7):
        border(userchr)
    
    print(userchr,end='')
    print(userchr,end='')
    for i in range(2,28):
        print(' ',end='')
    print('╔══ ═╦═ ╔══╗ ╔═╗ ║     ═╦═ ╔═╗ ╔═╗ ╔══╗ ╔══ ═╦═ ═╦═ ═╦═ ╔═╗ ╔══╗ ',end='')
    for i in range(93,118):
        print(' ',end='')
    print(userchr,end='')
    print(userchr)
    
    print(userchr,end='')
    print(userchr,end='')
    for i in range(2,28):
        print(' ',end='')
    print('╠═   ║  ║  ║ ╠═╣ ║      ║  ╠╦╝ ╠═╣ ║  ║ ╚═╗  ║   ║   ║  ║ ║ ║  ║ ',end='')
    for i in range(93,118):
        print(' ',end='')
    print(userchr,end='')
    print(userchr)
    
    print(userchr,end='')
    print(userchr,end='')
    for i in range(2,28):
        print(' ',end='')
    print('║   ═╩═ ║  ║ ║ ║ ╚══    ║  ║║  ║ ║ ║  ║ ══╝ ═╩═  ║  ═╩═ ╚═╝ ║  ║ ',end='')
    for i in range(93,118):
        print(' ',end='')
    print(userchr,end='')
    print(userchr)
    
    for i in range(10,22):
        border(userchr)
        
    print(userchr,end='')
    print(userchr,end='')
    for i in range(2,48):
        print(' ',end='')
    print('--- < New Game > ---',end='')
    for i in range(68,118):
        print(' ',end='')
    print(userchr,end='')
    print(userchr)   
        
    for i in range(23,27):
        border(userchr)    
    
    print(userchr,end='')
    print(userchr,end='')
    for i in range(2,52):
        print(' ',end='')
    print('< Load Game >',end='')
    for i in range(63,116):
        print(' ',end='')    
    print(userchr,end='')
    print(userchr) 
    
    for i in range(28,38):
        border(userchr)    
            
    for i in range (38,40):
        full_line(userchr)
        
        
def title_screen_loadgame(userchr):
    for i in range(0,2):
        full_line(userchr)
        
    for i in range(2,7):
        border(userchr)
    
    print(userchr,end='')
    print(userchr,end='')
    for i in range(2,28):
        print(' ',end='')
    print('╔══ ═╦═ ╔══╗ ╔═╗ ║     ═╦═ ╔═╗ ╔═╗ ╔══╗ ╔══ ═╦═ ═╦═ ═╦═ ╔═╗ ╔══╗ ',end='')
    for i in range(93,118):
        print(' ',end='')
    print(userchr,end='')
    print(userchr)
    
    print(userchr,end='')
    print(userchr,end='')
    for i in range(2,28):
        print(' ',end='')
    print('╠═   ║  ║  ║ ╠═╣ ║      ║  ╠╦╝ ╠═╣ ║  ║ ╚═╗  ║   ║   ║  ║ ║ ║  ║ ',end='')
    for i in range(93,118):
        print(' ',end='')
    print(userchr,end='')
    print(userchr)
    
    print(userchr,end='')
    print(userchr,end='')
    for i in range(2,28):
        print(' ',end='')
    print('║   ═╩═ ║  ║ ║ ║ ╚══    ║  ║║  ║ ║ ║  ║ ══╝ ═╩═  ║  ═╩═ ╚═╝ ║  ║ ',end='')
    for i in range(93,118):
        print(' ',end='')
    print(userchr,end='')
    print(userchr)
    
    for i in range(10,22):
        border(userchr)
        
    print(userchr,end='')
    print(userchr,end='')
    for i in range(2,52):
        print(' ',end='')
    print('< New Game >',end='')
    for i in range(64,118):
        print(' ',end='')
    print(userchr,end='')
    print(userchr)   
        
    for i in range(23,27):
        border(userchr)    
    
    print(userchr,end='')
    print(userchr,end='')
    for i in range(2,48):
        print(' ',end='')
    print('--- < Load Game > ---',end='')
    for i in range(67,116):
        print(' ',end='')    
    print(userchr,end='')
    print(userchr) 
    
    for i in range(28,38):
        border(userchr)    
            
    for i in range (38,40):
        full_line(userchr)
        
# title_screen_loadgame('x')