````markdown
# Update Operation

```python
from bookshelf.models import Book

# Retrieve the book and update its title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book

# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
```
````