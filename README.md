# haveibeenpawned-OSINT-Tool
This python script can be given a .txt file with names. It will then create a list of emails that could belong to people with the given names (firstname + some character + lastname + common email domain). Then the script passes all emails to the hibp API (an api key is needed), which then checks them for databreaches. The answer of the API is stored in a .txt file
