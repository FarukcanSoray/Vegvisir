import sqlite3

class Offer:
    def __init__(self, date, company, contact, telephone, mail, address, remindTime):
        self.offerDate = date
        self.company = company
        self.contact = contact
        self.telephone = telephone
        self.mail = mail
        self.address = address
        self.remindTime = remindTime

class Database:
    def __init__(self):
        self.create_tables()

    def make_connection(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def create_tables(self):
        self.make_connection()
        query = "CREATE TABLE IF NOT EXISTS offers (offerID INTEGER PRIMARY KEY AUTOINCREMENT, offerDate TEXT, company TEXT, contact TEXT, telephone TEXT, mail TEXT, address TEXT, remindTime INT)"
        self.cursor.execute(query)
        self.connection.commit()

        self.disconnect()

    def add_offer(self, offer):
        self.make_connection()
        query = "INSERT INTO offers VALUES(null, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (offer.offerDate, offer.company, offer.contact, offer.telephone, offer.mail, offer.address, offer.remindTime))
        self.connection.commit()
        self.disconnect()

    def find_last_offer(self):
        self.make_connection()
        query = "SELECT offerDate, company, contact, telephone, mail, address, remindTime FROM offers WHERE offerID = (select max(offerID) from offers)"
        self.cursor.execute(query)
        last_offer = self.cursor.fetchall()
        self.disconnect()
        return last_offer

    def edit_offer(self, offer):
        self.make_connection()
        query = "UPDATE offers SET offerDate = ?, company = ?, contact = ?, telephone = ?, mail = ?, address = ?, remindTime = ? WHERE offerID = (select max(offerID) from offers)"
        self.cursor.execute(query, (offer.offerDate, offer.company, offer.contact, offer.telephone, offer.mail, offer.address, offer.remindTime,))
        self.connection.commit()
        self.disconnect()

    def make_last_10_offer(self):
        self.make_connection()
        query = "SELECT * FROM offers ORDER BY offerID DESC LIMIT 10"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.disconnect()
        return result

    def make_last_offer(self):
        self.make_connection()
        query = "SELECT * FROM offers ORDER BY offerID DESC LIMIT 1"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.disconnect()
        return result

    def make_list_for_recommend_autofill(self):
        self.make_connection()
        query = "SELECT DISTINCT company FROM offers"
        self.cursor.execute(query)
        companies = self.cursor.fetchall()
        list = []
        for i in companies:
            list.append(i[0])
        self.disconnect()
        return list

    def search_by_company(self, name):
        self.make_connection()
        query = "SELECT * FROM offers  WHERE company = ? ORDER BY offerID DESC"
        self.cursor.execute(query, (name,))
        result = self.cursor.fetchall()
        self.disconnect()
        return result

    def get_last_offer_for_autofill(self, name):
        self.make_connection()
        query = "SELECT contact, telephone, mail, address, remindTime FROM offers WHERE company = ? ORDER BY offerID DESC LIMIT 1"
        self.cursor.execute(query, (name,))
        result = self.cursor.fetchall()
        list = []
        for i in result:
            list.append(i)
        self.disconnect()
        return list

    def get_offer_by_id(self, id):
        self.make_connection()
        query = "SELECT * FROM offers WHERE offerID = ?"
        self.cursor.execute(query, (id,))
        result = self.cursor.fetchall()
        self.disconnect()
        return result
