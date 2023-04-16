#!/usr/bin/env python
# coding: utf-8

# In[31]:


def pluralize(noun):
    if noun.endswith('y'):
        if noun[-2] not in 'aeiou':
            return noun[:-1] + 'ies'
    elif noun[-1] in 'sx' or noun[-2:] in ['sh', 'ch']:
        return noun + 'es'
    elif noun.endswith('man'):
        return noun[:-3] + 'men'
    else:
        return noun + 's'


def add_article(item_list):
    dict = {}
    description = ""
    for key in item_list:
        dict[key] = dict.get(key, 0) + 1
    lenth = len(dict)
    for i in dict.keys():
        if dict[i] > 1:
            item = pluralize(str(i))
        else:
            item = str(i)
        if lenth == 1:
            description += "and" + " " + str(dict[i]) + " " + item + '.'
        else:
            description += str(dict[i]) + " " + item + ", "  
            lenth = lenth - 1
    return description

def add_a_an(noun):
    if noun[0] in ['a', 'e', 'i', 'o', 'u']:
        return 'an ' + noun
    else:
        return 'a ' + noun


def replace_word(string, target_word, replacement_sentence):
    words = string.split()
    for i in range(len(words)):
        if words[i] == target_word:
            words[i] = replacement_sentence
    new_string = " ".join(words)
    return new_string


def check_word_from_sentence(sentence, word):
    words = sentence.split()
    if word in words:
        words.remove(word)
        new_sentence = " ".join(words)
        return True, new_sentence
    else:
        return False, sentence


def add_article_a_an(item_list):
    dict = {}
    description = ""
    for key in item_list:
        dict[key] = dict.get(key, 0) + 1
    lenth = len(dict)
    for i in dict.keys():
        if lenth == 1:
            description += "or" + " " + add_a_an(str(i)) + "?"
        else:
            description += add_a_an(str(i)) + ", "  
            lenth = lenth - 1
    return description




def Make_up_template(trust_candidate, template):
    prompt = ""
    make_up_xxx = []

    trust_items = add_article(trust_candidate)
    print(trust_items)
    temporary = template
    new_sentence = replace_word(temporary,"xxx",trust_items)
    print(new_sentence)
    make_up_xxx.append(new_sentence) 
    return new_sentence


# In[46]:


items = ['bed','carpet','vase','Bedside cabinet']

Template = "There is a room, in the room, there is xxx \n"
Question = "What room it could be like?(bedroom, iving room, office place or somthing else)            answer with just one word"

template = Make_up_template(items,Template)


# In[47]:


template


# In[36]:


import openai


gpt_version = "gpt-3.5-turbo"  

openai.api_key = openai_api_key
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": template+Question}]
)


# In[37]:


completion


# In[48]:


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": template+Question}],
  max_tokens=2, 
  temperature=0
)


# In[50]:


completion["choices"][0]["message"]["content"].strip()  


# In[51]:


completion


# In[ ]:




