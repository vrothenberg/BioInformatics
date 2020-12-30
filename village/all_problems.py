#import this

# a = 825
# b = 971
# c = a ** 2 + b ** 2
# print(c)

# s = "EqmgZdJSUugpY6Pogona9MWqr1ARVmzZi4YhhXE4y3P6S47gpJupWOUoaustralisN3lJxncFPhhYJVsOilDa7Gg8DfPsGsdOdZRySFqGTY02QCXbnk2d065hB2A8gfljNskUivxLRv6mxfEskxCH9Aj7TSdFT7yVFW1TQ00dsn4VrHYUz5MqX2LGFczptn5dGRIlca."
# a = 14
# b = 19
# c = 56
# d = 64
# #       01234
# #test = "something"
# print(s[a:b+1])
# print(s[c:d+1])

# a = 4709 
# b = 8917
# sum = 0
# for i in range(a,b+1):
#     if i % 2 == 1: sum += i

# print(sum)

# f = open("Village//rosalind_ini5.txt", "r")
# w = open("Village//output.txt", "w")

# i = 1
# for line in f:
#     if i % 2 == 0:
#         w.write(line)
#     i+=1

# f.close()
# w.close()

s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

d = {}
for word in s.split(' '):
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

for key, val in d.items():
    print(key, val)