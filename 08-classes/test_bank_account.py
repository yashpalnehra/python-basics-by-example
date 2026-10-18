import pytest

from bank_account import BankAccount, InsufficientFunds, SavingsAccount


def test_deposit_and_withdraw():
    acct = BankAccount("Sam", 100)
    acct.deposit(50)
    acct.withdraw(30)
    assert acct.balance == 120
    assert acct.history == [("deposit", 50), ("withdraw", 30)]


def test_cannot_overdraw():
    acct = BankAccount("Sam", 10)
    with pytest.raises(InsufficientFunds):
        acct.withdraw(11)
    assert acct.balance == 10


def test_amount_must_be_positive():
    acct = BankAccount("Sam")
    with pytest.raises(ValueError):
        acct.deposit(0)
    with pytest.raises(ValueError):
        acct.withdraw(-5)


def test_transfer_moves_money():
    a = BankAccount("A", 100)
    b = BankAccount("B")
    a.transfer(b, 40)
    assert (a.balance, b.balance) == (60, 40)


def test_savings_interest():
    acct = SavingsAccount("Sam", 1000, rate=0.05)
    assert acct.add_interest() == 50
    assert acct.balance == 1050


def test_interest_on_empty_account():
    acct = SavingsAccount("Sam")
    assert acct.add_interest() == 0
    assert acct.history == []


def test_str():
    assert str(BankAccount("Sam", 12.5)) == "Sam: 12.50"
