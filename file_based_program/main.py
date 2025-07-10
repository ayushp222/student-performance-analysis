# main.py

def sum_of_two(a, b):
    return a + b

def is_even(n):
    return "Even" if n % 2 == 0 else "Odd"

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(d) ** power for d in num_str)
    return total == n

def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def decrypt(encrypted_message, shift):
    return encrypt(encrypted_message, -shift)

def main():
    print("Program started...")

    try:
        with open("input.txt", "r") as infile:
            lines = infile.read().splitlines()

        results = []

        # Reading inputs from input.txt
        a, b = map(int, lines[0].split())
        results.append(f"Sum: {sum_of_two(a, b)}")

        n = int(lines[1])
        results.append(f"Odd or Even: {is_even(n)}")

        n = int(lines[2])
        results.append(f"Factorial: {factorial(n)}")

        n = int(lines[3])
        results.append(f"Fibonacci: {fibonacci(n)}")

        s = lines[4]
        results.append(f"Reversed String: {reverse_string(s)}")

        s = lines[5]
        results.append(f"Is Palindrome: {is_palindrome(s)}")

        year = int(lines[6])
        results.append(f"Is Leap Year: {is_leap_year(year)}")

        n = int(lines[7])
        results.append(f"Is Armstrong: {is_armstrong(n)}")

        shift = int(lines[8])
        message = lines[9]
        encrypted = encrypt(message, shift)
        decrypted = decrypt(encrypted, shift)
        results.append(f"Encrypted: {encrypted}")
        results.append(f"Decrypted: {decrypted}")

        # Writing output to output.txt
        with open("output.txt", "w") as outfile:
            for line in results:
                outfile.write(line + "\n")

        print("Program completed. ✅ Check output.txt")

    except Exception as e:
        print("❌ Error occurred:", e)

if __name__ == "__main__":
    main()
