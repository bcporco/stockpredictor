# Goals #
  1. Collect closing data for one of the major investing indexes (S&P500, NASDAQ, or DOW) from the past 5 years.
  1. Collect stock analysts picks from the same time period on a set of stocks or market sectors
    1. This may need to change. Not only is it hard to get this data (for free in minable amounts), but it's accuracy may make trying to use it to predict stock direction very difficult.
  1. Generate statistics on the profitability of each analyst
  1. Report findings
  1. Use findings to identify market opportunity

# Stage One #
  * Planning
    * Find out where market data can be found/mined from
      * **http://www.business-spreadsheets.com/forum.asp?t=40
    * Find out where analysts buy/hold/sell calls can be found/mined from
      *** This may be harder to get a hold of than I thought, and may or may not be free
      * **Putting this off for the time being, will focus on getting the stock data portion done and will come back to this
    * Identify the most important information needed to generate statistics
      *** Useful Stock Data
        *  52 week high/low
        *  P/E ratio
        *  Dividend / Yield
        *  Shares
        *  % institute owned
        *  Mrkt Cap
        *  EPS
        *  price
        *  Date and time all of above data was gathered at
    * Determine what information is useful to report
      * **Will put off till after data is gathered**

# Stage Two #
  * Planning
    * Design program to mine market data
      * **Basic brute force version designed. Many, many possible improvements but aiming for  "release early, release often".
    * Design program to mine analyst data
      *** Putting off until source can be found
  * Coding
    * Create schema for market data
      * **Basic schema done, need to figure out table type, keys, etc.
    * Create schema for analyst data
      *** Putting off until source can be found
    * Create schema for reports
      * **Putting off**

# Stage Three #
  * Coding
    * Create program capable of pulling market data
    * Create program capable of pulling analyst data

# Stage Four #
  * Planning
    * Review results of stage three and determine if any schema or design changes should be made
  * Coding
    * Create program to use results of stage three plus any corrections to populate the market and analyst tables

# Stage Five #
  * Planning
    * Review statistics to make sure the information being collected is useful
  * Coding
    * Create program to generate statistics with data collected in stage four.

# Stage Six #
  * Planning
    * Review statistics to make sure the information being collected is useful
    * Review how that information should be reported
  * Coding
    * Create program to generate reports on past performance from statistics from stage five.

# Stage Seven #
  * Coding
    * Add functionality in report program to identify potential leads using current analysts singals

# Stage Eight #
'''PROFIT!'''