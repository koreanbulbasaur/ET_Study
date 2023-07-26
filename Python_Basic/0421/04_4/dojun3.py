lst = input("염기 서열을 입력해주세요: ")
word_3 = None
kodon_list = []
kodon_dict = {}
kodon_group = []

for n, i in enumerate(lst):
    kodon_list.append(i)
    if len(kodon_list) == 3:
        word_3 = "".join(kodon_list)
        kodon_group.append(word_3)
        kodon_list = []
        
for n, i in enumerate(kodon_group):
    if i not in kodon_dict:
        kodon_dict[i] = 0
    kodon_dict[i] += 1
        
print(kodon_dict)