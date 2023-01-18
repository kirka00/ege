result_search = []
for x in '0123456789a':
    for y in '0123456789a':
        t = int(f'7{y}23{x}5', 25) + int(f'67{x}9{y}', 11)
        if t % 131 == 0:
            result_search.append(t)
if result_search:
    print(min(result_search) // 131)
