class SavingAccount:
    pass

class ChekingAccount:
    pass

class BankAccount(SavingAccount, ChekingAccount):
    pass

class Stock:
    pass
class Bond:
    pass
class Security(Stock, Bond):
    pass
class RealEstate:
    pass
class Asset(BankAccount, Security, RealEstate):
    pass

class Insurableltem(RealEstate, BankAccount):
    pass

class InterestBearingItem(BankAccount, Security):
    pass
