def LCS(X, Y):
    m = len(X)
    n = len(Y)
    
    # PHASE 1: Build the DP Table
    # Note: We use list comprehension to avoid Python's shallow-copy reference bug
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])
                
    # PHASE 2: Backtracking to find the string
    index = lcs_table[m][n]
    
    # Create an empty list of the correct size to hold our characters
    lcs_string = [""] * index 
    
    i = m
    j = n
    while i > 0 and j > 0:
        # If characters match, they are part of the LCS
        if X[i - 1] == Y[j - 1]:
            lcs_string[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        # If they don't match, trace back to the larger value
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    # Join the list into a clean string and return it
    return "".join(lcs_string)


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    
    print("\n--- Longest Common Subsequence ---")
    print(f"String 1: {X}")
    print(f"String 2: {Y}")
    print(f"Result:   {LCS(X, Y)}")