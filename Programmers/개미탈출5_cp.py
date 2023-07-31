import sys
def fight(j_idx, j_atk, j_hp, Monster):
        for m_idx, m_atk, m_hp in Monster:
            if j_idx == m_idx-1: 
                while True: 
                    m_hp -= j_atk
                    if m_hp <= 0: 
                        break 
                    j_hp -= m_atk
        return j_hp 
def escape(world_length, strength, world, j_atk, j_hp, Monster, rl):
    j_idx = world.index('@') 
    if rl == 'right':
        while True:
            j_idx += 1 
            if j_idx > world_length-1:
                return False
            if world[j_idx] == '#':
                strength -= 1
                if strength < 0:
                    return False 
            elif world[j_idx] == 'O': 
                return True
            elif world[j_idx] == '&': 
                j_hp = fight(j_idx, j_atk, j_hp, Monster)
                if j_hp <= 0: 
                    return False
                
    elif rl == 'left': 
        while True:
            j_idx -= 1 
            if j_idx < 0:
                return False
            if world[j_idx] == '#':
                strength -= 1
                if strength < 0: 
                    return False
            elif world[j_idx] == 'O': 
                return True
            elif world[j_idx] == '&': 
                j_hp = fight(j_idx, j_atk, j_hp, Monster)
                if j_hp <= 0: 
                    return False

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        world_length, strength, monster = map(int, sys.stdin.readline().split()) 
        world = sys.stdin.readline()
        j_atk, j_hp = map(int, sys.stdin.readline().split())
        Monster = [tuple(map(int, sys.stdin.readline().split())) for _ in range(monster)]
        sys.stdin.readline()
        if escape(world_length, strength, world, j_atk, j_hp, Monster, 'right') or escape(world_length, strength, world, j_atk, j_hp, Monster, 'left'):
            print("YES")
        else:
            print("NO")
    
if __name__ == "__main__":
    main()
