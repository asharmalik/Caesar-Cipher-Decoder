__author__ = 'Ashar Malik'

f = open('dictionary.txt', 'r')

dictionary = f.read().split("\n")

def ces_shift(str, index):  #Caesarian shift
    str = str.lower()
    char_list = []
    for char in str:
        if not char.isalpha():#ignore non-letters
            char_list.append(char)
            continue
        ascii = ord(char)+index
        if(ascii>122): #character wrapping
            ascii = ascii-25
        if(ascii<97): #for negative indices
            ascii = ascii+25
        char_list.append(chr(ascii))

    return "".join(char_list)

def amount_words(str):
    words = str.split(" ")
    count = 0

    for word in words:
        if dictionary.__contains__(word):
            count+=1

    return count

def decode_ces_shift(str): #tests all shift possibilities for one with most correctly spelled words
    best_index_guess = 0
    best_guess_amt_words = 0
    best_str_guess = ""

    for i in range(0, 25):#test all shift possibilities
        conv_str = ces_shift(str, -i)
        word_count = amount_words(conv_str)

        if(word_count>best_guess_amt_words):#is the new shift guess better than the other?
            best_guess_amt_words = word_count
            best_index_guess = i
            best_str_guess = conv_str

    return best_str_guess

org_str = "This is a sample string to illustrate an example."
shift_by = 20
coded_string = ces_shift(org_str, shift_by)

print "Original: '%s'\nEncoded (N=%d): '%s'\nDecoding..." % (org_str, shift_by, coded_string)

print decode_ces_shift(coded_string)
