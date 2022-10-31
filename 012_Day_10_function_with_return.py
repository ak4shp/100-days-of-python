
'''1. Convert full name into Title Case.'''

def format_name(f_name, l_name):
  if len(f_name) == 0 and len(l_name) == 0:
    return "You didn't type anything."
  
  f_name = f_name.lower()
  l_name = l_name.lower()
  f_letter = f_name[0].upper() + f_name[1:len(f_name)]
  l_letter = l_name[0].upper() + l_name[1:len(l_name)]
  # In-built -> title
  # f_letter = f_name.title()
  # l_letter = l_name.title()
  return f_letter + " " + l_letter

print(format_name(input("First name? "), input("Last name? ")))


'''2. Any string into title case.'''
def string_into_title(sentence):
    str_list = sentence.split(" ")
    title_sentence = ''
    for word in str_list:
        w = word[0]
        if not ((w >= 'a' and w<= 'z') or (w >= 'A' and w <= "Z")):
            return f"The word '{word}' contains non alphabatic char '{w}' in starting. Sentence can not be converted to titlecase."
        
        word = word.lower()
        title_word = word[0].upper() + word[1:len(word)] + " "
        title_sentence += title_word
    return title_sentence.strip()

sentence_str = "this sentence IS In 9NF6ormatEd Form BUt tHis Can Be lIkE tHiS."
print(string_into_title(sentence_str))
sentence_str2 = "this sentence IS In iNF6ormatEd Form BUt tHis Can Be lIkE tHiS."
print(string_into_title(sentence_str2))
sentence_str3 = "this sentence IS In iNFormatEd Form BUt tHis Can Be lIkE tHiS."
print(string_into_title(sentence_str3))
