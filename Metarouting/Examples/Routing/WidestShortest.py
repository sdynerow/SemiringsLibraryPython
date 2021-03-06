#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 - Seweryn Dynerowicz, FUNDP.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# imitations under the License.

from Metarouting.Algebra.RoutingMatrix import *

from Metarouting.Policy.Routing.ShortestR import *
from Metarouting.Policy.Routing.WidestShortest import *

from Metarouting.Algorithms.APSP import *
from Metarouting.Algorithms.Bellman import *
from Metarouting.Algorithms.Dijkstra import *

I = ShortestR.zeroElt
m = RoutingMatrix(5, 5, [ (0, I), (5, 1), (0, I), (0, I), (0, I)
                        , (0, I), (0, I), (0, I), (0, I), (0, I)
                        , (0, I), (5, 4), (0, I), (5, 1), (0, I)
                        , (5, 1), (0, I), (0, I), (0, I), (10, 1)
                        , (10, 5), (0, I), (5, 1), (0, I), (0, I)], cast=WidestShortest)

print "Input matrix:\n" + str(m) + "\n"


llo = m.leftLocalOptimum2()
rlo = m.rightLocalOptimum()

print str(m.rightLocalOptimum()) + "\n"
print str(m.rightLocalOptimum2())

#print "LLO:\n" + str(llo) + "\n"
#print "RLO:\n" + str(rlo) + "\n"

solveAPSP(dijkstraR, "Dijkstra R ( D)", m)
print
solveAPSP(dijkstraNDR, "Dijkstra R (ND)", m)
print
solveAPSP(dijkstraNDL, "Dijkstra L (ND)", m)
