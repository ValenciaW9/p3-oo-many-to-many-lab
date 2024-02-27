from typing import List

class Book:
    members: List['Book'] = []

    def __init__(self, title: str):
        self.title = title
        self.members.append(self)


class Author:
    members: List['Author'] = []

    def __init__(self, name: str):
        self.name = name
        self.members.append(self)

    def contracts(self) -> List['Contract']:
        related_contracts = []
        for contract in Contract.members:
            if contract.author == self:
                related_contracts.append(contract)
        return related_contracts

    def books(self) -> List[Book]:
        related_books = []
        for contract in Contract.members:
            if contract.author == self:
                related_books.append(contract.book)
        return related_books

    def sign_contract(self, book: Book, date: str, royalties: int) -> 'Contract':
        if not isinstance(book, Book):
            raise ValueError("Book must be an instance of the Book class")
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self) -> int:
        total = 0
        for contract in Contract.members:
            if contract.author == self:
                total += contract.royalties
        return total


class Contract:
    members: List['Contract'] = []

    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise ValueError("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise ValueError("Date must be a string")
        if not isinstance(royalties, int):
            raise ValueError("Royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.members.append(self)

    @classmethod
    def contracts_by_date(cls, date: str) -> List['Contract']:
        contracts = []
        for contract in cls.members:
            if contract.date == date:
                contracts.append(contract)
        return contracts