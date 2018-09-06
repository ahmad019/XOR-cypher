

def xor(x,y): #function to cypher text
	g = []
	for i in range(len(x)):
		if x[i] == y[i]:
			g.append(0)
		elif x[i] != y[i]:
			g.append(1)
	return g

#x = [1,0,1,0,1,0,0,1] some key 
#y = [1,1,1,1,1,0,1,1]     values
cipher_string = []
asc_str = []
asc_list = [[]]
refined = ([[]])
cipher = []



cipher_input = input('Enter the string to cipher: ')
key_input = '101010101' #input('Enter 8bit key ex:10101101: ')

for ch in cipher_input:
    
    cipher_string.append(ch)

num_of_char = len(cipher_string)

for i in range(num_of_char):
    
    asc_str.append(('{0:08b}'.format(ord(cipher_string[i]))))


jr = 0
k = 0
for n in range(len(asc_str)):
    refined.append([])
    for object in asc_str[n]:
        if(jr==8):
            k += 1
            jr = 0
        refined[k].append(object)
        jr += 1
        #if(n == len(asc_str)-1):
         #   break
        
        
l = 0

for l in range(len(refined)):
    asc_list.append([])
    asc_list[l] = list(map(int, refined[l]))
    

key = list(map(int, key_input))

f=0

for f in range(len(asc_list)-2):
    
    cipher.append(xor(asc_list[f], key))


cipher_str = []
cipher_text = []


cipher_str = ["".join((map(str, (cipher[i])))) for i in range(len(cipher))]

for i in range(len(cipher_str)):
    cipher_text.append(chr(int(cipher_str[i],2)))
    

#decipher_1 = list(map(int, decipher))
cipher_text = ["".join(cipher_text)]

print(cipher)
print(cipher_str)
print(cipher_text)
