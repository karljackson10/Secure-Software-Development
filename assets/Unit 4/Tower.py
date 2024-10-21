
def move_disc (old, target, pegs):
    d=pegs[old].pop()
    pegs[target].append(d)
    show_pegs (pegs)
    return
    
    
def tower(n,a,b,c):
    """move tower with n at base"""
    if n == 1:
        move_disc (a,b,pegs)
    else:
        
        tower(n-1, a, b,c) 
        #tower(1, a, c,b) 
        #tower (n-1,b,c,a) 

    
def show_pegs (pegs):
    for p in range( len(pegs)):
        print(pegs[p])
    print()    
    return

#Empty All Pegs
peg_A =[]
peg_B=[]
peg_C =[]
pegs=[peg_A, peg_B, peg_C]

peg_A = [3,2,1]
pegs=[peg_A, peg_B, peg_C]
show_pegs(pegs)
tower(5,0,2,1)

#move_disc(0, 2, pegs)

