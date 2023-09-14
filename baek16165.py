
n,m = map(int, input().split())
group = {}
mem_group = {}
for _ in range (n):
    groupname = input()
    groupsize = int(input())
    group[groupname]= []
    for j in range (groupsize):
        name = input()
        group[groupname].append(name)
        mem_group[name] = groupname
for _ in range (m):
    name = input()
    gametype = int(input())
    # 1이면 팀이름, 0이면 멤버이름 사전순
    if gametype == 0:
        for i in sorted(group[name]):
            print(i)
    else:
        print(mem_group[name])
