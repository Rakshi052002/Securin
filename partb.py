n=6
old_dice_A=[]
old_dice_B=[]
print("Enter the dice value of the six values")
for i in range(n):
    value=int(input())
    old_dice_A.append(value)
    old_dice_B.append(value)
print("Dice A",old_dice_A)
print("Dice B",old_dice_B)
new_dice_A=[0]*(n)
new_dice_B=[0]*(n)
val=0
for i in range(n):
    if old_dice_A[i] > 4:
        new_dice_A[i]=4
        val=(old_dice_A[i])-(4)
        new_dice_B[i]=old_dice_B[i]+val
    else:
        new_dice_A[i]=old_dice_A[i]
        new_dice_B[i]=old_dice_B[i]
    val=0
print("updated dice A")
print(new_dice_A)
print("updated dice B")
print(new_dice_B)

#to check probability of old dice and new dice remains the same
new_sum_distribution = [[0] * n for k in range(n)]
for i in range(len(new_dice_A)):
    for j in range(len(new_dice_B)):
        new_sum_distribution[i][j] = new_dice_A[i] + new_dice_B[j]
print("sum distribution matrix")
for i in new_sum_distribution:
    print(i)

#probabability of possible sums
probability_sum=[0]*13
for i in range(len(new_dice_A)):
    for j in range(len(new_dice_B)):
        check=new_sum_distribution[i][j]
        if check >=2 and check<13:
            probability_sum[check]=probability_sum[check]+1
        check=0
k=0
for i in probability_sum:
    if i>0:
        print("probability of ",k ,"is",i)
    k=k+1