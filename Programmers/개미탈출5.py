import sys

input = sys.stdin.readline

def fight(Jun_locate,JunATK, JunHP, monster):
    for m in monster:
            if Jun_locate == m[0]-1: 
                while True: 
                    m[2] -= JunATK
                    if m[2] <= 0: 
                        break 
                    JunHP -= m[1]
    return JunHP

def escape(world_length, strength, world, j_atk, j_hp, monster, rl):
    j_locate = world.index("@")
    if rl == 'left':
        while True:
            j_locate-=1
            if j_locate < 0 :
                return False
            if world[j_locate] == '#':
                strength -= 1
                if strength < 0 :
                    return False
            elif world[j_locate] == '&':
                j_hp = fight(j_locate,j_atk,j_hp,monster)
                if j_hp <= 0:
                    return False
            elif world[j_locate] == 'O':
                return True
    else:
        while True:
            j_locate+=1
            if j_locate > world_length-1:
                return False
            if world[j_locate] == '#':
                strength -=1
                if strength < 0 :
                    return False
            elif world[j_locate] == '&':
                j_hp = fight(j_locate,j_atk,j_hp,monster)
                if j_hp <= 0:
                    return False
            elif world[j_locate] == 'O':
                return True

def main():
    testcase = int(input())
    for _ in range(testcase):
        # 입력받는 곳
        mapLength, strength, monsters = map(int, input().split())
        world = input()
        JunATK, JunHP = map(int, input().split())
        Jatk = JunATK
        Jhp = JunHP
        monster=[list(map(int, input().split())) for mon in range(monsters) ]
        input()
        if escape(mapLength, strength, world, Jatk, Jhp, monster,'right') or escape(mapLength, strength, world, Jatk, Jhp, monster,'left'):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
