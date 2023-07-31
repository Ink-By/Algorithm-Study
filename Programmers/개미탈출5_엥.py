import sys

input = sys.stdin.readline


def verifyJun(world):
    return world.index("@")


def checkGate(world, JunLocation):
    GateLocation = []
    index = JunLocation
    if "O" in (world[0 : JunLocation + 1]):
        while True:
            if index < 0:
                break
            if world[index] == "O":
                GateLocation.append(index)
                break
            index -= 1
    index = JunLocation
    if "O" in (world[JunLocation : len(world)]):
        while True:
            if index > len(world) - 1:
                break
            if world[index] == "O":
                GateLocation.append(index)
                break
            index += 1
    return GateLocation


def findMonster(monster, indexNum):
    for mons in monster:
        if mons[0] - 1 == indexNum:
            atk = mons[1]
            hp = mons[2]
            return atk, hp


def fight(JunATK, JunHP, monsterATK, monsterHP):
    while True:
        monsterHP -= JunATK
        if monsterHP <= 0:
            junWin = True
            return JunHP, junWin
        JunHP -= monsterATK
        if JunHP <= 0:
            junWin = False
            return JunHP, junWin



def main():
    testcase = int(input())
    for _ in range(testcase):
        # 입력받는 곳
        mapLength, strength, monsters = map(int, input().split())
        mapInput = input()
        world = [m for m in mapInput]
        JunATK, JunHP = map(int, input().split())
        Jatk = JunATK
        Jhp = JunHP
        monster = []
        for mon in range(monsters):
            monster.append(list(map(int, input().split())))
        input()
        JunLocation = verifyJun(world)
        GateLocation = checkGate(world, JunLocation)
        escaped = False

        for i in range(len(GateLocation)):
            # 준식이 atk, hp 초기화
            JunATK = Jatk
            JunHP = Jhp

            # 벽 몇번 부수는지 count 초기화
            count = 0

            # 탈출 성공여부 초기화
            escaped = False

            # 괴물을 만났는지 여부 초기화
            notmeetMonster = True

            # 괴물 싸움에서 승리여부 초기화
            junWin = False

            gate = GateLocation[i]
            if gate < JunLocation:
                # jun 왼쪽에 게이트 존재
                for adventure in range(len(world[gate : JunLocation + 1])):
                    indexNum = adventure + gate
                    if world[indexNum] == "#":
                        count += 1
                    elif world[indexNum] == "&":
                        notmeetMonster = False
                        monsterATK, monsterHP = findMonster(monster, indexNum)
                        JunHP, junWin = fight(JunATK, JunHP, monsterATK, monsterHP)

            else:
                # jun 오른쪽에 게이트 존재
                for adventure in range(len(world[JunLocation : gate + 1])):
                    # print(JunHP)
                    indexNum = adventure + JunLocation

                    if world[indexNum] == "#":
                        count += 1

                    elif world[indexNum] == "&":
                        notmeetMonster = False
                        monsterATK, monsterHP = findMonster(monster, indexNum)
                        JunHP, junWin = fight(JunATK, JunHP, monsterATK, monsterHP)
                        

            if notmeetMonster:
                if count <= strength:
                    # print("괴물 안만나고 벽부수고 나옴")
                    escaped = True
                    break
                # else:
                #     print("벽못부숨")
            else:
                if count <= strength and junWin:
                    # print("괴물 죽이고 벽부수고 나옴")
                    escaped = True
                    break
                # else:
                #     if junWin:
                #         print("벽을 못부숨")
                #     else:
                #         print("괴물 못죽였음")
        if escaped:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
