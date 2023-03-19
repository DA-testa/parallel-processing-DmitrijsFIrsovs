# python3
import os

def parallel_processing(n, m, data):
    
    p = [(0,1) for i in range(n)]
    result = []
    
    for i in range(m):
        t = data[i]
        ft, d = p[0]
        result.append((d, ft))
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
                
    with open(os.environ['OUTPUT_PATH'], 'w') as f:
        for thread_id, start_time in result:
            f.write(f"{thread_id} {start_time}\n")
   
def main():
    n , m = map(int, input().split())
    data = list(map(int, input().split()))
    
    os.environ['OUTPUT_PATH'] = 'output.txt'
    
    
    parallel_processing(n, m, data)
    
 


if __name__ == "__main__":
    main()
