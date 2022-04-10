import numpy as np

class BotUtils():

    @staticmethod
    def get_trend_line(index, data, order = 1):
        coeffs = np.polyfit(index, list(data), order)
        slope = coeffs[-2]
        return float(slope)