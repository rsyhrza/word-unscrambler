character_lists = []

log = open("unscramble.log", "w")

def log_right(word):
    global character_lists
    word_len = len(word) + 1
    for j in range(word_len):
        for i in range(j, word_len):
            if len(word[j:i]) > 2:
                print(word[j:i])
                log.write("{}\n".format(word[j:i]))
                character_lists.append(word[j:i].lower())

def log_chars(word_list):
    # left right & right left
    for word in word_list:
        log_right(word)

        word_reversed = word[::-1]
        log_right(word_reversed)

    # top bottom & bottom top
    for i in range(0, len(word_list[0])):
        word_start = ""
        for j in range(0, len(word_list)):
            word_start = word_start + word_list[j][i]

        #print(word_start)
        log_right(word_start)

        word_reversed = word_start[::-1]
        log_right(word_reversed)

    # diagonal
    
    word_list_len = len(word_list[0])
    for i in range(word_list_len):
         diagonal_start = ""
         for j in range(len(word_list) - i):
              diagonal_start = diagonal_start + word_list[j+i][j]
        
         log_right(diagonal_start)
         diagonal_reversed = diagonal_start[::-1]
         log_right(diagonal_reversed)

         diagonal_start = ""
         for j in range(i, len(word_list) - i):
              diagonal_start = diagonal_start + word_list[j-i][j]
        
         log_right(diagonal_start)
         diagonal_reversed = diagonal_start[::-1]
         log_right(diagonal_reversed)

def main(word_list):    
    log_chars(word_list)
    log.close()

    file_kamus = open("words.txt", "r")
    kamus = file_kamus.read()
    file_kamus.close()

    list_kamus_raw = kamus.splitlines()
    list_kamus = []
    for kata in list_kamus_raw:
        if len(kata) > 2:
            list_kamus.append(kata.lower())

    valid = open("valid-unscrambled.log", "w")
    for char in character_lists:
        if char in list_kamus:
            print(char)
            valid.write("{}\n".format(char))
    valid.close()

    print("Program has finished executing.")

file_words = open("text_to_find.txt", "r")
words = file_words.read()
file_words.close()

main(words.splitlines())