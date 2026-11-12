

Input = ["eat", "tea", "tan", "ate", "nat", "bat", "tab", "cab"]

string = []
visited = []

for i in Input:
    if i not in visited:
        temp = []
        for j in Input:
            if len(i) == len(j):
                count = 0

                for a in i:
                    for b in j:
                        if a == b:
                            count += 1
                            break

                if count == len(i):
                    temp.append(j)
                    visited.append(j)

        string.append(temp)

print(string)
