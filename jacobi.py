def jacobi(A, b):
    n = len(b)
    x = np.random.rand(n)
    k = np.random.rand(n)
    
    for _ in range(100):
        for i in range(n):
            sum_ = 0
            for j in range(n):   
                if i != j:
                    sum_ += A[i, j] * k[j]
            
            x[i] = (b[i] - sum_)/A[i, i]
        
        if np.linalg.norm(x-k)/np.linalg.norm(x) < 1e-9:
            break
        else:
            k = x.copy()
            
    return k