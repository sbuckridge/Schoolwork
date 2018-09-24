% A fibonacci program in prolog

fib(0, 1).
fib(1, 1).
fib(N, Result) :- 
    N > 1,
    N2 is N - 2, fib(N2, Result2),
    N1 is N - 1, fib(N1, Result1),
    Result is N1 + N2.
