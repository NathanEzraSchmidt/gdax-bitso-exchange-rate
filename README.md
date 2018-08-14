# gdax-bitso-exchange-rate
for each currency common to both exchanges, prints the bitso MXN price, gdax USD price, and the first of those divided by the second
```
>>> from compare_gdax_bitso import *
>>> init_all_tickers()
>>> compare_bitso_gdax()
BTC 	 116238.5 	 6015.94 	 19.32175187917433

ETH 	 4910.29 	 260.01 	 18.88500442290681

LTC 	 955.21 	 51.1 	 18.692954990215263

BCH 	 9310.0 	 483.79 	 19.243886810392937

>>> compare_bitso_gdax()
BTC 	 116238.5 	 6015.95 	 19.32171976163366

ETH 	 4910.29 	 260.66 	 18.837911455535945

LTC 	 955.21 	 51.1 	 18.692954990215263

BCH 	 9310.0 	 483.79 	 19.243886810392937

>>> compare_bitso_gdax()
BTC 	 116238.5 	 6015.95 	 19.32171976163366

ETH 	 4910.29 	 260.66 	 18.837911455535945

LTC 	 955.21 	 51.1 	 18.692954990215263

BCH 	 9310.0 	 483.71 	 19.247069525128694
