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

from Metarouting.Algebra.Semiring import *

class Bottleneck(Semiring):
    S0 = 0
    S1 = 1
    S2 = 2
    S3 = 3
    S4 = 4
    SI = 5

    def __add__(self, other):
        return Bottleneck(max(self.elt, other.elt));

    def __mul__(self, other):
        return Bottleneck(min(self.elt, other.elt));

    def __le__(self, other):
        return (self.elt >= other.elt)

    def __repr__(self):
        if(self.elt == 5):
            return "I"
        else:
            return self.elt.__repr__()

    @staticmethod
    def zero():
        return Bottleneck(0)

    @staticmethod
    def unit():
        return Bottleneck(Bottleneck.SI)

    @staticmethod
    def groundSet():
        return map(Bottleneck, range(6))