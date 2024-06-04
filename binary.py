def generate_binary_numbers(n):
    if n == 0:
        print(0)
        return
    for i in range(1, n + 1):
        print(bin(i)[2:])

# Example usage:
n=int(input())
generate_binary_numbers(n)
