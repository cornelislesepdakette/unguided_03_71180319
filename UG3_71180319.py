
from collections import Counter

def hitungKata(kata, kalimat):
   li = kalimat.split(' ')
   katas = Counter(li).most_common()
   d = {}
   for w in katas:
      d[w[0]] = w[1]
   try:
      print("%s : %d" % (kata, d[kata]))
   except KeyError as d:
      print("%s : 0" % kata)

def main():
   kalimat = input("Masukkan kalimat: ")

   kata = input("Masukkan kata yang dicari: ")

   # mencari jumlah kata
   hitungKata(kata, kalimat)

if __name__ == "__main__":
   main()