import os

def main():

    path = '../GrahakSeva/grahakseva/www.grahakseva.com/complaints/'
    #path2 = "100602/climb-first-good-marketing-to-make-bakras-fool-them-after-they-join-the-class.html"
    c = 0
    flag = 0
    categories = []
    try:
        l = os.listdir(path)
        # print l
        for folder in l:
            path2 = path + folder

            if os.path.isdir(path2):
                for filename in os.listdir(path2):
                    fname = path2+'/'+filename
                    if os.path.isfile(fname):
                        ff = open(path2+'/'+filename,'r')
                        text = ff.read()
                        # print text
                        c += 1
                        print c
                        text = text.split("<!DOCTYPE html><html lang=\"en\">")
                        find_t = "content=\"text/html;charset=utf-8\" /><meta name=\"google-site-verification\" content=\"R9ykra4wlC3hy_7W_QXEtjkQUjHy2mKcU7tDXOpL--o\" /><title>"
                        for words in text:
                            if find_t in words:
                                title = words.split(find_t)[1]
                                title = title.split("- Grahak Seva")[0]
                                # print title
                                find = "</a></div></div><div id=\"_cacp\" class="
                                if find in words:
                                    cat = words.split(find)
                                    category =  cat[0].split('>')[-1]
                                    category = category.replace("&amp;","And")
                                    category = category.replace("/","")
                                    category = category.replace(" ","")
                                    # print category
                                    categories.append(category)
                                    fff = open(category+".txt",'a')
                                    # fff.write(" ")
                                    fff.write(title+"\n")
                                    fff.close()
    except Exception as e:
        print e
        pass

main()
