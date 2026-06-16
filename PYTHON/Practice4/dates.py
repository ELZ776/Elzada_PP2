# Import datetime module
import datetime

x = datetime.datetime.now()

print(x)

# Import datetime module
import datetime

x = datetime.datetime.now()

print(x.year)

print(x.strftime("%A"))

# Import datetime module
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# Import datetime module
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# Import datetime module
import datetime

x = datetime.datetime(2026, 6, 16, 20, 8, 34)

print(x.strftime("%A"))
print(x.strftime("%d"))
print(x.strftime("%B"))
print(x.strftime("%Y"))
print(x.strftime("%H:%M:%S"))

# Import datetime module
import datetime

x = datetime.datetime(2026, 6, 16, 20, 8, 34)

print(x.strftime("%d/%m/%Y"))
print(x.strftime("%B %d, %Y"))
print(x.strftime("%A, %B %d"))
print(x.strftime("%H:%M"))