from math import exp
class SingleMachine:
    def __init__(self, n, p, d, start=0):
        #n: number of jobs
        #M: number of machines
        #J: number of jobs
        #p: processing time
        #d: due date
        #start: start time
        self.n = n
        self.J = list(range(n))
        self.p = p
        self.d = d
        self.start = start
    def process(self):
        #S: start time for job j
        #C: completion time for job j
        #L: lateness for job j
        #T: tardiness for job j
        #E: earliness for job j
        self.S = [0]*self.n
        self.C = [0]*self.n
        self.L = [0]*self.n
        self.T = [0]*self.n
        self.E = [0]*self.n
        self.C[-1] = self.start
        for j in range(self.n):
            self.S[j] = max(self.start, self.C[j-1])
            self.C[j] = self.S[j] + self.p[j]
            self.L[j] = self.C[j] - self.d[j]
            self.T[j] = max(0, self.L[j])
            self.E[j] = max(0, -self.L[j])
    def FCFS(self):
        self.J = sorted(self.J)
        self.process()
        return self.J
    def SPT(self):
        self.J = [self.J for _, self.J in sorted(zip(self.p, self.J))]
        self.d = [self.d for _, self.d in sorted(zip(self.p, self.d))]
        self.p = sorted(self.p)
        self.process()
        return self.J
    def EDD(self):
        self.J = [self.J for _, self.J in sorted(zip(self.d, self.J))]
        self.p = [self.p for _, self.p in sorted(zip(self.d, self.p))]
        self.d = sorted(self.d)
        self.process()
        return self.J
    def LPT(self):
        self.J = [self.J for _, self.J in sorted(zip(self.p, self.J), reverse=True)]
        self.d = [self.d for _, self.d in sorted(zip(self.p, self.d), reverse=True)]
        self.p = sorted(self.p, reverse=True)
        self.process()
        return self.J
    def CR(self, check_time=False):
        if check_time == False:
            SyntaxError("check_time is not defined, Start time is used instead")
            check_time = self.start
        t = check_time
        CR = [0]*self.n
        for j in self.J:
            CR[j] = (self.d[j]-t)/self.p[j]
        self.J = [self.J for _, self.J in sorted(zip(CR, self.J))]
        self.p = [self.p for _, self.p in sorted(zip(CR, self.p))]
        self.d = [self.d for _, self.d in sorted(zip(CR, self.d))]
        self.process()
        return self.J
    CriticalRatio = CR
    def MinimumSlack(self, check_time=False):
        if check_time == False:
            SyntaxError("check_time is not defined, Start time is used instead")
            check_time = self.start
        t = check_time
        MS = [0]*self.n
        for j in self.J:
            MS[j] = max(0,self.d[j]-t-self.p[j])
        self.J = [self.J for _, self.J in sorted(zip(MS, self.J))]
        self.p = [self.p for _, self.p in sorted(zip(MS, self.p))]
        self.d = [self.d for _, self.d in sorted(zip(MS, self.d))]
        self.process()
        return self.J
    MinSlack = MinimumSlack
    def MaximumSlack(self, check_time=False):
        if check_time == False:
            SyntaxError("check_time is not defined, Start time is used instead")
            check_time = self.start
        t = check_time
        MS = [0]*self.n
        for j in self.J:
            MS[j] = max(0,self.d[j]-t-self.p[j])
        self.J = [self.J for _, self.J in sorted(zip(MS, self.J), reverse=True)]
        self.p = [self.p for _, self.p in sorted(zip(MS, self.p), reverse=True)]
        self.d = [self.d for _, self.d in sorted(zip(MS, self.d), reverse=True)]
        self.process()
        return self.J
    MaxSlack = MaximumSlack
    def ATC(self, check_time=False, K =False):
        if check_time == False:
            SyntaxError("check_time is not defined, Start time is used instead")
            check_time = self.start
        if K == False:
            SyntaxError("K is not defined, K = 1 is used instead")
            K = 1
        t = check_time
        ATC = [0]*self.n
        P = sum(self.p)/self.n
        for j in self.J:
            ATC[j] = (1/self.n)/(self.p[j])*exp(-max(self.d[j]-t-self.p[j], 0)/(K*P))
        self.J = [self.J for _, self.J in sorted(zip(ATC, self.J), reverse=True)]
        self.p = [self.p for _, self.p in sorted(zip(ATC, self.p), reverse=True)]
        self.d = [self.d for _, self.d in sorted(zip(ATC, self.d), reverse=True)]
        self.process()
        return self.J
    def CommonDueDate(self):
        if len(set(self.d)) != 1:
            SyntaxError("Not All jobs have the same due date")
        #Step 0: Rank the jobs in SPT order
        self.SPT()
        #Step 1: Create two sets A and B
        A = []
        B = []
        #Step 2: Compute Cmax = \sum_{j=1}^{n} p_j, i = n, R = Cmax-d
        n = self.n
        Cmax = sum(self.p)
        i = n
        R = Cmax - self.d[0]
        L = self.d[0]
        #Step 3: If R > L, then add job i to set A and go to step 4
        while i > 0:
            if R >= L:
                A.append(i)
                i -= 1
                R = R-self.p[i]
            else:
                B.append(i)
                i -= 1
                L = L-self.p[i] 
        Order = B + list(reversed(A))
        Lab = [0]*n
        for j in range(n):
            Lab[j] = self.J[Order[j]-1]
        self.J = Lab
        return self.J
    
n = 7
d = [21]*n
p = [8, 14, 18, 2, 3, 7, 24]
SM = SingleMachine(n=n, d=d, p=p)
print(SM.CommonDueDate())