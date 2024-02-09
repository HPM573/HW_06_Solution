import InputData as D
from deampy.random_variates import Exponential


class Parameters:
    # class to contain the parameters of the urgent care model
    def __init__(self):
        self.hoursOpen = D.HOURS_OPEN
        self.nPCPs = D.N_PCP
        self.arrivalTimeDist = Exponential(scale=D.MEAN_ARRIVAL_TIME)
        self.examTimeDist = Exponential(scale=D.MEAN_EXAM_DURATION)
        self.probDepression = D.PROB_DEPRESSION
        self.mentalHealthConsultDist = Exponential(scale=D.MEAN_MH_CONSULT)
