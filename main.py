# python3

def parallel_processing(n, m, data):
    
    p = [(0,1) for i in range(n)]
    output = []
    
    for i in range(m):
        t = data[i]
        ft, d = p[0]
        output.append((d, ft))
        p[0] = (ft + t,d)
        
        j=0
        while True:
            ch1 = 2*j +1
            ch2 = 2*j +2
            if ch1 >= n:
                break
            if ch2 >= n or p[ch1] <= p[ch2]:
                ch = ch1
            else:
                ch = ch2
            if p[ch] < p[j]:
                p[ch], p[j] = p[j], p[ch]
                j = ch
            else:
                break
    

    return output

def main():
    n , m = map(int, input().split())
    data = list(map(int, input().split()))
    
    output = parallel_processing(n, m , data)

    for d , st in output:
        print(d, st)
    




if __name__ == "__main__":
    main()
