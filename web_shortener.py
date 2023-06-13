# Python webshortener
import pyshorteners as ps
print("**Web shortener**")
url = input("Enter url:")
u = ps.Shortener().tinyurl.short(url)
print("The shorter version of is: ", end = "")
print(u)