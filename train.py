import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
# from statistics import mode
from nltk.tokenize import word_tokenize
import sys,os,time
import smtplib
# t = time.time()




def send_email(sender,to):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # print 1
    server.starttls()
    # print 2
    server.login(sender, "password")
    # print 3
    msg = "YOUR MESSAGE!"
    server.sendmail(sender, to, msg)
    # print 4
    server.quit()

def encodable(string):
    for i in xrange(len(string)):
        try:
            string[i].decode("utf-8").encode()
        except:
            string  =  string.replace(string[i]," ")
    return string

def classification():
    categories = []
    path = "."
    l = os.listdir(path)
    for folder in l:
        if ".txt" in folder:
            categories.append(folder[:-4])

    kk = []

    allowed_word_types = ["NN","VB","VBP","VBD","J","JJ","NNP"]

    ##########
    for i,cat in enumerate(categories):
        count = 0
        temp =[]
        short_cat = open(cat+".txt","r").read()
        short_cat = encodable(short_cat)
        for p in short_cat.split('\n'):
            words = word_tokenize(p)
            pos = nltk.pos_tag(words)
            no = ["LICENSE","LICENSE-FLAC","Aramex","PF","output"]
            for w in pos:
                if w[1] in allowed_word_types and w[0] not in no:

                    a = {}
                    a[w[0].lower()] = 1
                    temp.append((a,cat))
                    count+=1

        if count > 5000:
            random.shuffle(temp)
            random.shuffle(temp)
            for t in temp[:5000]:
                kk.append(t)
        else:
            for t in temp:
                kk.append(t)
        # print count,cat



    random.shuffle(kk)
    random.shuffle(kk)
    random.shuffle(kk)

    training_set = kk[:4000]
    testing_set = kk[4000:6000]

    voice = open("output.txt",'r').read()
    voice = word_tokenize(voice)
    pos = nltk.pos_tag(voice)

    voice_test = []
    for w in pos:
        if w[1] in allowed_word_types:
            a = {}
            a[w[0].lower()] = 1
            voice_test.append(a)

    MNB_classifier = SklearnClassifier(MultinomialNB())
    MNB_classifier.train(training_set)
    print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

    m = {}
    for text in voice_test:
        k = MNB_classifier.classify(text)
        m[k]  = m.get(k,0)  +1
        ##########
        # send an email to the appropriate category incharge
        # eg. if the complaint is related to Phone Company
        # email would be sent to some email id -phone_company_incharge@gmail.com
        ##########

        print k
    # the category to which the complaint most likely belongs
    max_votes_category =  max(m, key=m.get)
    print "finally, "+max_votes_category
    sys.exit()
