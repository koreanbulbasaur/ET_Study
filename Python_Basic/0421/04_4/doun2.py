dna = input("염기 서열을 입력해주세요: ")
dna_dict = {}

for n, i in enumerate(dna):
    if i not in dna_dict:
        dna_dict[i] = 0
    dna_dict[i] += 1
    
for value in dna_dict:
    print(f"{value}의 개수 : {dna_dict[value]}")