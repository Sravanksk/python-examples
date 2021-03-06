# Jon Snow visits Dragonstone to meet Daenerys Targaryen. He asks for aid in defeating the White Walkers and Army of
# Dead. But Daenerys refuses to believe that white walkers are real. She puts a condition before Jon that if he
# solves the challenge given by her then she will send her army to fight White Walkers. She gives certain inputs and
# outputs , Jon needs to find the logic and predict the output for the corresponding inputs. Jon Snow is struggling
# with the challenge as he knows nothing!! Help Jon to find the logic and win this challenge.


# INPUT : Input contains integers separated by a newline

# OUTPUT : For the given input , Output the required answer.

# NOTE : No. of input integers are unknown.

# CONSTRAINTS :

# 0<= N (total inputs)<= 10^15

#   SAMPLE INPUT          SAMPLE OUTPUT
#   0                     0
#   1                     1
#   5                     1
#   12                    4
#   22                    2
#   1424                  16


while True:
    try:
        n = int(input())
        zeroes = 0
        if n == 0:
            print(0)
        else:
            for i in range(len(bin(n)) - 1, -1, -1):
                if bin(n)[i] == '1':
                    print(int('1' + ('0' * zeroes), 2))
                    break
                else:
                    zeroes += 1
                    continue
    except:
        break
