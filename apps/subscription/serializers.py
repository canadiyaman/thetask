class BookSerializer(object):
    def __init__(self, initial_data, request):
        self.initial_data = initial_data

    @property
    def data(self):
        return self.initial_data


class BookListSerializer(BookSerializer):

    @property
    def data(self):
        book_list = list()
        for _book in self.initial_data:
            book_list.append(_book)
        return book_list
