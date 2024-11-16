# Delete the book

book.delete()

# Confirm deletion by trying to retrieve the book

Book.objects.filter(title="Nineteen Eighty-Four").exists()
