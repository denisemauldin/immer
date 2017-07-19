import csv

varieties = {
        'M': 'manchuria',
        'S': 'svansota',
        'V': 'velvet',
        'T': 'trebi',
        'P': 'peatland'
}

sites = {
    'GR': 'Grand Rapids',
    'D': 'Duluth',
    'UF': 'University Farm',
    'M': 'Morris',
    'C': 'Crookston',
    'W': 'Waseca'
}

# print legends

# we're specifically calling this the same as the variety key below
# so that a more specific XPATH must be used to retrieve the two kinds of data
print('<div id="legends">')
print('{:>4s}<div id="variety-legend">'.format(' '))
for variety in varieties:
    print('{:>8s}<div id="variety">{} = {}</div>'.format('', variety, varieties[variety]))

print('{:>4s}</div>'.format(''))
print('{:>4s}<div id="site-legend">'.format(''))
for site in sites:
    print('{:>8s}<div id="site">{} = {}</div>'.format('', site, sites[site]))

print('{:>4s}</div>'.format(''))
print('</div>')

# open the csv file
with open("immer.csv") as csvfile:
    # figure out if there's a header
    has_header = csv.Sniffer().has_header(csvfile.read(1024))
    # go back to the top of the file
    csvfile.seek(0)
    #create a parser for the csv file
    reader = csv.reader(csvfile, delimiter=",")
    # skip the header line if there is one
    if has_header:
        next(reader)
    # go through each row of the file
    for row in reader:
      print('<div id="barley-data">\n    <div id="site">{}</div>\n    <div id="site-name">{}</div>\n    <div id="variety">{}</div>\n    <div id="variety-name">{}</div>\n    <div id="Y1">{}</div>\n    <div id="Y2">{}</div>\n</div>'.format(row[1], sites[row[1]], row[2], varieties[row[2]], row[3], row[4]))
