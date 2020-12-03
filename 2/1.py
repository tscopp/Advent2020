def pwvalidate(lines):
    valid_passwords = 0
    for line in lines:
      policy, password = line.split(':')
      min_rep, max_rep = policy.split(' ')[0].split('-')
      char = policy.split(' ')[1]
      if password.count(char) >= int(min_rep) and password.count(char) <= int(max_rep):
        valid_passwords = valid_passwords + 1
    return valid_passwords


if __name__ == "__main__":
  lines  = [line.strip() for line in open('input', 'r').readlines()]
  print(pwvalidate(lines))
