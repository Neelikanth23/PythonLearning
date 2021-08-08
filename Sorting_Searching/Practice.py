arr= [0,0,2,1,1]
n = len(arr)


def fourSum(arr, k):
    # code here
    result = set()
    mp = {}
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            mp[arr[i] + arr[j]] = [i, j]

    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = arr[i] + arr[j]
            if (k - sum) in mp.keys():
                p = mp[k - sum]
                if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):

                    r = arr[i], arr[j], arr[p[0]], arr[p[1]]

                    #result.add(r)

    return result
#print(fourSum(arr,3))

s = ["sairam", "ram"]
print(s[0])


s1 = "raji"
print(s1[0])