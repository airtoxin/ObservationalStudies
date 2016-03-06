#!/usr/bin/env python
# -*- conding: utf-8 -*-

from __future__ import absolute_import

from observational_studies import (
    CaseControl,
    Cohort,
    CrossSectional
)

def test_class():
    case_control = CaseControl()
    cohort = Cohort()
    cross_sectional = CrossSectional()

    assert type(case_control).__name__ == "CaseControl"
    assert type(cohort).__name__ == "Cohort"
    assert type(cross_sectional).__name__ == "CrossSectional"
