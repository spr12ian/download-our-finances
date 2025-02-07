from cls_helper_sqlalchemy import SQLAlchemyHelper
from cls_helper_date_time import DateTimeHelper
from models import BankAccounts, Transactions
from sqlalchemy import func, not_, text
import utility_functions as uf
from sqlalchemy.dialects import sqlite


sql = SQLAlchemyHelper()
session = sql.get_session()


query = (
    session.query(
        func.strftime("%Y-%m", Transactions.date).label("month"),
        func.sum(Transactions.credit).label("money_in"),
        func.sum(Transactions.debit).label("money_out"),
        func.sum(Transactions.credit - Transactions.debit).label("net_amount"),
    )
    .join(BankAccounts, BankAccounts.key == Transactions.key)
    .filter(
        BankAccounts.our_money == "TRUE",
        not_(Transactions.description.like("X%")),
        Transactions.date.between("2025-01-01", "2025-01-31"),
    )
    .group_by(func.strftime("%Y-%m", Transactions.date))
    .order_by("month")
)

print(query.statement.compile(compile_kwargs={"literal_binds": True}))

# Perform the query
results = query.all()
if len(results):
    # Print the results
    for result in results:
        print(
            f"Month: {result.month}"
            + f", In: {uf.format_as_gbp(result.money_in, 11)}"
            + f", Out: {uf.format_as_gbp(result.money_out, 11)}"
            + f", Amount: {uf.format_as_gbp(result.net_amount, 11)}"
        )

query = (
    session.query(
        Transactions.date.label("d"),
        Transactions.credit.label("plus"),
        Transactions.debit.label("minus"),
        (Transactions.credit - Transactions.debit).label("net"),
        Transactions.description.label("description"),
    )
    .join(BankAccounts, BankAccounts.key == Transactions.key)
    .filter(
        BankAccounts.our_money == "TRUE",
        not_(Transactions.description.like("X%")),
        Transactions.date.between("2025-01-01", "2025-01-31"),
    )
    .order_by("d")
)

print(query.statement.compile(compile_kwargs={"literal_binds": True}))

# Perform the query
results = query.all()
if len(results):
    dth = DateTimeHelper()
    print("Date           Credit      Debit        Net Description")
    # Print the results
    for result in results:
        date = dth.ISO_to_UK(result.d)
        plus = uf.format_as_gbp(result.plus, 11)
        minus = uf.format_as_gbp(result.minus, 11)
        net = uf.format_as_gbp(result.net, 11)
        description = result.description
        print(f"{date}{plus}{minus}{net} {description}")
