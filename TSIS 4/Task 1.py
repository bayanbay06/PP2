with open('data.txt') as f:
    lines = f.readlines()
count, cnt = 0, 0
result_from_txt, result, result_of_item = dict(), dict(), dict()
for line in lines:
    count += 1
    result_from_txt[count] = line.replace('\n', '')

result["name of company"] = result_from_txt.get(2)
result["bin"] = result_from_txt.get(3)[4:]
result['address'] = result_from_txt.get(141)
result['total_price'] = result_from_txt.get(135)
result['date'] = result_from_txt.get(140)[7:]


for item in range(13, 131 + 1, 6):
    result_of_item = dict()
    result_of_item["name of product"] = result_from_txt[item]
    result_of_item["count"] = result_from_txt[item + 1][0]
    result_of_item["price"] = result_from_txt[item + 2]
    result_of_item["total_price"] = result_from_txt[item + 4]
    cnt += 1
    result[cnt] = result_of_item

for k, v in result.items():
    print(k, v)



