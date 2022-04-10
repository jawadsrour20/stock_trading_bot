import numpy as np

class BotUtils():
    '''
    
        if the slope is a +ve value --> increasing trend

        if the slope is a -ve value --> decreasing trend

        if the slope is a zero value --> No trend
    
    '''
    @staticmethod
    def get_trend_line(index, data, order = 1):
        coeffs = np.polyfit(index, list(data), order)
        slope = coeffs[-2]
        return float(slope)