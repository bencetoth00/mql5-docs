# Testing Statistics


After the testing is over, different parameters of the trading results statistics are calculated. The values of the parameters can be obtained using the [TesterStatistics()](../../../Common-Functions/TesterStatistics/TesterStatistics.md) function, by specifying the parameter ID from the ENUM\_STATISTICS enumeration.

Although two types of parameters (int and double) are used for calculating statistics, the function returns all values in the double form. All the statistic values of the double type are expressed in the deposit currency by default, unless otherwise specified.

ENUM\_STATISTICS

| ID | Description of a statistic parameter | Type |
| --- | --- | --- |
| STAT\_INITIAL\_DEPOSIT | The value of the initial deposit | double |
| STAT\_WITHDRAWAL | Money withdrawn from an account | double |
| STAT\_PROFIT | Net profit after testing, the sum of STAT\_GROSS\_PROFIT and STAT\_GROSS\_LOSS (STAT\_GROSS\_LOSS is always less than or equal to zero) | double |
| STAT\_GROSS\_PROFIT | Total profit, the sum of all profitable (positive) trades. The value is greater than or equal to zero | double |
| STAT\_GROSS\_LOSS | Total loss, the sum of all negative trades. The value is less than or equal to zero | double |
| STAT\_MAX\_PROFITTRADE | Maximum profit – the largest value of all profitable trades. The value is greater than or equal to zero | double |
| STAT\_MAX\_LOSSTRADE | Maximum loss – the lowest value of all losing trades. The value is less than or equal to zero | double |
| STAT\_CONPROFITMAX | Maximum profit in a series of profitable trades. The value is greater than or equal to zero | double |
| STAT\_CONPROFITMAX\_TRADES | The number of trades that have formed STAT\_CONPROFITMAX (maximum profit in a series of profitable trades) | int |
| STAT\_MAX\_CONWINS | The total profit of the longest series of profitable trades | double |
| STAT\_MAX\_CONPROFIT\_TRADES | The number of trades in the longest series of profitable trades STAT\_MAX\_CONWINS | int |
| STAT\_CONLOSSMAX | Maximum loss in a series of losing trades. The value is less than or equal to zero | double |
| STAT\_CONLOSSMAX\_TRADES | The number of trades that have formed STAT\_CONLOSSMAX (maximum loss in a series of losing trades) | int |
| STAT\_MAX\_CONLOSSES | The total loss of the longest series of losing trades | double |
| STAT\_MAX\_CONLOSS\_TRADES | The number of trades in the longest series of losing trades STAT\_MAX\_CONLOSSES | int |
| STAT\_BALANCEMIN | Minimum balance value | double |
| STAT\_BALANCE\_DD | Maximum balance drawdown in monetary terms. In the process of trading, a balance may have numerous drawdowns; here the largest value is taken | double |
| STAT\_BALANCEDD\_PERCENT | Balance drawdown as a percentage that was recorded at the moment of the maximum balance drawdown in monetary terms (STAT\_BALANCE\_DD). | double |
| STAT\_BALANCE\_DDREL\_PERCENT | Maximum balance drawdown as a percentage. In the process of trading, a balance may have numerous drawdowns, for each of which the relative drawdown value in percents is calculated. The greatest value is returned | double |
| STAT\_BALANCE\_DD\_RELATIVE | Balance drawdown in monetary terms that was recorded at the moment of the maximum balance drawdown as a percentage (STAT\_BALANCE\_DDREL\_PERCENT). | double |
| STAT\_EQUITYMIN | Minimum equity value | double |
| STAT\_EQUITY\_DD | Maximum equity drawdown in monetary terms. In the process of trading, numerous drawdowns may appear on the equity; here the largest value is taken | double |
| STAT\_EQUITYDD\_PERCENT | Drawdown in percent that was recorded at the moment of the maximum equity drawdown in monetary terms (STAT\_EQUITY\_DD). | double |
| STAT\_EQUITY\_DDREL\_PERCENT | Maximum equity drawdown as a percentage. In the process of trading, an equity may have numerous drawdowns, for each of which the relative drawdown value in percents is calculated. The greatest value is returned | double |
| STAT\_EQUITY\_DD\_RELATIVE | Equity drawdown in monetary terms that was recorded at the moment of the maximum equity drawdown in percent (STAT\_EQUITY\_DDREL\_PERCENT). | double |
| STAT\_EXPECTED\_PAYOFF | Expected payoff | double |
| STAT\_PROFIT\_FACTOR | Profit factor, equal to  the ratio of STAT\_GROSS\_PROFIT/STAT\_GROSS\_LOSS. If STAT\_GROSS\_LOSS=0, the profit factor is equal to [DBL\_MAX](../../Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) | double |
| STAT\_RECOVERY\_FACTOR | Recovery factor, equal to the ratio of STAT\_PROFIT/STAT\_BALANCE\_DD | double |
| STAT\_SHARPE\_RATIO | Sharpe ratio | double |
| STAT\_MIN\_MARGINLEVEL | Minimum value of the margin level | double |
| STAT\_CUSTOM\_ONTESTER | The value of the calculated custom optimization criterion returned by the [OnTester()](../../../Event-Handling/OnTester/OnTester.md) function | double |
| STAT\_DEALS | The number of deals | int |
| STAT\_TRADES | The number of trades | int |
| STAT\_PROFIT\_TRADES | Profitable trades | int |
| STAT\_LOSS\_TRADES | Losing trades | int |
| STAT\_SHORT\_TRADES | Short trades | int |
| STAT\_LONG\_TRADES | Long trades | int |
| STAT\_PROFIT\_SHORTTRADES | Profitable short trades | int |
| STAT\_PROFIT\_LONGTRADES | Profitable long trades | int |
| STAT\_PROFITTRADES\_AVGCON | Average length of a profitable series of trades | int |
| STAT\_LOSSTRADES\_AVGCON | Average length of a losing series of trades | int |
| STAT\_COMPLEX\_CRITERION | Complex [optimization criterion](https://www.metatrader5.com/en/terminal/help/algotrading/optimization_types#criterion) |  |
