def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))
'''When it encounters an assert statement, Python evaluates the accompanying
expression, which is hopefully true. If the expression is false, Python
raises an AssertionError exception.

The syntax for assert is −

assert Expression[, Arguments]'''
