# https://edyst.com/cohort/daily-coding-challenge-april-2020-0L0oG/module/daily-coding-challenge-april-2020-JxE19/topic/challenge-6-qYY07/question/6/name/-M4Yk3Gb7iFoFQZD9c-y?is_required=1

t = int(input())
for i in range(t):
    dic_voter  ={}
    party_win = []

    parti = input().split()
    num_party = int(parti[0])
    p_name = parti[1:]

  
    voter = input().split()
    num_voter = int(voter[0])
    v_pass = voter[1:]

    for i in range(len(v_pass)):
        dic_voter[v_pass[i]] = len(set(v_pass[i]))


    for i in dic_voter.values():
        for j in range(len(p_name)):
            if i == len(set(p_name[j])):
                party_win.append(p_name[j])

    if party_win == []:
        print("stalemate")
    else:
        party_win.sort()
        for i in party_win:
            print(i,end = " ")
            
    print("\n")
