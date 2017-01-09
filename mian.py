kryptos = 'KRYPTOSABCDEFGHIJLMNQUVWXZ'
clue1 = 'EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD'
clue2 = 'VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKK?DQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVH?DWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGEWJLLAETG'
clue3 = 'SLOWLYDESPARATLYSLOWLYTHEREMAINSOFPASSAGEDEBRISTHATENCUMBEREDTHELOWERPARTOFTHEDOORWAYWASREMOVEDWITHTREMBLINGHANDSIMADEATINYBREACHINTHEUPPERLEFTHANDCORNERANDTHENWIDENINGTHEHOLEALITTLEIINSERTEDTHECANDLEANDPEEREDINTHEHOTAIRESCAPINGFROMTHECHAMBERCAUSEDTHEFLAMETOFLICKERBUTPRESENTLYDETAILSOFTHEROOMWITHINEMERGEDFROMTHEMISTXCANYOUSEEANYTHINGQ?'
clue4 = 'OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR'

sym2 = []
for i in range(0, len(clue2)):
    if clue2[i] in kryptos:
        continue
    else:
        sym2.append(i)
clue2 = clue2.replace('?', '')
sym3 = []
for i in range(0, len(clue3)):
    if clue2[3] in kryptos:
        continue
    else:
        sym2.append(3)
clue3 = clue3.replace('?', '')

key1 = 'PALIMPSEST'
key2 = 'ABSCISSA'
key3 = ''

kryptos_trans1 = []
for i in range(0, len(key1)):
    kryptos_trans1.append(kryptos[kryptos.index(key1[i]):] + kryptos[:kryptos.index(key1[i])])
kryptos_trans2 = []
for i in range(0, len(key2)):
    kryptos_trans2.append(kryptos[kryptos.index(key2[i]):] + kryptos[:kryptos.index(key2[i])])
solution1 = []
solution2 = []
for i in range(0, len(clue1)):
    j = i % len(kryptos_trans1)
    solution1.append(kryptos[kryptos_trans1[j].index(clue1[i])])
solution1 = ''.join(solution1)
for i in range(0, len(clue2)):
    j = i % len(kryptos_trans2)
    if clue2[i] in kryptos:
        solution2.append(kryptos[kryptos_trans2[j].index(clue2[i])])
    else:
        solution2.append(clue2[i])
solution2 = ''.join(solution2)
for i in sym2:
    solution2 = solution2[:i] + '?' + solution2[i:]
print(solution1)
print(solution2)
