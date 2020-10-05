from django.test import TestCase

# Create your tests here.
import random
ar = [20,30,40,50,60,70]
From = random.randint(1,3)
To = random.randint(2,4)
for k in range(From,To + 1):
    print(ar[k],end='#')