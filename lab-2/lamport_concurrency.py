import random

def display(e, p):
    print()
    print("The time stamps of events in each process:")
    for i in range(e):
        print("P" + str(i+1) + ":", end=" ")
        for j in range(e):
            print(p[i][j], end=" ")
        print()

def lamportLogicalClock(e, m):
    p = [[0]*e for _ in range(e)]

    for i in range(e):
        for j in range(e):
            p[i][j] = j + 1

    for i in range(e):
        print("\t", end="")
        print("e" + str(i+1), end="")

    for i in range(e):
        print()
        print("e" + str(i+1), end="\t")
        for j in range(e):
            print(m[i][j], end="\t")

    for i in range(e):
        for j in range(e):
            if m[i][j] == 1:
                p[j][j] = max(p[j][j], p[i][j] + 1)
                for k in range(j + 1, e):
                    p[j][k] = p[j][k - 1] + 1

            if m[i][j] == -1:
                p[i][i] = max(p[i][i], p[i][j] + 1)
                for k in range(i + 1, e):
                    p[k][i] = p[k - 1][i] + 1

    display(e, p)
    detect_concurrent_events(e, p)

def detect_concurrent_events(e, p):
    print("\nConcurrent Events:")
    for i in range(e):
        for j in range(e):
            for k in range(e):
                for l in range(e):
                    if (i != k or j != l) and p[i][j] == p[k][l]:
                        print(f"Events P{i+1}e{j+1} and P{k+1}e{l+1} are concurrent")

if __name__ == "__main__":
    e = 5  
    m = [[0]*e for _ in range(e)]

    for i in range(e):
        for j in range(e):
            if random.random() < 0.35:
                m[i][j] = 0
            else:
                m[i][j] = random.choice([1, -1])


    lamportLogicalClock(e, m)