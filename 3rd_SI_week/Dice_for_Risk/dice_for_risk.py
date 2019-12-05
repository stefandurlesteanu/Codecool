import random


while True:
    try:
        attackers_num = int(input("How many units will attack?: "))
        assert 0 < attackers_num < 4
        defenders_num = int(input("How many defending units?: "))
        assert 0 < defenders_num < 3
    except ValueError:
        print("Not an integer! Please enter an integer.")
    except AssertionError:
        print("Please enter an integer between 1 and 3")
    else:
        break
    

attacker = []
defender = []

for i in range (attackers_num):
    attacker.append(str(random.randint(1,6)))

for i in range (defenders_num):
    defender.append(str(random.randint(1,6)))


defender_loss = 0
attacker_loss = 0

if len(attacker) == 3:
    for i in range(len(attacker)-1):
        if attacker[i] >= defender[i]:
            defender_loss += 1
        else:
            attacker_loss += 1
else:
    for i in range(len(attacker)):
        if attacker[i] >= defender[i]:
            defender_loss += 1
        else:
            attacker_loss += 1


print ("Dice:\n  Attacker: {adice}\n  Defender: {bdice}\n".format(adice = '-'.join(attacker), bdice = '-'.join(defender)))
print ("Outcome:\n  Attacker: Lost {nr_atack_units} unit\n  Defender: Lost {nr_def_units} unit"
.format(nr_atack_units=attacker_loss, nr_def_units=defender_loss))