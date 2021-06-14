#!/usr/bin/env python
# coding: utf-8

# In[ ]:



from lambdas.mathlib import lambda_handler

def test_calc_addition():

        event = {"Number1": 2, "Number2": 4}


        actual_output = lambda_handler(event, '')

        assert actual_output == 6








