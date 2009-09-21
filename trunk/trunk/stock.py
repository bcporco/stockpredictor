'''stock.py: Module to identify a stock and its associated data

Exports:
    Stock(symbol, index)
        [ (symbol is the shorthand character representation for the stock) and
          (index is the market index used to track the stock, if any) ->
              returns an instance of Stock]
'''

class Stock:
	"""An instance of a stock for a particular company and index
	"""
	def __init__(self, symbol, index, type):
		"""Constructor for Stock.
		"""
		if !(isinstance(symbol,str) && 
		(isinstance(index,str) || isnull(index)) &&
		(isinstance(type,str) || isnull(type)) :
			raise InstanceError, ( "Both symbol and index must be of string type" )
		else:
			self.symbol = symbol
			self.index = index
			self.type = type