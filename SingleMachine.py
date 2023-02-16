from math import exp
def FCFS( J, n, p, d, start):
    # M: number of machines
    # J: number of jobs
    # p: processing time
    # d: due date
    # start: start time
    
    # initialize
    S = [0]*n
    C = [0]*n
    L = [0]*n
    T = [0]*n
    E = [0]*n
    
    # FCFS
    for j in J:
        S[j] = max(start, C[j-1])
        C[j] = S[j] + p[j]
        L[j] = C[j]-d[j]
        T[j] = max(0, L[j])
        E[j] = max(0, -L[j])
    Order = list(J)
    meanTardiness = sum(T)/n
    meanEarliness = sum(E)/n
    meanLateness = sum(L)/n
    return S, C, L, T, E, Order, meanTardiness, meanEarliness, meanLateness



def SPT( J, n, p, d, start):
    # M: number of machines
    # J: number of jobs
    # p: processing time
    # d: due date
    # start: start time
    # Order: order of jobs
    J = sorted(J, key=lambda j: p[j], reverse=True)
    p = sorted(p, reverse=True)
    d = [d for _, d in sorted(zip(p, d), reverse=True)]
    # initialize
    S = [0]*n
    C = [0]*n
    L = [0]*n
    T = [0]*n
    E = [0]*n
    
    # SPT
    for j in J:
        S[j] = max(start, C[j-1])
        C[j] = S[j] + p[j]
        L[j] = C[j]-d[j]
        T[j] = max(0, L[j])
        E[j] = max(0, -L[j])
    Order = list(J)
    meanTardiness = sum(T)/n
    meanEarliness = sum(E)/n
    meanLateness = sum(L)/n
    return S, C, L, T, E,Order, meanTardiness, meanEarliness, meanLateness

def EDD( J, n, p, d, start):
    # M: number of machines
    # J: number of jobs
    # p: processing time
    # d: due date
    # start: start time
    # Order: order of jobs
    J = sorted(J, key=lambda j: d[j], reverse=True)
    p = [p for _, p in sorted(zip(d, p), reverse=True)]
    d = sorted(d, reverse=True)
    # initialize
    S = [0]*n
    C = [0]*n
    L = [0]*n
    T = [0]*n
    E = [0]*n
    
    # EDT
    for j in J:
        S[j] = max(start, C[j-1])
        C[j] = S[j] + p[j]
        L[j] = C[j]-d[j]
        T[j] = max(0, L[j])
        E[j] = max(0, -L[j])
    Order = list(J)
    meanTardiness = sum(T)/n
    meanEarliness = sum(E)/n
    meanLateness = sum(L)/n
    return S, C, L, T, E,Order, meanTardiness, meanEarliness, meanLateness
def CR(J, n, p, d, start, t):
    # M: number of machines
    # J: number of jobs
    # p: processing time
    # d: due date
    # t: Present time

    # CR = (d - t)/d
    CR = [0]*n
    for j in J:
        CR[j] = (d[j]-t)/p[j]
    # start: start time

    # Order: order of jobs
    J = sorted(J, key=lambda j: CR[j], reverse=True)
    p = [p for _, p in sorted(zip(CR, p), reverse=True)]
    d = [d for _, d in sorted(zip(CR, d), reverse=True)]
    CR = sorted(CR, reverse=True)
    # initialize
    S = [0]*n
    C = [0]*n
    L = [0]*n
    T = [0]*n
    E = [0]*n
    
    # EDT
    for j in J:
        S[j] = max(start, C[j-1])
        C[j] = S[j] + p[j]
        L[j] = C[j]-d[j]
        T[j] = max(0, L[j])
        E[j] = max(0, -L[j])
    Order = list(J)
    meanTardiness = sum(T)/n
    meanEarliness = sum(E)/n
    meanLateness = sum(L)/n
    return S, C, L, T, E,Order, meanTardiness, meanEarliness, meanLateness
