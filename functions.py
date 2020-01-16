"""
Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

For example, Jay ran like a fool! or Chantelle slid down the slide!.
"""

def run(kid_name):
  print(f"{kid_name} ran")
def swing(kid_name):
  print(f"{kid_name} swung")
def slide(kid_name):
  print(f"{kid_name} slid")
def hide_and_seek(kid_name):
  print(f"{kid_name} hid and sought")

run("Bob")
swing("Bob")
slide("Bob")
hide_and_seek("Bob")


"""The following lists of children should be iterated, and the names sent to the appropriate functions. """

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

for kid in running_kids:
  run(kid)
for kid in swinging_kids:
  swing(kid)
for kid in sliding_kids:
  swing(kid)
for kid in hiding_kids:
  swing(kid)