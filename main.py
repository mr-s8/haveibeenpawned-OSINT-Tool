import requests

# defining a function that returns many email addresses, that could belong to a person with a given first and last name, stored in a list


def name(first_name, last_name):
    l = []
    # specifying which seperators to use between first and lastname; you can add new characters if you like
    seperators = [".", "-", "_", ""]
    # specifying the list of email domains to use, i googled the most popular ones and added some for my country; change them if you want
    mails = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@gmx.de", "@web.de"]
    # adding firstname seperator, lastname and emaildomain together and storing it in a list
    for domain in mails:
        for char in seperators:
            l.append(first_name + char + last_name + domain)
    return l


# getting the names from the text file names.txt; change the name if needed
get_names = open("names.txt", "r")

names_to_check = []

for line in get_names:
    # deleting the \n character that is created when u add a new line to a textfile
    names_to_check.append(line.strip())

# splitting the text in every line and putting it into a list, so we now
counter = 0
emails_to_check = []
for fullname in names_to_check:
    a = names_to_check[counter].split(' ', 1)
    emails_to_check.append(name(a[0], a[1]))
    counter += 1


# getting and storing the result for each email in the results.txt file

# change the filename if u name the file to store the results differently
res = open('results.txt', 'a')

for list in emails_to_check:
    for email in list:
        req = requests.get(r"https://haveibeenpwned.com/api/v3/breachedaccount/"+email, headers={
            "hibp-api-key": "your api key here"  # put your api key between the brackets
        })
        res.write(req)
        res.write("\n\n")
res.write("\n")
res.write("Checked Breaches for these emails: " + emails_to_check)


"""
things i add mby:
-add a mode for phone numbers or use name and phonenumber at the same time
-print error if only a first or a last name is given in a line in the names.txt file
-print error if three names are given in names.txt file or a the add the function to create emails consistin of three names
"""
