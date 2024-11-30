import re

file = []
with open('input.txt', 'r') as f:
    for line in f:
        file.append(line[:-1])

class Bag:
    def __init__(self, colour, content):
        self.colour = colour
        self.content = content
        self.count = 0
    def __str__(self):
        return f"Bag with colour {self.colour} and content {self.content}"
    def __repr__(self):
        return f"{self.colour}{self.content}"


bag_list = []
for rule in file:
    # Separate the outer bag from the contained bags
    outer_bag, contained_bags = rule.split(" bags contain ")

    # Parse the contained bags
    contained = re.findall(r'(\d+) (\w+ \w+) bag', contained_bags)

    # Create a Bag object for each outer bag
    bag_list.append(Bag(outer_bag,{bag_color: int(quantity) for quantity, bag_color in contained}))

def bag_check(bags):
    unchecked = ["shiny gold"]  # possible bags, where other bags weren't checked for if they contain this one
    checked = [] # possible bags, which have already been checked (don't add these colours again)
    while len(unchecked): # when this list is empty, every needed check has been done
        for check_bag in unchecked:
            for bag in bags:
                if check_bag in list(bag.content.keys()) and bag not in (unchecked + checked): # stops endless loop
                    unchecked.append(bag.colour) # add colour to the bags to be checked
            checked.append(check_bag) # move colour to checked
            unchecked.remove(check_bag) # from unchecked
    return (f"All bags that can contain a shiny golden bag are: {set(checked[1:])}"
            f"\nThat are: {len(set(checked[1:]))} bags")


def bag_count(bags):
    unchecked = [Bag("schmiera", {"shiny gold": 1})]
    checked = []
    while len(unchecked):
        for bag in unchecked:
            for content in bag.content:

                print(bag.colour)
                print(content)
            unchecked.remove(bag)

print(bag_check(bag_list))
print(bag_count(bag_list))