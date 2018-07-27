from os import environ
import sqlite3

DATABASE_NAME = environ.get('DATABASE_NAME')  

class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {
            'name': self.name,
            'price': self.price
        }

    @classmethod
    def find_by_name(cls, name):
        con = sqlite3.connect(DATABASE_NAME)
        cr = con.cursor()

        query = 'SELECT * FROM items WHERE name=?'
        result = cr.execute(query, (name,))
        row = result.fetchone()
        con.close()
        if row:
            return cls(*row)
    
    def insert(self):
        '''
        Args:
            cls -> The current class
            item -> Dictionary with name and price keys'''
        con = sqlite3.connect(DATABASE_NAME)
        cr = con.cursor()
        query = "INSERT INTO items VALUES (?,?)"
        cr.execute(query, (self.name, self.price) )

        con.commit()
        con.close()

    
    def update(self):
        '''
        Args:
            cls -> The current class
            item -> Dictionary with name and price keys'''
        con = sqlite3.connect(DATABASE_NAME)
        cr = con.cursor()
        query = "UPDATE items SET price = ? WHERE name = ?"
        cr.execute(query, (self.price, self.name) )
        con.commit()
        con.close()