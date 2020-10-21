# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#Censor Words

first_censor = "learning algorithms"

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]

proprietary_terms_title = [term.title() for term in proprietary_terms] + [term.title() + "!" for term in proprietary_terms] + [term.title() + "." for term in proprietary_terms] + [term.title() + "," for term in proprietary_terms]

proprietary_terms_upper = [term.upper() for term in proprietary_terms] + [term.upper() + "!" for term in proprietary_terms] + [term.upper() + "." for term in proprietary_terms] + [term.upper() + "," for term in proprietary_terms]

proprietary_terms_handle = proprietary_terms + proprietary_terms_title + proprietary_terms_upper

negative_words = ["helena","concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

negative_words_title = [negative.title() for negative in negative_words] + [negative.title() + "." for negative in negative_words] + [negative.title() + "!" for negative in negative_words] + [negative.title() + "," for negative in negative_words]

negative_words_upper = [negative.upper() for negative in negative_words] + [negative.upper() + "." for negative in negative_words] + [negative.upper() + "!" for negative in negative_words] + [negative.upper() + "," for negative in negative_words]

negative_words_handle = negative_words + negative_words_title + negative_words_upper

all_words_handle = proprietary_terms_handle + negative_words_handle


# 1 - Learning Algorithms - E-mail 1

def censor_single_word(text, word):
  result = text.replace(word, " ")
  return print(result)

# 2 - Proprietary words - E-mail 2

def censor_multiple_words(text):

  split_text = text.split()

  for i in range(len(split_text)):
    for h in range(len(proprietary_terms_handle)):
      if split_text[i] == proprietary_terms_handle[h]:
        text = text.replace(split_text[i], " ")
  return text


# 3 - Negative words & Proprietary words - E-mail 3

def censor_negative_words(text):
  clean_text = censor_multiple_words(text)
  split_text = clean_text.split()

  for i in range(len(split_text)):
    for j in range(len(negative_words_handle)):
      if split_text[i] == negative_words_handle[j] and text.count(split_text[i]) >= 2:
        text = text.replace(split_text[i], " ")
  return text

# 4 - Negative words & Proprietary words & Before and After - Email 4

def censor_before_after(text):

  split_text = text.split()

  for i in range(len(split_text)):
    for h in range(len(proprietary_terms_handle)):
      if split_text[i] == proprietary_terms_handle[h]:
        text = text.replace(split_text[i], " ")
        text = text.replace(split_text[i-1], " ")
        text = text.replace(split_text[i+1], " ")

  for i in range(len(split_text)):
    for j in range(len(negative_words_handle)):
      if split_text[i] == negative_words_handle[j]:
        text = text.replace(split_text[i], " ")
        text = text.replace(split_text[i-1], " ")
        text = text.replace(split_text[i+1], " ")

  return text


#Test functions

print(censor_single_word(email_one, first_censor))
print(censor_multiple_words(email_two))
print(censor_negative_words(email_three))
print(censor_before_after(email_four))