def MinimumSlack(J, n, p, d, start, t):
    # M: number of machines
    # J: number of jobs
    # p: processing time
    # d: due date
    # t: Present time

    # CR = (d - t)/d
    Slack = [0]*n
    for j in J:
        Slack[j] = max(0, d[j]-t-p[j])
    # start: start time

    # Order: order of jobs
    J = sorted(J, key=lambda j: Slack[j], reverse=True)
    p = [p for _, p in sorted(zip(Slack, p), reverse=True)]
    d = [d for _, d in sorted(zip(Slack, d), reverse=True)]
    Slack = sorted(Slack, reverse=True)
    # initialize
    S = [0]*n
    C = [0]*n
    L = [0]*n
    T = [0]*n
    E = [0]*n
    
    # EDT
    for j in J:
        S[j] = max(start, C[j-1])
        C[j] = S[j] + p[j]
        L[j] = C[j]-d[j]
        T[j] = max(0, L[j])
        E[j] = max(0, -L[j])
    Order = list(J)
    meanTardiness = sum(T)/n
    meanEarliness = sum(E)/n
    meanLateness = sum(L)/n
    return S, C, L, T, E,Order, meanTardiness, meanEarliness, meanLateness
def ATC(J, n, p, d, start, t, K):
    # M: number of machines
    # J: number of jobs
    # p: processing time
    # d: due date
    # t: Present time

    # CR = (d - t)/d
    P = sum(p)/n
    ATC = [0]*n
    for j in J:
        ATC[j] = (1/n)/(p[j])*exp(-max(d[j]-t-p[j], 0)/(K*P))
    # start: start time

    # Order: order of jobs
    J = sorted(J, key=lambda j: ATC[j], reverse=True)
    p = [p for _, p in sorted(zip(ATC, p), reverse=True)]
    d = [d for _, d in sorted(zip(ATC, d), reverse=True)]
    ATC = sorted(ATC, reverse=True)
    # initialize
    S = [0]*n
    C = [0]*n
    L = [0]*n
    T = [0]*n
    E = [0]*n
    
    # EDT
    for j in J:
        S[j] = max(start, C[j-1])
        C[j] = S[j] + p[j]
        L[j] = C[j]-d[j]
        T[j] = max(0, L[j])
        E[j] = max(0, -L[j])
    Order = list(J)
    meanTardiness = sum(T)/n
    meanEarliness = sum(E)/n
    meanLateness = sum(L)/n
    return S, C, L, T, E,Order, meanTardiness, meanEarliness, meanLateness
