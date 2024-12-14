# Retrieve the book with title '1984'

book = Book.objects.get(title="1984")

book

# output

<Book: 1984 by George Orwell published in 1949>
