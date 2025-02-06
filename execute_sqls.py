from cls_helper_log import LogHelper
from cls_helper_sqlalchemy import SQLAlchemyHelper
from models import Base, BankAccounts, Transactions
from sqlalchemy import create_engine, func, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///our_finances.sqlite"

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

queries = [
    """
SELECT strftime('%Y-%m', t.date) as month, 
SUM(credit) as money_in, 
SUM(debit) as money_out, 
SUM(credit - debit) as net_amount
FROM bank_accounts b 
JOIN transactions t ON b.key = t.key
WHERE b."our_money" = "TRUE"
AND t.description LIKE "X%"
GROUP BY month
ORDER BY month
    """,
    """
SELECT t.key, SUM(credit) as money_in, SUM(debit) as money_out, SUM(credit - debit)
FROM bank_accounts b JOIN transactions t
ON b.key = t.key
WHERE "our_money"="TRUE"
AND t.date BETWEEN "2025-01-01" AND "2025-01-31"
AND t.description LIKE "X%"
GROUP BY t.key
    """,
]
# Execute the query
with engine.connect() as connection:
    for query in queries:
        print(query)
        result = connection.execute(text(query))
        for row in result:
            print(row)


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
        Transactions.description.like("X%"),
        Transactions.date.between("2025-01-01", "2025-01-31"),
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
            + f", Money In: {result.money_in}"
            + f", Money Out: {result.money_out}"
            + f", Net Amount: {result.net_amount}"
        )
