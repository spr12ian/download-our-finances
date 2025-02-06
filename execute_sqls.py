from cls_helper_log import LogHelper
from cls_helper_sqlalchemy import SQLAlchemyHelper
from models import BankAccounts, Transactions
from sqlalchemy import create_engine, func, not_, text
from sqlalchemy.orm import sessionmaker
import utility_functions as uf

DATABASE_URL = "sqlite:///our_finances.sqlite"

# Create an engine
#engine = create_engine(DATABASE_URL, echo=True)
engine = create_engine(DATABASE_URL)

queries = [
    """
SELECT strftime('%Y-%m', t.date) as month, 
SUM(credit) as money_in, 
SUM(debit) as money_out, 
SUM(credit - debit) as net_amount
FROM bank_accounts b 
JOIN transactions t ON b.key = t.key
WHERE b."our_money" = "TRUE"
AND t.description NOT LIKE "X%"
GROUP BY month
ORDER BY month
    """,
    """
SELECT t.key, SUM(credit) as money_in, SUM(debit) as money_out, SUM(credit - debit)
FROM bank_accounts b JOIN transactions t
ON b.key = t.key
WHERE "our_money"="TRUE"
AND t.date BETWEEN "2025-01-01" AND "2025-01-31"
AND t.description NOT LIKE "X%"
GROUP BY t.key
    """,
]
# Execute the query
# with engine.connect() as connection:
#     for query in queries:
#         print(query)
#         result = connection.execute(text(query))
#         for row in result:
#             print(row)


# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Perform the query
results = (
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
        Transactions.date.between("2025-02-01", "2025-02-28"),
    )
    .group_by(func.strftime("%Y-%m", Transactions.date))
    .order_by("month")
    .all()
)

if len(results):
    # Print the results
    for result in results:
        print(
            f"Month: {result.month}"
            + f", In: {uf.format_as_gbp(result.money_in, 11)}"
            + f", Out: {uf.format_as_gbp(result.money_out, 11)}"
            + f", Amount: {uf.format_as_gbp(result.net_amount, 11)}"
        )


# Perform the query
results = (
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
        Transactions.date.between("2025-02-01", "2025-02-28"),
    )
    .order_by("d")
    .all()
)

if len(results):    
    print(
        "Date           Credit      Debit        Net Description"
    )
    # Print the results
    for result in results:
        date=result.d
        plus=uf.format_as_gbp(result.plus, 11)
        minus=uf.format_as_gbp(result.minus, 11)
        net=uf.format_as_gbp(result.net, 11)
        description=result.description
        print(
            f"{date}{plus}{minus}{net} {description}"
        )
