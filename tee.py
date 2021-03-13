import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz 
ABCDEFGHIZKLMNOPQRSTUVWXYZ
123456789

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*2222
800-555-2222
900-555-2222


Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson                                                           
Mr. T

'''
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

sentence = "Start a sentence and then bring it to am end"

#print(r'\tTab')

#pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-z-]+\.(com|edu|net)')

#The small letters, caps, digits, _, .(period), +, - followed by @ and then again small, Large, digits, -, .
#pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')    
#pattern = re.compile(r'https?://[a-z.]+')  
#pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')  

      
pattern = re.compile(r'start', re.IGNORECASE)         #Types of Flags = multi-line Flag, verbose--> allows you to add whitespace 
matches = pattern.match(sentence)    #The .match only take care of the beginning of the sentence. If the sentence in the beginning is returning True otherwise None.
matches = pattern.search(sentence)    #Only prints the first match, will not proceed further. If not there will return None.
print(matches)


"""
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)
"""
"""
matches = pattern.finditer(urls)

for match in matches:     #span is the beginning and the end index
    print(match.group(2))
"""

"""
with open("data.txt", "r") as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)
"""