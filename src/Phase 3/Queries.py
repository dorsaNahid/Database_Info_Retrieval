import bsddb3, sys, re
import termSearch
import yearGreater, yearLess

def parseQuery(query):
    numeric="[0-9]"
    alphanumeric="[0-9a-zA-Z]"

    term=alphanumeric + "+"
    termPrefix="(title|author|other):"
    termQuery="({})?{}".format(termPrefix,term)

    year=numeric + "+"
    yearPrefix="(year:|year>|year<)"
    yearQuery="{}{}".format(yearPrefix,year)

    phrase="{}(\\s{})*".format(term,term)
    phraseQuery='({})?"{}"'.format(termPrefix,phrase)

    expression="({}|{}|{})".format(yearQuery,termQuery,phraseQuery)
    querySearch="^{}(\\s{})*$".format(expression,expression)


    # y=re.compile(yearQuery)
    # t=re.compile(termQuery)
    # p=re.compile(phraseQuery)
    #

    if re.match(querySearch,query):
        print("\ncorrect query\n")
        
        it = re.finditer(expression, query)
        for m in it:
            exp=query[m.start():m.end()]
            
            if(exp=="author" or exp=="title" or exp=="other"):
            	continue
        
            if re.match(yearQuery,exp):
                parseYearSearch(exp)
                continue
               
            if re.match(termQuery,exp):
                parseTermSearch(exp)
                continue
					
            if re.match(phraseQuery,exp):
                if m.start()!=0 and query[m.start()-1]==":":
                    if query[m.start()-2]=="e":                		
                        phraseTitleEqualTo(exp[1:-1])
                    elif query[m.start()-3]=="e":
                		   phraseOtherEqualTo(exp[1:-1])
                    else:
                        phraseAuthorEqualTo(exp[1:-1])
                else:
                	phraseNamelessEqualTo(exp[1:-1])
                continue
      
            
    else:
        print("\nincorrect query\n")

	
	
def parseYearSearch(exp):
   for m in re.finditer("<", exp):
      print(yearsLess(exp[m.start()+1:]))
      return
   for m in re.finditer(">", exp):
      print(yearsGreater(exp[m.start()+1:]))
      return

def parseTermSearch(exp):
   for m in re.finditer("title:", exp):
      titleEqualTo(exp[m.start()+6:])
      return
      
   for m in re.finditer("author:", exp):
      authorEqualTo(exp[m.start()+7:])
      return
      
   for m in re.finditer("other:", exp):
      otherEqualTo(exp[m.start()+6:])
      return

   namelessEqualTo(exp)

def yearsGreater(starting_year):
    return yearGreater.yearSearch(starting_year)

def yearsLess(ending_year):
    return yearLess.yearSearch(ending_year)

def titleEqualTo(title):
    return termSearch.termSearch('t-' + title)

def authorEqualTo(author):
    return termSearch.termSearch('a-' + author)

def otherEqualTo(other):
    return termSearch.termSearch('o-' + other)

def namelessEqualTo(nameless):
	print(nameless)


def phraseTitleEqualTo(title):
	print(title)
	
def phraseAuthorEqualTo(author):
	print(author)

def phraseOtherEqualTo(other):
	print(other)

def phraseNamelessEqualTo(nameless):
	print(nameless)



def joinQueries():
    pass


def main():
    for line in sys.stdin:
        parseQuery(line)

if __name__ == '__main__':
    main()
