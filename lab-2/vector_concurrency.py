import random

def display_vector_clocks(e, p):
    print()
    print("The vector clocks of events in each process:")
    for i in range(e):
        print("P" + str(i+1) + ":")
        for j in range(e):
            print("e" + str(j+1) + ":", end=" ")
            print(p[i][j])
        print()

def vectorClocks(e, m):
    p = [[[0]*e for _ in range(e)] for _ in range(e)]

    for i in range(e):
        for j in range(e):
            p[i][j][i] = j + 1

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
                for k in range(e):
                    p[j][j][k] = max(p[j][j][k], p[i][j][k])
                p[j][j][j] += 1
                for k in range(j + 1, e):
                    for l in range(e):
                        p[j][k][l] = p[j][k - 1][l]
                    p[j][k][j] += 1

            if m[i][j] == -1:
                for k in range(e):
                    p[i][i][k] = max(p[i][i][k], p[i][j][k])
                p[i][i][i] += 1
                for k in range(i + 1, e):
                    for l in range(e):
                        p[k][i][l] = p[k - 1][i][l]
                    p[k][i][i] += 1

    display_vector_clocks(e, p)
    detect_concurrent_events_vector(e, p)

def detect_concurrent_events_vector(e, p):
    print("\nConcurrent Events:")
    for i in range(e):
        for j in range(e):
            for k in range(e):
                for l in range(e):
                    if (i != k or j != l) and not happened_before(p[i][j], p[k][l]) and not happened_before(p[k][l], p[i][j]):
                        print(f"Events P{i+1}e{j+1} and P{k+1}e{l+1} are concurrent")

def happened_before(vc1, vc2):
    for i in range(len(vc1)):
        if vc1[i] > vc2[i]:
            return False
    return vc1 != vc2

if __name__ == "__main__":
    e = 5  
    m = [[0]*e for _ in range(e)]

    for i in range(e):
        for j in range(e):
            if random.random() < 0.35:
                m[i][j] = 0
            else:
                m[i][j] = random.choice([1, -1])

    vectorClocks(e, m)