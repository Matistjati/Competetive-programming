# Solving https://challenges.reply.com/tamtamy/challenge/code-teen2020/detail
def main():
    def compare(a,b):
        if a[0]<b[0]:
            return -1
        elif a[0]>b[0]:
            return 1

        else:
            if a[1]<b[1]:
                return 1
            elif a[1]>b[1]:
                return -1
            else:
                if a[2]<b[2]:
                    return 1
                elif a[2]>b[2]:
                    return -1
                else:
                    return 0
    
    def getnextline(lines, line):
        a = lines[line[0]]
        line[0] += 1
        return a

    lines = []
    with open("input.txt", "r") as inp:
        l = inp.read()
        lines = l.splitlines()
    index = [0]
    t = int(getnextline(lines,index))
    print(len(lines))
    print("HOI")


    with open("output.txt", "w") as f:

        for case in range(t):
            teamCount, logCount = [int(i) for i in getnextline(lines,index).split()]
            teams = []
            for i in range(teamCount):
                teams.append([0,0, i+1])
            logs = {}
            for i in range(teamCount):
                logs[i+1] = [] 
            for i in range(logCount):
                log = [int(i) for i in getnextline(lines,index).split()]
                logs[log[1]].append([log[0], log[1], log[2], log[3], log[4]])

            #print(logs)
            
            
            for key, value in logs.items():
                problems = {}
                #print(value)
                for log in value:
                    if log[2] in problems:
                        if log[3] in problems[log[2]]:
                            if problems[log[2]][log[3]][1] == 0:
                                problems[log[2]][log[3]] = [log[0],log[4]]
                        else:
                            problems[log[2]][log[3]] = [log[0],log[4]]         
                    else:
                        problems[log[2]] = {log[3]: [log[0],log[4]]}

                for _, prob in problems.items():
                    for inputId, sub in prob.items():
                        if sub[1]:
                            teams[key-1][0] += inputId * 100
                            teams[key-1][1] += sub[0]

            from functools import cmp_to_key

            teams = sorted(teams, key=cmp_to_key(compare), reverse=True)
            result = "Case #" + str(case+1) + ":"

            for i in teams:
                result += " " + str(i[2])
            f.write(result + "\n")
            print(result)

import cProfile
cProfile.run('main()')
