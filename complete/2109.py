# https://daimhada.tistory.com/42?category=810236
import sys

def solution(payList, dCountList, dSet):
    total = 0
    payList = sorted(payList, key=lambda fee: fee[0], reverse=True)
    payList = sorted(payList, key=lambda fee: fee[1], reverse=True)

    while dSet:
        first_d = dSet.pop(0) # first deadline
        next_d = 0 # if no more deadline option is in dSet, next_d should be 0
        if len(dSet) > 0:
            next_d = dSet[0]
        period = first_d - next_d # number of days you can go to lecture.
        dCount = dCountList[str(first_d)] # Number of lectures requested by the deadline
        # if you have enough time, you can go all options.
        if period >= dCount:
            for i in range(dCountList[str(first_d)]):
                option = payList.pop(0)
                total += option[0]
        else:
            # Sort by fee as dCount
            selected_options = sorted(payList[:dCount], key=lambda option:option[0], reverse=True)
            extra_options = []
            # If the deadline is short, only the number of options available will go to the lecture.
            for i in range(dCount):
                if i < period:
                    # 기한 내
                    option = selected_options[i]
                    total += option[0]
                else:
                    if next_d == 0:
                        break
                    else:
                        # exceeded options are changed to next deadline.
                        extra_options.append((selected_options[i][0], next_d))
            if next_d != 0:
                # add count about changed options
                dCountList[str(next_d)] += len(extra_options)
            payList = extra_options + payList[dCount:]
    return total


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    payList = []
    dCountList = {} # check same deadline count.
    dSet = set() # The set value of the proposed deadlines
    for i in range(n):
        p, d = map(int, sys.stdin.readline().strip().split())
        if str(d) in dCountList:
            dCountList[str(d)] += 1
        else:
            dSet.add(d)
            dCountList[str(d)] = 1
        payList.append((p,d))
    dSet = sorted(dSet, reverse=True)
    print(solution(payList, dCountList, dSet))