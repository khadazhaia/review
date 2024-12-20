from main import remove_domain

print("remove_domain(['test@gmail.com', 'helloworld@yahoo.com'])",
      remove_domain(['test@gmail.com', 'helloworld@yahoo.com']) == ['test', 'helloworld'])

print("remove_domain(['test@gmail.com'])",
      remove_domain(['test@gmail.com']) == ['test'])

print("remove_domain(['1@yahoo.com'])",
      remove_domain(['1@yahoo.com']) == ['1'])

print("remove_domain(['test'])",
      remove_domain(['test']) == ['test'])

print("remove_domain([''])",
      remove_domain(['']) == [''])

print("remove_domain([])",
      remove_domain([]) == [])

print("remove_domain([1])",
      remove_domain([1]) == -1)

print("remove_domain([None, None])",
      remove_domain([None, None]) == -1)
