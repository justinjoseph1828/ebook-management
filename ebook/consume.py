import requests
base_url="http://127.0.0.1:8000/"


# Create a new book
data =      {
            "title": "The PSychology of money",
            "author": "Morgan housewl",
            "genre": "Non-Fiction",
            "review": 4,
            "favorite": "false"}
response = requests.post(base_url + 'books/', data=data)
print(response.status_code)
print(response.json())

#  Get a list of books.
response = requests.get(base_url + 'books/')
print(response.status_code)
print(response.json())

#  Get a detail view of a book
response = requests.get(base_url + 'bookdetail/15')
print(response.status_code)
print(response.json())

# Update an existing object
data ={
    "title": "wings of fire by APJ",
    "author": "APJ Abdul Kalam",
    "genre": "Literary",
    "review": 5,
    "favorite": "false"
}
response = requests.put(base_url + 'bookdetail/2', data=data)
print(response.status_code)
print(response.json())

# Delete an book
response = requests.delete(base_url + 'bookdetail/15')
print(response.status_code)
