# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


def is_prime(num):
    is_prime = True
    divisor = num - 1

    while divisor > 1 and is_prime:
        if num % divisor == 0:
            is_prime = False

        divisor -= 1
    print(divisor)
    return is_prime

print(is_prime(75))