from odoo.tests.common import TransactionCase
class TestBook(TransactionCase):
    def setup(self, *args, **kwargs):
        super().setUp(*args, **kwargs)  #When the setUp method of TestBook gets executed, the line super().setUp(*args, **kwargs) ensures that
                                        # The setUp method of the parent class (TransactionCase) also runs.
                                        # Any arguments (either positional or keyword) provided to TestBook's setUp method are forwarded to the setUp method of TransactionCase
        self.Book = self.env["library.book"] # asking the Odoo environment to give you access to the model named library.book
        self.book1 = self.Book.create({"name": "Odoo development Essentials", "isbn": "879-1-78439-279-6"})

