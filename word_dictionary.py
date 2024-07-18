from PyMultiDictionary import MultiDictionary
from Pronunciation import pronounce
import eng_to_ipa as ipa





def get_defination(text: str):
    dictionary = MultiDictionary()
    user_input = text
    if dictionary.meaning('en', user_input)[1]:
        file = open('Dictionary_History.txt', "a")
        file.write(user_input)
        file.write("\n")
        file.close()
    # print(ipa.get_rhymes("stew"))

    print(dictionary.meaning('en', user_input)[1])
    print(dictionary.synonym('en', user_input))
    pronounce(user_input)




"""Dictionary Quiz based on the words i have looked up
Pronnouncation"""


