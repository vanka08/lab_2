def is_prime_simple(n):
  """Проверяет, является ли число простым, простым перебором."""
  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

# Примеры
print(is_prime_simple(2)) # True
print(is_prime_simple(3)) # True
print(is_prime_simple(4)) # False
print(is_prime_simple(17)) # True
