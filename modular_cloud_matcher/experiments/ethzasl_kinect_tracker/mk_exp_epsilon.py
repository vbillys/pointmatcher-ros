#!/usr/bin/env python

from Numeric import *


cstParams = 'startupDropCount=0 readingDataPointsFilterCount=2 readingDataPointsFilter/0/name=ClampOnAxisThresholdDataPointsFilter readingDataPointsFilter/0/threshold=2.5 readingDataPointsFilter/0/dim=2 readingDataPointsFilter/1/name=FixstepSamplingDataPointsFilter readingDataPointsFilter/1/startStep=17 readingDataPointsFilter/1/endStep=17 readingDataPointsFilter/1/stepMult=1 readingStepDataPointsFilterCount=0 keyframeDataPointsFilterCount=2 keyframeDataPointsFilter/0/name=ClampOnAxisThresholdDataPointsFilter keyframeDataPointsFilter/0/threshold=2.5 keyframeDataPointsFilter/0/dim=2 keyframeDataPointsFilter/1/name=SamplingSurfaceNormalDataPointsFilter  matcher/name=KDTreeMatcher transformationCheckerCount=3 transformationCheckers/0/name=ErrorTransformationChecker transformationCheckers/0/minRotErrorDelta=0.001 transformationCheckers/0/minTransErrorDelta=0.01 transformationCheckers/0/tail=4 transformationCheckers/1/name=CounterTransformationChecker transformationCheckers/1/maxIterationCount=40 transformationCheckers/2/name=BoundTransformationChecker transformationCheckers/2/maxRotationNorm=1 transformationCheckers/2/maxTranslationNorm=0.5 featureOutlierFilterCount=2 featureOutlierFilters/0/name=MaxDistOutlierFilter featureOutlierFilters/0/maxDist=0.2 featureOutlierFilters/1/name=MedianDistOutlierFilter featureOutlierFilters/1/factor=4 inspector/name=Inspector errorMinimizer/name=PointToPlaneErrorMinimizer ratioToSwitchKeyframe=0.7'

for epsilon in arange(0,3,0.2):
	for k in [4, 11, 30]:
		localParams = 'matcher/epsilon=' + str(math.pow(epsilon,4)) + ' '
		localParams +='keyframeDataPointsFilter/1/k=' + str(k)
		print(cstParams + ' ' + localParams)