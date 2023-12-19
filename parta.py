#total combination
n = 6
dice_A = []
dice_B = []
print("Enter the dice value of the six faces")
for i in range(n):
    value=int(input())
    dice_A.append(value)
    dice_B.append(value)
print("Dice A",dice_A)
print("Dice B",dice_B)
total_combination = len(dice_B) * len(dice_A)
print("totalcombination", total_combination)

#distribution combination
distribution = [[0] * n for k in range(n)]
for i in range(len(dice_A)):
    for j in range(len(dice_B)):
        distribution[i][j] = dice_A[i] , dice_B[j]
print("Distribution Matrix")
for i in distribution:
    print(i)

#sum of each combination
sum_distribution = [[0] * n for k in range(n)]
for i in range(len(dice_A)):
    for j in range(len(dice_B)):
        sum_distribution[i][j] = dice_A[i] + dice_B[j]
print("sum distribution matrix")
for i in sum_distribution:
    print(i)

#probabability of possible sums
probability_sum=[0]*13
for i in range(len(dice_A)):
    for j in range(len(dice_B)):
        check=sum_distribution[i][j]
        if check >=2 and check<13:
            probability_sum[check]=probability_sum[check]+1
        check=0
k=0
for i in probability_sum:
    if i>0:
        print("probability of ",k ,"is",i)
    k=k+1


