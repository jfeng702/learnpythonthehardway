cities = {
    'CA': 'San Francisco',
    'NY': 'New York',
    'TX': 'Austin'
}

states = {
    'California': 'CA',
    'Texas': 'TX',
    'New York': 'New York'
}

print '-' * 10
print "TX State has: ", cities['TX']
print "California has: ", cities[states['California']]
for abbrev, city in cities.items():
    print "%s contains %s" % (abbrev, city)
