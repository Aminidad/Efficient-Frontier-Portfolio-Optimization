# ODIN 
An Efficient Frontier Portfolio Optimization Tool using Python

# Description
Modern Portfolio Theory (MPT) is an investment theory developed by Harry Markowitz and published under the title “Portfolio Selection” in the Journal of Finance in 1952.
ODIN is a tool developed to handle both NASDAQ and TSE markets in terms of efficient distribution percentage of wanted stocks given by the user.
As there are no structure, APIs or frameworks for TSE market, Odin also scrapes the information directly from the TSE website and stores all stocks registered under TSE excluding the OTC market in csv files for further use (csv was chosen so both developers and fellow accountants and financial analysts can work with the data).
# Features
- You can choose between QuandL or Odin Libraries to get stock information.
    - Process stock information on TSE (Tehran Stock Exchange Market) using Odin (which is not supported by QuandL).
    - Process stock information on NASDAQ or other stock markets supported by QuandL libraries.    
- Downloads Stock information on all TSE stock (OTC Market excluded).
- Calculates Efficient Frontier with a fixed random Seed for consistency.

# Required Libraries
- Python 3
- Pandas
- QuandL
- numPy
- MatplobLib


