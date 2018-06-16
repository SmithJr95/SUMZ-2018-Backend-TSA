from enum import Enum


class JsonRequestKeys(Enum):
    TimeSeries = 'time_series'
    PredictionSteps = 'pred_steps'
    NumberOfSamples = 'num_samples'
    TimeSeriesID = 'id'
    TimeSeriesValues = 'values'
