import pandas as pd
import numpy as np
import norgatedata

# priceadjust = norgatedata.StockPriceAdjustmentType.NONE
# priceadjust = norgatedata.StockPriceAdjustmentType.CAPITAL
# priceadjust = norgatedata.StockPriceAdjustmentType.CAPITALSPECIAL
# priceadjust = norgatedata.StockPriceAdjustmentType.TOTALRETURN

# padding_setting = norgatedata.PaddingType.NONE 
# padding_setting = norgatedata.PaddingType.ALLMARKETDAYS
# padding_setting = norgatedata.PaddingType.ALLWEEKDAYS
# padding_setting = norgatedata.PaddingType.ALLCALENDARDAYS


# for fetching historical price time series of a ticker
def hist_sym(sym,start):
        #sym: symbol or ticker
        #start: start date 'yyyy-mm-dd' format
	priceadjust = norgatedata.StockPriceAdjustmentType.TOTALRETURN
	padding_setting = norgatedata.PaddingType.NONE 
	timeseriesformat = 'pandas-dataframe'
	start_date = pd.Timestamp(start)

	try:
		dff = norgatedata.price_timeseries(sym,stock_price_adjustment_setting = priceadjust,padding_setting = padding_setting,start_date = start_date,format=timeseriesformat)
		return(dff)

	except:
		return('no symbol')

	

# for fetching historical price time series of a ticker with end dates
def hist_sym_end(sym,start,end):
        #sym: symbol or ticker
        #start: start date in 'yyyy-mm-dd' format
        #end: end date in 'yyyy-mm-dd' format
	priceadjust = norgatedata.StockPriceAdjustmentType.TOTALRETURN
	padding_setting = norgatedata.PaddingType.NONE 
	timeseriesformat = 'pandas-dataframe'
	start_date = pd.Timestamp(start)
	end_date = pd.Timestamp(end)

	try:
		dff = norgatedata.price_timeseries(sym,stock_price_adjustment_setting = priceadjust,padding_setting = padding_setting,start_date = start_date,end_date = end_date,format=timeseriesformat)
		return(dff)

	except:
		return('no symbol')

	



