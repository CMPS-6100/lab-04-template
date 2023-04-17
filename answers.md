# CMPS 6100 Lab 04
## Answers

**Name:**_________________________


Place all written answers from `lab-04.md` here.

## Asymptotic Analysis Problems (1 pt ea.)

1. $T(n) = 3T(n/2) + n$



2. $T(n) = 2T(n/3) + 1$



3. $T(n) = 4T(n/16) + n^{1/4}$



4. $T(n) = T(n-1) + n$



5. $T(n) = T(\sqrt n) + 1$



6. $T(n) = 3T(n/3) + n$



7. $T(n) = 2T(n/2) + n^2$



8. $T(n) = 4T(n/2) + n^2$



9. $T(n) = 8T(n/2) + n^2$



10. $T(n) = T(n/2) + \lg n$



## The Master Method (5 pts)

11. The Master Method gives an easy formula for solving recurrences of the form: 
    $$T(n) = aT(n/b) + n^c$$

    Derive the asymptotic behavior of $T(n)$ by solving its general recursion tree for each of the three cases. This problem is graded on based on your work shown for your derivations, not on the final results. Show your recursion tree and derivations from it.

    1. $\log_b a < c$

    2. $\log_b a = c$

    3. $\log_b a > c$

## Coding Problems Analysis

### Unimodal Max (3 pts)

13. Prove that your **Unimodal Max** algorithm runs in $O(\lg n)$ work by deriving the recurrence for your algorithm and solving it.

### Recursive List Sum (3 pts)

15. What is the work and span of your **List Sum** algorithm? Derive the work and span recurrences for your algorithm and solve them.