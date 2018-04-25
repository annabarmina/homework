def is_palindrome(s):
  s = str(s).lower().replace(' ', '')
  return s == s[::-1]
