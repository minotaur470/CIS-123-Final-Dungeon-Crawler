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

def title_screen(userchr):
    for i in range(0,2):
        full_line(userchr)
    for i in range(2,38):
        border(userchr)
    for i in range (38,40):
        full_line(userchr)
        
title_screen('x')