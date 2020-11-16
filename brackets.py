p = { 'a' : '(', 'A' : ')', 
      'b' : '[', 'B' : ']', 
      'c' : '{', 'C' : '}' }

def get_key(val): 
    for key, value in p.items(): 
        if val == value: 
            return key 

string = '{3+4*5}{3+[2*(()1+2)-1]-7} + []{3*(2*x-1)+4}'
string = '{}}}'


bracket_clear = ''
bracket_index = ''

for elem in string:
    if elem in p.values():
        bracket_clear += elem
        bracket_index += get_key(elem)

L = 2

if len(bracket_index) % 2 == 0:
    
    while True: 

        bigPart = bracket_index[:L]
        print(bigPart,' - ', L, ' - ', bracket_index)
        
        l = int( L/2 )
        firstHalf = bracket_index[:l]
        firstHalf = firstHalf[::-1].swapcase()

        secondHalf = bigPart[l:L]
        
        if firstHalf == secondHalf:
 
            bracket_index = list(bracket_index)
            bracket_index[:L] = ''
            bracket_index = "".join(bracket_index)

            L = 2

        else:
            L += 2


        if len(bracket_index) < L:
            break


if len(bracket_index):
    print('something is wrong')
else:
    print('all is ok')