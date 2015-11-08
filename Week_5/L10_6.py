mySortEntries = 0
newSortEntries = 0

def mySort(L):
    global mySortEntries
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            mySortEntries += 1
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                
def newSort(L):
    global newSortEntries
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            newSortEntries += 1
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1

rawList = [5, 3, 8, 7, 4, 2, 1, 9, 6]
L1 = rawList[:]
L2 = rawList[:]

mySort(L1)
newSort(L2)

print "My Sort Entries: " + str(mySortEntries)
print "New Sort Entries: " + str(newSortEntries)