def pwvalidate(lines):
    valid_passwords = 0
    for line in lines:
      policy, password = line.split(':')
      min_rep, max_rep = policy.split(' ')[0].split('-')
      char = policy.split(' ')[1]
      if password[int(min_rep)] == char and password[int(max_rep)] == char:
          continue
      if password[int(min_rep)] == char:
        valid_passwords = valid_passwords + 1
      if password[int(max_rep)] == char:
        valid_passwords = valid_passwords + 1
    return valid_passwords


if __name__ == "__main__":
  lines  = [line.strip() for line in open('input', 'r').readlines()]
  print(pwvalidate(lines))
