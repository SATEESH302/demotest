
import os
import jwt


def lambda_handler(event, context):
   number1 = event['Number1']
   number2 = event['Number2']
   sum = number1 + number2

   return sum



