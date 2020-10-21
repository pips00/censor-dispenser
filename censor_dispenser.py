# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#Censor Words

first_censor = "learning algorithms"

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]

negative_words = ["helena","concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]


# Handler function - Corrects for punctuation,upper and lowercase.

def words_handler(lst):
  new_lst=[]
  for word in lst:
    new_lst.append(word)
    new_lst.append(word.upper())
    new_lst.append(word.lower())
    new_lst.append(word.title())
    new_lst.append(word + ".")
    new_lst.append(word + ",")
    new_lst.append(word + "!")
    new_lst.append(word + "'s")
    new_lst.append("(" + word)
    new_lst.append(word + ")")
  return new_lst

proprietary_terms_handle = words_handler(proprietary_terms)

negative_words_handle = words_handler(negative_words)

all_words_handle = proprietary_terms_handle + negative_words_handle


# 1 - Censor one word

def censor_single_word(text, word):
  result = text.replace(word, "****")
  return print(result)

# 2 - Censor Proprietary Words

def censor_multiple_words(text):

  split_text= []

  split_text_paragraphs = text.split("\n")

  for paragraph in split_text_paragraphs:
    split_text.append(paragraph.split())
    continue
    return split_text

  new_text = []

  for i in range(len(split_text)):
    if split_text[i] == []:
      new_text.append("\n\n")
    else:
      for word in split_text[i]:
        if word not in proprietary_terms_handle:
          new_text.append(word)
        else:
          new_text.append("****")

  return " ".join(new_text)


# 3 - Censor Proprietary and Negative Words

def censor_negative_words(text):

  clean_text = censor_multiple_words(text)

  split_text = []

  split_text_paragraphs = clean_text.split("\n")

  for paragraph in split_text_paragraphs:
    split_text.append(paragraph.split())
    continue
    return split_text

  new_text=[]

  for i in range(len(split_text)):
    if split_text[i] == []:
      new_text.append("\n\n")
    else:
      for word in split_text[i]:
        if word in negative_words_handle and text.count(word) >= 2:
          new_text.append("****")
        else:
          new_text.append(word)

  return " ".join(new_text)

# 4 - Censor Proprietary and Negative Words, as well as words before and after the censored words.

def censor_before_after(text):

  split_text = []

  split_text_paragraphs = text.split("\n")

  for paragraph in split_text_paragraphs:
    split_text.append(paragraph.split())
    continue
    return split_text

  new_text=[]

  for i in range(0,len(split_text)):
    if split_text[i] == []:
      new_text.append("\n\n")
    else:
      for word in split_text[i]:
        if word in all_words_handle:
          split_text[i] = "****"
          split_text[i-1] = "****"
          split_text[i+1] = "****"
          new_text.append(split_text[i-1])
          new_text.append(split_text[i])
          new_text.append(split_text[i+1])
        else:
          new_text.append(word)
  return " ".join(new_text)

#Test functions
print("\n\nE-MAIL 1\n\n")
print(censor_single_word(email_one, first_censor))
print("\n\nE-MAIL 2\n\n")
print(censor_multiple_words(email_two))
print("\n\nE-MAIL 3\n\n")
print(censor_negative_words(email_three))
print("\n\nE-MAIL 4\n\n")
print(censor_before_after(email_four))
