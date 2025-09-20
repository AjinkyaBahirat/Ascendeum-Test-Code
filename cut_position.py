#random logic pending
import random

MAX_Player = 4
# sample player positions and dice roll
#ppdr = [{"pp":[1,2],"dr":[2,2]},{"pp":[1,2],"dr":[2,2]}]
def next_pp(p,cpp,ppdr):
    if ppdr[p]:
        player_data = ppdr[p]
    else:
        player_data = {"pp":[]}
    ppl = player_data.get("pp",[])
    if len(ppl) == 0:
        opp = 0
    else:
        opp = ppl[-1]
    if opp == cpp:
        return True
    else:
        if p>4:
            return False
        else:
            next_pp(p+1,cpp,ppdr)
            
ppdr = [{},{},{},{}]
def main(grid):
    total_positions = grid*grid
    print(total_positions)
    initial_position = 1
    i = 0
    drc = 0
    while i<=total_positions:
        for p in range(0,MAX_Player):
            player = p+1
            print(f"Player {player} Turn")
            #get oher players position
          
            if ppdr[p]:
                player_data = ppdr[p]
            else:
                player_data = {"pp":[0],"dr":[]}
                
            pp = player_data["pp"]
            dr = player_data["dr"]
            
            #get random number from 1-6
            random = generate_random()
            print("Random Dice Roll::",random)
            dr.append(random)
            pos = pp[-1] + random
            
            if drc >1:
                check_pp = next_pp(p,pos,ppdr)
                if check_pp:
                    pos = 0
                
            i = pos
            if pos == total_positions:
                pp.append(pos)
                ppdr[p] = {"pp":pp,"dr":dr}
                print("Position and Dice Roll::",ppdr[p])
                print(f"Winner is Player ::: {player} !!!!!!!!!!!!")
                return ppdr
            elif pos > total_positions:
                pp.append(pp[-1])
                i = pp[-1]
            else:
                pp.append(pos)
            ppdr[p] = {"pp":pp,"dr":dr}
            print("Position and Dice Roll::",ppdr[p])
    drc +=1
    return ppdr

def generate_random():
    num = int(random.random()*10)
    if num > 0 and num <=6:
        return num
    else:
        rgenrand = generate_random()
        return rgenrand
        
res = main(3)
print("--------------------FINAL------------------------")
print(res)


