# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    
    t = [(0 , i) for i in range(n)]
    heapq.heapify(t)
    
    for i in range(m):
        a , b = heapq.heappop(t)
        output.append((b , a))
        heapq.heappush(a, (a + data[i], b))
        
    return output    
    
   
   
def main():
    n , m = map(int, input().split())
    data = list(map(int, input().split()))
    
    assert 1 <= n <=10 **5
    assert 1 <= m <=10 **5
    assert len(data) == m
    assert all (0 <= ti<= 10 ** 9 for ti in data)
    
    
    
    
    result = parallel_processing(n, m, data)
    
    for b , ab in result:
        print(a , ab)
    
 


if __name__ == "__main__":
    main()
