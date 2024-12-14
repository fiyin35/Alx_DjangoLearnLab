# create

from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book

# Output

<Book: 1984 by George Orwell published in 1949>

# retrieve

book = Book.objects.get(title="1984")

book

# output

<Book: 1984 by George Orwell published in 1949>

# update

book.title = "Nineteen Eighty-Four"

book.save()

# output

<Book: Nineteen Eighty-Four by George Orwell published in 1949>

# delete

book.delete()

# Confirm deletion by trying to retrieve the book

Book.objects.filter(title="Nineteen Eighty-Four").exists()
