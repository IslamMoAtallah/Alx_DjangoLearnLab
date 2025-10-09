````markdown
# Delete Operation

```python
from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify deletion
Book.objects.all()

# Expected Output:
# <QuerySet []>
```
````
