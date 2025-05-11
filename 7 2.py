sp = [1, 2, 10, 1, 11, 3, 7, 8, 9, 5]
povt = set()
dub = []
for item in sp:
    if item in povt:
        dub.append(item)
    else:
        povt.add(item)
if dub:
    print(f"Повторяющиеся элементы:, {dub}")
else:
    print("Повторяющихся элементов нет.")