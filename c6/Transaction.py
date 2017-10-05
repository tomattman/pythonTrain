import pickle

class Transaction:

	def __init__(self, amount, date, currency = "USD", usd_conversion_rate = 1, description = None):
		"""
        >>> t = Transaction(100, "2008-12-09")
        >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
        (100, 'USD', 1, 100)
        >>> t = Transaction(250, "2009-03-12", "EUR", 1.53)
        >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
        (250, 'EUR', 1.53, 382.5)
        """
		self.__amount = amount
		self.__date = date
		self.__currency = currency
		self.__usd_conversion_rate = usd_conversion_rate
		self.__description = description

	@property
	def amount(self):
		return self.__amount

	@property
	def date(self):
		return self.__date

	@property
	def currency(self):
		return self.__currency

	@property
	def usd_conversion_rate(self):
		return self.__usd_conversion_rate

	@property
	def description(self):
		return self.__description

	@property
	def usd(self):
		return self.__amount * self.__usd_conversion_rate

class Account:
	"""
    >>> import os
    >>> import tempfile
    >>> name = os.path.join(tempfile.gettempdir(), "account01")
    >>> account = Account(name, "Qtrac Ltd.")
    >>> os.path.basename(account.number), account.name,
    ('account01', 'Qtrac Ltd.')
    >>> account.balance, account.all_usd, len(account)
    (0.0, True, 0)
    >>> account.apply(Transaction(100, "2008-11-14"))
    >>> account.apply(Transaction(150, "2008-12-09"))
    >>> account.apply(Transaction(-95, "2009-01-22"))
    >>> account.balance, account.all_usd, len(account)
    (155.0, True, 3)
    >>> account.apply(Transaction(50, "2008-12-09", "EUR", 1.53))
    >>> account.balance, account.all_usd, len(account)
    (231.5, False, 4)
    >>> account.save()
    >>> newaccount = Account(name, "Qtrac Ltd.")
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (0.0, True, 0)
    >>> newaccount.load()
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (231.5, False, 4)
    >>> try:
    ...     os.remove(name + ".acc")
    ... except EnvironmentError:
    ...     pass
    """

	def __init__(self, number, name):	
	"""
    >>> import os
    >>> import tempfile
    >>> name = os.path.join(tempfile.gettempdir(), "account01")
    >>> account = Account(name, "Qtrac Ltd.")
    >>> os.path.basename(account.number), account.name,
    ('account01', 'Qtrac Ltd.')
    >>> account.balance, account.all_usd, len(account)
    (0.0, True, 0)
    >>> account.apply(Transaction(100, "2008-11-14"))
    >>> account.apply(Transaction(150, "2008-12-09"))
    >>> account.apply(Transaction(-95, "2009-01-22"))
    >>> account.balance, account.all_usd, len(account)
    (155.0, True, 3)
    >>> account.apply(Transaction(50, "2008-12-09", "EUR", 1.53))
    >>> account.balance, account.all_usd, len(account)
    (231.5, False, 4)
    >>> account.save()
    >>> newaccount = Account(name, "Qtrac Ltd.")
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (0.0, True, 0)
    >>> newaccount.load()
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (231.5, False, 4)
    >>> try:
    ...     os.remove(name + ".acc")
    ... except EnvironmentError:
    ...     pass
    """	
		self.__number = number
		self.__name = name
		self.__transactions = []

	@property
	def number(self):
		return self.__number

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		assert len(name) >= 4, "account name must be at least 4 characters"
		self.__name = name

	def __len__(self):
		return len(self.__transactions)

	@property
	def balance(self):
		balance = 0.0
		for transaction in self.__transactions:
			balance += transaction.usd
		return balance

	@property
	def all_usd(self):
		for transaction in self.__transactions:
			if not transaction.currency != "USD":
				return False
		return True

	def apply(self, transaction):
		self.__transactions.append(transaction)

	def save(self):
		fh = None
        try:
            data = [self.number, self.name, self.__transactions]
            fh = open(self.number + ".acc", "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()

	def load(self):
		fh = None
        try:
            fh = open(self.number + ".acc", "rb")
            data = pickle.load(fh)
            assert self.number == data[0], "account number doesn't match"
            self.__name, self.__transactions = data[1:]
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()

if __name__ == "__main__":
    import doctest
    doctest.testmod()


