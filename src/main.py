def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Compute the Levenshtein distance between two strings.

    Args:
        s1 (str): The first stringawdddddddd
        s2 (str): The second string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """
    m, n = len(s1), len(s2)

    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # Deletion
                    dp[i][j - 1],  # Insertion
                    dp[i - 1][j - 1],
                )  # Substitution

    return dp[m][n]


def main() -> None:
    "MAIN"
    print(levenshtein_distance(s1="kitten", s2="sitting"))


if __name__ == "__main__":
    main()
