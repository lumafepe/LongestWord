n_palavras = int(input())
maior_palavra = ""
for i in range(n_palavras):
    palavra = input()
    if len(palavra) > len(maior_palavra):
      maior_palavra = palavra
print(maior_palavra)
