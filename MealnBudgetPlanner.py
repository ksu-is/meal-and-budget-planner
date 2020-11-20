import itertools
import yaml

docs = yaml.load(open("recipes.yml", "r"))
options = dict((i, (name, values)) for i, (name, values) in enumerate(docs.items(), 1))

print "What would you like to meal prep?"
print "Here are the options:"
for option, (name, ingredients) in iter(sorted(options.iteritems())):
    print str(option) + ". " + str(name)

choose = raw_input("> ")
