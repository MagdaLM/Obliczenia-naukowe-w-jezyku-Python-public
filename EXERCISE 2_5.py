S="Ala ma kota, a kot ma Alę i żyć bez siebie nie mogą wcale, ciągle figlują, bez przerwy psocą i wczesnym rankiem i późną nocą. Skarżą się wszyscy Ali sąsiedzi. Jakby huragan ten dom nawiedził. Przestań już Alu figlować z kotem, żeby był spokój w domu z powrotem. Tego hałasu nikt nie wytrzyma. Skarży się cała Ali rodzina, lecz Ala dalej z kotem psoci, jak to w zwyczaju bywa kocim. Raz Ala na kocie, raz kot na Ali. Przestańcie tak szaleć, bo dom się zawali. Jak można zatrzymać tych dwoje kamratów? Wysłać ich do ZOO lub do rezerwatu? Raz kot za Alą, raz Ala za kotem, biegną jak szaleni w tamtą i z powrotem. Lecz gdy noc na niebie gwiazdki pozapala, wnet zasną zmęczeni : kot i mała Ala, bo zwykła zabawa to ciężka robota, kiedy kot ma Alę, a Ala ma kota."

#(1)

count = 0
for c in S:
     if not c.isspace():
         count += 1
 
         
print("Original sentence: ", S)
print("Number of black characters: ", count)

#(2)

words=S.split()
count_word = len(words)
print("Number of words: ", count_word)

#(3)

longest_word = len(max(words, key=len))
result = [textword for textword in words if len(textword) == longest_word]
print("The longest word: ", result)

#(5.1)

print("Sort words according to the lexicographic:")
def sort_lexo(S):
     words.sort()
     for i in words:
          print (i)
if __name__ == '__main__':

     sort_lexo(S)

#(5.2)

print("Sort words according to the length:")
sort_length = sorted(words, key=len)

print(sort_length)
