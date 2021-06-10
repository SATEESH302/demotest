#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mathlib


def test_calc_addition():

        event = {"Number1": 2, "Number2": 4}


        actual_output = lambda_handler(event, '')

        assert actual_output == 6



def test_calc_substraction():

    output = mathlib.calc_substraction(2, 4)


def test_calc_multiply():

    output = mathlib.calc_multiply(2, 4)


def test_calc_mult():

    output = mathlib.calc_multiply(0, 4)