if __name__ == "__main__":
    m=1
    n=4

    M = range(m)
    J = range(n)
    p = [20,14,35,10]
    d = [13*60+25,13*60+45,13*60+50,13*60+30]
    start = 13*60

    S, C, L, T, E, Order, meanTardiness, meanEarliness, meanLateness = FCFS(J, n, p, d, start)
    print("\n\nFCFS\n")
    print("Orden:" , Order, "\n Tiempo de inicio:", S, "\n Tiempo de finalización:", C, "\n Tiempo de latencia:", L, "\n Tiempo de tardanza:", T, "\n Tiempo de anticipación:", E, "\n Tardanza media:", meanTardiness, "\n Anticipación media:", meanEarliness, "\n Latencia media:", meanLateness)

    S, C, L, T, E, Order, meanTardiness, meanEarliness, meanLateness = SPT(J, n, p, d, start)
    print("\n\nSPT\n")
    print("Orden:" , Order, "\n Tiempo de inicio:", S, "\n Tiempo de finalización:", C, "\n Tiempo de latencia:", L, "\n Tiempo de tardanza:", T, "\n Tiempo de anticipación:", E, "\n Tardanza media:", meanTardiness, "\n Anticipación media:", meanEarliness, "\n Latencia media:", meanLateness)

    S, C, L, T, E, Order, meanTardiness, meanEarliness, meanLateness = EDD(J, n, p, d, start)
    print("\n\nEDD\n")
    print("Orden:" , Order, "\n Tiempo de inicio:", S, "\n Tiempo de finalización:", C, "\n Tiempo de latencia:", L, "\n Tiempo de tardanza:", T, "\n Tiempo de anticipación:", E, "\n Tardanza media:", meanTardiness, "\n Anticipación media:", meanEarliness, "\n Latencia media:", meanLateness)
    t = 13*60
    S, C, L, T, E, Order, meanTardiness, meanEarliness, meanLateness = CR(J, n, p, d, start, t)
    print("\n\nCR\n")
    print("t: ",t ,"\n Orden:" , Order, "\n Tiempo de inicio:", S, "\n Tiempo de finalización:", C, "\n Tiempo de latencia:", L, "\n Tiempo de tardanza:", T, "\n Tiempo de anticipación:", E, "\n Tardanza media:", meanTardiness, "\n Anticipación media:", meanEarliness, "\n Latencia media:", meanLateness)
    t = 13*60+20
    S, C, L, T, E, Order, meanTardiness, meanEarliness, meanLateness = CR(J, n, p, d, start, t)
    print("\n\nCR\n")
    print("t: ",t ,"\n Orden:" , Order, "\n Tiempo de inicio:", S, "\n Tiempo de finalización:", C, "\n Tiempo de latencia:", L, "\n Tiempo de tardanza:", T, "\n Tiempo de anticipación:", E, "\n Tardanza media:", meanTardiness, "\n Anticipación media:", meanEarliness, "\n Latencia media:", meanLateness)
    t = 13*60+25
    S, C, L, T, E, Order, meanTardiness, meanEarliness, meanLateness = CR(J, n, p, d, start, t)
    print("\n\nCR\n")
    print("t: ",t ,"\n Orden:" , Order, "\n Tiempo de inicio:", S, "\n Tiempo de finalización:", C, "\n Tiempo de latencia:", L, "\n Tiempo de tardanza:", T, "\n Tiempo de anticipación:", E, "\n Tardanza media:", meanTardiness, "\n Anticipación media:", meanEarliness, "\n Latencia media:", meanLateness)
    t = 13*60
    S, C, L, T, E, Order, meanTardiness, meanEarliness, meanLateness = MinimumSlack(J, n, p, d, start, t)
    print("\n\nMinimumSlack\n")
    print("t: ",t ,"\n Orden:" , Order, "\n Tiempo de inicio:", S, "\n Tiempo de finalización:", C, "\n Tiempo de latencia:", L, "\n Tiempo de tardanza:", T, "\n Tiempo de anticipación:", E, "\n Tardanza media:", meanTardiness, "\n Anticipación media:", meanEarliness, "\n Latencia media:", meanLateness)
    t = 13*60+20
    S, C, L, T, E, Order, meanTardiness, meanEarliness, meanLateness = MinimumSlack(J, n, p, d, start, t)
    print("\n\nMinimumSlack\n")
    print("t: ",t ,"\n Orden:" , Order, "\n Tiempo de inicio:", S, "\n Tiempo de finalización:", C, "\n Tiempo de latencia:", L, "\n Tiempo de tardanza:", T, "\n Tiempo de anticipación:", E, "\n Tardanza media:", meanTardiness, "\n Anticipación media:", meanEarliness, "\n Latencia media:", meanLateness)
    t = 13*60+25
    S, C, L, T, E, Order, meanTardiness, meanEarliness, meanLateness = MinimumSlack(J, n, p, d, start, t)
    print("\n\nMinimumSlack\n")
    print("t: ",t ,"\n Orden:" , Order, "\n Tiempo de inicio:", S, "\n Tiempo de finalización:", C, "\n Tiempo de latencia:", L, "\n Tiempo de tardanza:", T, "\n Tiempo de anticipación:", E, "\n Tardanza media:", meanTardiness, "\n Anticipación media:", meanEarliness, "\n Latencia media:", meanLateness)
    t = 13*60
    S, C, L, T, E, Order, meanTardiness, meanEarliness, meanLateness = ATC(J, n, p, d, start, t, 2)
    print("\n\nATC\n")
    print("t: ",t ,"\n Orden:" , Order, "\n Tiempo de inicio:", S, "\n Tiempo de finalización:", C, "\n Tiempo de latencia:", L, "\n Tiempo de tardanza:", T, "\n Tiempo de anticipación:", E, "\n Tardanza media:", meanTardiness, "\n Anticipación media:", meanEarliness, "\n Latencia media:", meanLateness)
