def encontraJ(A,e,d,x):
    if A[e] == A[d]:
        print("Os ponteiros se encontraram")
        return d+1
    if A[d] == x:
        print("A[d] == x")
        return d
    else:
        meio = int((e + d) / 2)
        if A[meio] < x:
            d = d-1
            e = meio
            
        else:
            d = meio
        print(f"d: {d}")
        print(f"e: {e}")
        return encontraJ(A,e,d,x)

A = [1,3,5,7,9,10]
e = 0
d = len(A)-1
x = 8
resultado = encontraJ(A, e, d, x)
print("Resultado:", resultado)