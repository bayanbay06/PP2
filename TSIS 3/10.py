synonyms = dict()
def main():
  item_number = int(input())
  for _ in range(item_number):
    words = input().split()
    synonyms[words[0]] = words[1]
  sought_word = input()
  for k, v in synonyms.items():
    if k == sought_word:
      print(v)
      break
    elif v == sought_word:
      print(k)
      break


if __name__ == '__main__':
  main()


