# https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q/description

def firstDuplicate(a):
    di = {}
    for i in range(len(a)):
        if a[i] not in di:
            di[i] = a[i]
    print(di)
