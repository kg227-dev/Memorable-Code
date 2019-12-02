import numpy as np

first_p = np.random.normal(20, 15 ,13)
second_p = np.random.normal(70, 15,12)

P = np.concatenate((first_p, second_p), axis=None)
P[P < 0] = 0
P[P >100] = 100
P_round = np.round(P)
P_round.sort()


count = 0
condition = True

while condition is True:
   if (count == 100):
       break
   for i in P_round:
        if (i <= count):
            count = count+4
            P_round = np.delete(P_round, np.where(P_round == i))
        else:
            condition = False
            break
if (count <= 50):
    print("Revolution failed.")
else:
    print("Successful Revolution.")
print("Percentage of Population who joined Revolution: " +str(count))