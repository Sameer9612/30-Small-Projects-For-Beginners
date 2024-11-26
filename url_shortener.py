import pyshorteners

link = input("Enter the link you want to shorten: ")

shortener = pyshorteners.Shortener()

shorted_link = shortener.tinyurl.short(link)

print(shorted_link)






