def calc_x(V, M, a, t): 
  x = [1] * (V+1)
  
  for n in range (1, V+1):
    sum = 0;
    for i in range (0, M):
      if n >= t[i]:
        sum += a[i] * t[i] * x[n - t[i]]

    x[n] = sum/n;
  return x

#-----------------------#
def calc_P0(x):
  sum = 0

  #1/item divides by 0
  for item in x:
    sum += item

  return 1/sum

#-----------------------#
def calc_P(V, M, a, t, x):
  P = [1] * (V+1)
  P[0] = calc_P0(x)

  for n in range (1, V+1):
    sum = 0
    for i in range (0, M):
      if n >= t[i]:
        sum += a[i] * t[i] * P[n - t[i]]
    
    P[n] = sum/n;
  
  return P

#-----------------------#
def calc_b(V, t, P, i=1):
  # b = [1] * [V+1]
  sum = 0
  for n in range (V - t[i-1] + 1, V+1):
    sum += P[n]

  return sum

#-----------------------#
M = 2   #strumienie ruchu
V = 3   #pojemnosc wiazki w kanalach lub podstawowych jedn. pasma
t = [[1, 2]]    #liczba zadanych jednostek przetwarzania
a = [[0.4, 3]]  #ruch oferowany

print("M = ", M)
print("V = ", V)
print("\n")

for itA in a:
  for itT in t:
    print("---" * 10)
    print("a_i = ", itA)
    print("t_i = ", itT)

    x = calc_x(V, M, itA, itT)
    P0 = calc_P0(x)
    P = calc_P(V, M, itA, itT, x)

    b = [1] * M

    for i in range (0, M):
      b[i] = calc_b(V, itT, P, i)

    #print("x = {} \n P = {}".format(x, P))
    for i in range (0, V+1):
      print("x[{}] = {}".format(str(i), x[i]))
      print("P[{}] = {}\n".format(str(i), P[i]))


    i = 0
    for i in range (0, M):
      print("b[{}] = {}".format(str(i+1), b[i]))

