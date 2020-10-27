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
    return ack_inner(m, n, 0)

ack(int(sys.argv[1]), int(sys.argv[2]))
