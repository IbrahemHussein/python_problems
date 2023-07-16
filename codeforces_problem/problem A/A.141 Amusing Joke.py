def count_letter(x):
    count_letter = {}
    for i in x:
        if i not in count_letter.keys():
            count_letter[i] = x.count(i)
    return dict(sorted(count_letter.items()))


guest_name = input()
residence_name = input()
full_string = guest_name + residence_name
pile_letter = input()
if count_letter(full_string) == count_letter(pile_letter):
    print('YES')
else:
    print('NO')
