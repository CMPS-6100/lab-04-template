# CMPS 6100 Lab 04
## Answers

**Name:**_________________________


Place all written answers from `lab-04.md` here.

## Asymptotic Analysis Problems (1 pt ea.)

1. $T(n) = 3T(n/2) + n$



2. $T(n) = 2T(n/3) + 1$



3. $T(n) = 4T(n/16) + n^{1/4}$



4. $T(n) = T(n-1) + n$



5. $T(n) = 3T(n/3) + n$



6. $T(n) = 2T(n/2) + n^2$



7. $T(n) = 4T(n/2) + n^2$



8. $T(n) = 8T(n/2) + n^2$



## Coding Problems Analysis

### Unimodal Max (2 pts)

12. Prove that your **Unimodal Max** algorithm runs in $O(\lg n)$ work by deriving the recurrence for your algorithm and solving it.

## Sorting Analysis

14.  Use `print_results` to print a table of selection sort and merge sort's runtimes for each of the sizes: 

    `[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]`

15. Add plots for the runtimes of Selection Sort and Merge Sort for each of the following lists of sizes:

    1. `[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`

    2. `[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]`

    3. `[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]`

16. Do your results match your expectations? That is, are the trends that you see between the Selection Sort and Merge Sort's runtimes what you expected? Why or why not?

17. How long does it take your computer to sort lists of sizes `[1000, 10000, 100000]` using Selection Sort and Merge Sort? Based on this, how long would you expect Selection Sort to take to sort a list of size 1,000,000? Express this in minutes, hours, or days, which ever is the appropriate scale. How long does it take Merge Sort to sort a list of 1,000,000?