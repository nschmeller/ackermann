import sys

def ack_inner(m, n, ind):
  print((' ' * ind) + '({0}, {1})'.format(m, n))
  if m == 0 and n == 0:
    return 1
  elif m == 0:
    return n + 1
  elif n == 0:
    return ack_inner(m-1, 1, ind+1)
  else:
    return ack_inner(m-1, ack_inner(m, n-1, ind+1), ind+1)

def ack(m, n):
    if m < 0 or n < 0:
      raise ValueError('expected nonnegative inputs')
    return ack_inner(m, n, 0)

m = int(sys.argv[1])
n = int(sys.argv[2])

res = ack(m, n)

print()
print('ack({0}, {1}) = {2}'.format(m, n, res))
