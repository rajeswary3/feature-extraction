
## to filter out special chars except for comma ''' "()" '/""'

def text_to_word_sequence(text,filters='-!"#$%*+.:;<=>?@[\\]^_`{|}~\t\n,',lower=True, split=" "):
  
    if lower:
        text = text.lower()
    text = text.translate(str.maketrans(filters, split * len(filters)))
 
    return text;

def convertShortExp(word):
    
    if word=="nt":
        fullw ="not"
    elif word=="tho":
        fullw ="though"
    elif word =="wud":
        fullw ="would"
    elif word =="cud":
        fullw = "could"
    elif (word == "aren't") or (word == "aren 't") :
        fullw = "are not"
    elif (word =="can't") or (word =="can 't"):
        fullw = "cannot"   
    elif (word == "couldn't") or (word == "couldn 't"):
        fullw = "could not"
    elif (word == "'d") or (word == " 'd") :
        fullw = "would"
    elif (word == "daren't") or (word == "daren 't"):
        fullw = "dare not"
    elif (word == "didn't") or (word == "didn 't"):
        fullw = "did not"
    elif (word == "doesn't") or (word == "doesn 't"):
        fullw = "does not"
    elif (word == "don't") or  (word == "don 't")  :
        fullw = "does not"
    elif (word == "'em") or  (word == " 'em") :
        fullw = "them"
    elif (word == "hadn't") or  (word == "hadn 't") :
        fullw = "had not"    
    elif (word == "hasn't") or  (word == "hasn 't") :
        fullw = "has not"  
    elif (word == "haven't") or  (word == "haven 't"):
        fullw = "have not"  
    elif (word == "he'd") or  (word == "he 'd") :
        fullw = "he would"
    elif (word == "he'll") or (word == "he 'll") :
        fullw = "he will"
    elif (word == "he's") or  (word == "he 's"):
        fullw = "he is"
    elif (word == "i'd") or (word == "i 'd"):
        fullw = "i would"
    elif (word == "i'll") or (word == "i 'll"):
        fullw = "i will" 
    elif (word == "i'm") or (word == "i 'm") :
        fullw = "i am" 
    elif (word == "isn't") or (word == "isn 't") :
        fullw = "is not" 
    elif (word == "it'd") or  (word == "it 'd"):
        fullw = "it would" 
    elif (word == "it'll") or  (word == "it 'll"):  
        fullw = "it will" 
    elif (word == "it's") or (word == "it 's"):
        fullw = "it is"
    elif (word == "i've") or (word == "i 've") :
        fullw = "i have"
    elif (word == "let's") or (word == "let 's"):
        fullw = "let us"
    elif (word == "mightn't") or  (word == "mightn 't") :
        fullw = "might not"
    elif (word == "mustn't") or  (word == "mustn 't") :
        fullw = "must not"
    elif (word == "needn't") or (word == "needn 't") :
        fullw = "need not"
    elif (word == "oughtn't") or (word == "oughtn 't") :
        fullw = "ought not"
    elif (word == "'s") or (word == " 's") :
        fullw = "is"
    elif (word == "shan't") or (word == "shan 't"):
        fullw = "shall not"
    elif (word == "she'd") or (word == "she 'd"):
        fullw = "she would"
    elif (word == "she'll") or  (word == "she 'll") :
        fullw = "she will"
    elif (word == "she's") or  (word == "she 's"):
        fullw = "she is"
    elif (word =="shouldn't") or (word =="shouldn 't") :
        fullw = "should not"
    elif (word == "they'd") or  (word == "they 'd"):
        fullw = "they would" 
    elif (word == "they'll") or (word == "they 'll") :
        fullw = "they will"
    elif (word == "they're") or (word == "they 're"):
        fullw = "they are"
    elif (word == "they've") or (word == "they 've"):
        fullw = "they have"
    elif (word == "'tis")or (word == " 'tis") :
        fullw = "it is"
    elif (word == "'twas") or (word == " 'twas") :
        fullw = "it was"
    elif (word == "'ve") or (word == " 've") :
        fullw = "have"
    elif (word == "'ve") or  (word == " 've"):
        fullw = "have"
    elif (word == "wasn't") or (word == "wasn 't") :
        fullw = "was not"
    elif (word == "we'd") or (word == "we 'd"):
        fullw = "we would"
    elif (word == "we'll") or (word == "we 'll"):
        fullw = "we will"
    elif (word == "we're") or (word == "we 're"):
        fullw = "we are"
    elif (word == "weren't") or (word == "weren 't")  :
        fullw = "were not"
    elif (word == "we've") or (word == "we 've"):
        fullw = "we have"
    elif (word == "what's") or (word == "what 's"):
        fullw = "what is"
    elif (word == "who'd") or (word == "who 'd") :
        fullw = "who would"
    elif (word == "who'll") or (word == "who 'll"):
        fullw = "who will"
    elif (word == "who're") or (word == "who 're") :
        fullw = "who are"
    elif (word == "who's") or (word == "who 's"):
        fullw = "who is"
    elif (word == "who've") or (word == "who 've"):
        fullw = "who have"
    elif (word == "won't") or  (word == "won 't"):
        fullw = "will not"
    elif (word == "wouldn't")or (word == "wouldn 't") :
        fullw = "would not"
    elif (word == "would've") or  (word == "would 've"):
        fullw = "would have"
    elif (word == "you'd") or (word == "you 'd"):
        fullw = "you would"
    elif (word == "you'll") or (word == "you 'll"):
        fullw = "you will"
    elif (word == "you're") or (word == "you 're"):
        fullw = "you are"
    elif (word == "you've") or  (word == "you 've"):
        fullw = "you have"
    elif (word == "n't") or (word == "n 't"):
        fullw = "not"
    elif (word == "'m") or (word == " 'm"):
        fullw = "am"
    elif (word == "'t") or (word == " 't"):
        fullw = "not"
    elif (word == "'re") or (word == " 're"):
        fullw = "are"
    elif (word == "bit") or (word == "'bit"):
        fullw = "little"   
    else:
        fullw=word
    
        
    return fullw;

def chkIfOpinionWord (word):
    

    allOpinion=[]
    with open("OpinionLexiconNew.txt", "r") as file:
          for line in file:
            s = line.rstrip()  
            if (len(s)>1):
                allOpinion.append(s)       
    file.close()
    exist = ""
    op =""
    for a in range ( len (allOpinion)):
        op = allOpinion[a]
        if ( op== word):
            exist ="true"
            break
            
        else:
            exist ="false"   
    return exist;
    

def chkIfAlreadyExist(word,strArr):
    strW = strArr.split("|")
    for b in range (len(strW)):
        strWW = strW[b]
        wExist= "false"
        if ( word in strWW):
            wExist ="true"
            break
    return wExist;
        
    
def chkIfAlreadyExistExactMatch(word,strArr):

    strW = strArr.split("|")
    for b in range (len(strW)):
        strWW = strW[b]
        wExist= "false"
        if ( word == strWW):
            wExist ="true"
            break
    return wExist;
        
