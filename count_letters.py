def Count_Letters(phrase):
        prev_char = phrase[0]
        counter = 0
        output = ""
        
        for i in range(len(phrase)):
                # print phrase[i]
                # print prev_char
                if(phrase[i] == prev_char):
                        counter += 1
                else:
                        output += str(counter) + prev_char
                        counter = 1
                
                prev_char = phrase[i]
        
        output += str(counter) + prev_char
        return output


print(Count_Letters("aabb"))
print(Count_Letters("abcd"))
print(Count_Letters("aaaabbcca"))
print(Count_Letters("aaaabbccc"))
print(Count_Letters("abbccddaaaabbccca"))