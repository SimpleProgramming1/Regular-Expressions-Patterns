
# Parsing 

from bs4 import BeautifulSoup
import urllib.request

page= urllib.request.urlopen('https://statecancerprofiles.cancer.gov/quick-profiles/index.php?statename=newjersey')

soup=BeautifulSoup(page,'html.parser')


print(soup)



# Creating Word Count Frequency and plotting
 
import nltk
from nltk.tokenize import word_tokenize
text=soup.get_text(strip=True)

print(text)


word_tokens=word_tokenize(text)

print(word_tokens)


cts=nltk.FreqDist(word_tokens)

cts.plot(20)


# Regular Expression package

import re
#Patterns
#Functions




# Find all Alphanumeric charaters 
text1=re.findall("\w",text)
print(text1)


# Find all characters other than alphanumeric characters 
text1=re.findall("\W",text)
print(text1)


# In[75]:

# Find all digit characters 
text1=re.findall("\d",text)
print(text1)


# Find all characters other than digits  
text1=re.findall("\D",text)
print(text1)


# Find the words in the data
text1=re.findall("\w+",text)
print(text1)



# Find words starting with
text1=re.findall(r"\bS\w+","Sand sand water")
print(text1)



# Find words ending with
text1=re.findall(r"\w+d\b","Sand sand water")
print(text1)


# Find emails 
text1=re.findall(r"\w+@\w+.com","Sand egucdvu@google.com dshvav@yahoo.com sand water")
print(text1)





