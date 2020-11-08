import urllib3 as u


http = u.PoolManager()

p = http.request('GET','https://sites.google.com/view/amigoshop') #p for page


print(p.status)
'''
Informational responses (100–199)
Successful responses (200–299)
Redirects (300–399)
Client errors (400–499)
Server errors (500–599)
'''

p.read()

'''
######in here I'm checking if the p (page) is a urllib3.response.HTTPResponse object
if isinstance(p,u.response.HTTPResponse):
    print('yes of course')
else:
    print(' no men you\'re wrong')
'''

print('################################################################################################')

print(p.data.decode('utf-8'))

print('################################################################################################')
#print(p.data)
#print('################################################################################################')
print('done')

