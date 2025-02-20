import re

def list_composers(string_of_composers):

    #finds all the durations and what comes immediatelly before and creates a new string from the resulting list
    news = "".join(re.findall(r"[\w '\-,()]+;\d{2}:\d{2}:\d{2}", string_of_composers))         

    #extracts all the composers from the previous string and forms a new string from them
    composers = "".join(re.findall(r"[^\d:]", news))

    list1 = re.split(r";", composers)

    #remove any empty strings that may have appeared
    list1 = list(filter(None, list1))

    #create set from list so as to remove duplicates and then convert back to list
    composers = list(set(list1))

    #normalizing all names to "last name, rest of name"
    unsplit_names = []
    normalized_names = []
    #separating normalized from non normalized name
    for i in composers:
        if ',' not in i:
            unsplit_names.append(i)
        else:
            normalized_names.append(i)

    #normalizing non normalized names
    reversed_names = []
    for i in unsplit_names:
        splitted = i.split()
        splitted.reverse()
        last_name = splitted.pop(0)
        splitted.reverse()
        final = " ".join(splitted)
        final = last_name + ", " + final
        reversed_names.append(final)

    #final list of composers unsorted
    all_unsorted = normalized_names + reversed_names

    #all composers sorted
    composers = sorted(all_unsorted, key=str.casefold)

    print(composers)

def opusByPeriod(stringOfOpus):
    #finds all the durations composers and periods and creates a new string from the resulting list
    aux = "".join(re.findall(r"[ \w]+;[\w '\-,()]+;\d{2}:\d{2}:\d{2}", stringOfOpus))

    #remove durations from the previous string
    meme = "".join(re.findall(r"[^\d:]", aux))

    list1 = re.split(r";", meme)

    #remove any empty strings that may have appeared
    list1 = list(filter(None, list1))

    periods = []
    #separating periods from composers
    for i in list1:
        if 'Século' in i:
            periods.append(i)
        if ' ' not in i:
            periods.append(i)

    #dictionary of period:number of times
    d = {}
    for p in periods:
        d[p] = periods.count(p)

    #final dictionary sorted alphabetically
    final = dict(sorted(d.items()))
    
    print(final)
    return periods

def listOpusByPeriod(first_opus_line, string, ordered_periods):
    #clean up first_opus_line first opus name
    first_opus_line = re.sub(r" {2,}", "", first_opus_line)       #delete double spaces
    first_opus_line = re.sub(r"\n", " ", first_opus_line)         #replace \n by single space
    first_opus_line = first_opus_line.strip("\n")                 #remove last \n

    #get header line and name of first opus
    aux = "".join(re.findall(r"[\w]+;[\w]+;[\w]+;[\w]+;[\w]+;[\w]+;[\_\w]+[ \w]+", first_opus_line))

    #clean up first opus name
    list1 = re.split(r";", aux)
    first_opus = (list1[6])[4:]


    #finds all the durations composers and periods and creates a new string from the resulting list
    aux = "".join(re.findall(r":\d{2}:\d{2};[É\w\. äöüÄÖÜßÉ']+", string))

    meme = "".join(aux)

    list1 = re.split(r";", meme)
    list2 = []

    for i in list1:
        a = (i[:-6])
        list2.append(a)

    #remove any empty strings that may have appeared
    list2 = list(filter(None, list2))
    listOfOpus = []

    #removing cluter (previous id) from beggining of opus name
    for i in list2:
        string = re.sub(r"O\d+ ", "", i)       #delete double spaces
        listOfOpus.append(string)

    #prepending first opus to list
    listOfOpus = [first_opus]+listOfOpus

    #creating dictionary of periods: list of opus
    d = {}
    i = 0
    while i<len(ordered_periods):
        period = ordered_periods[i]
        if period in d.keys():              #if period already in dict->append
            d[period].append(listOfOpus[i])
        else:                               #if not, create key and add opus to it
            d[period] = [listOfOpus[i]]
        i+=1

    #sort dictionary values
    for period in d:
        sorted_opus = sorted(d.get(period), key=str.casefold)
        d[period] = sorted_opus

    print(d)



def main():

    file = open("obras.csv", "r", encoding="utf-8")

    #read all lines of the csv into a single string
    semi_colons = 0
    string = ""
    firsttwolines = ""
    for line in file:
        string = string + line
        semi_colons+=1
        if semi_colons <=2:
            firsttwolines = firsttwolines + line
    
    #clean up string
    string = re.sub(r" {2,}", "", string)       #delete double spaces
    string = re.sub(r"\n", " ", string)         #replace \n by single space
    string = string.strip("\n")                 #remove last \n

    #list all composers
    print("\nLIST OF COMPOSERS")
    list_composers(string)


    #number of opus by period
    print("\nNumber of Opus by Period")
    periods = opusByPeriod(string)

    #list of opus by period
    print("\nList of Opus by Period")
    listOpusByPeriod(firsttwolines, string, periods)


    file.close()

if __name__ == "__main__":
    main()