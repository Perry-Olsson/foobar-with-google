testStr = "abaabaaba"


def solution(s):
    # Your code here
    mostSlices = 1
    stringLength = len(s)
    stringSlice = 1
    while stringSlice <= stringLength / 2:
        if stringLength % stringSlice == 0:
            slices = stringLength / stringSlice
            i = stringSlice
            testSlice = s[0:stringSlice]
            while i < stringLength:
                if s[i:i + stringSlice] != testSlice:
                    break
                else:
                    i += stringSlice
            if i >= stringLength and slices > mostSlices:
                mostSlices = slices
        stringSlice += 1
    return mostSlices


print(solution(testStr))


def solution2(s):
    stringLength = len(s)
    stringSlice = 1
    i = stringSlice
    while i < stringLength:
        if stringLength % stringSlice != 0 or s[i] != s[i - stringSlice]:
            stringSlice = i + 1
        i += 1
    if stringSlice > stringLength / 2:
        return 1
    return stringLength / stringSlice


print(solution2(testStr))
