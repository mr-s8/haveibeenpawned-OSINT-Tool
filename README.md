# haveibeenpawned-OSINT-Tool
This python script can be given a .txt file with names. It will then create a list of emails that could belong to people with the given names (firstname + some character + lastname + common email domain). Then the script passes all emails to the hibp API (an api key is needed), which then checks them for databreaches. The answer of the API is stored in a .txt file

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. create a names.txt (if you name it differently you have to also change the name in the main.py file) file where the main.py is located. 
2. if you dont have one, create a results.txt file (if you name it differently you have to also change the name in the main.py file) where the main.py is located. ---- it should be automaticaly added if you dont create one
3. store the names u want to check in the names.txt - use a new line for every fullname and use spaces between first and lastname (casing doesnt matter in emails):
4.Add your API Key in line 45
5.let the program run
6.look at results.txt
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------mby i made mistakes

