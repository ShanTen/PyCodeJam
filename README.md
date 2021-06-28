# PyCodeJam
# *Incorrect* Solution for the Python Summer Code Jam 

It mutates, pads unevenly and dies on multiple object calls of the same name but it's 40 minutes of **solid** *honest work* work. <3

```
from makeTable import make_table

table1 = make_table(
    rows=[
        ["Lemon", 18_3285, "Owner"],
        ["Sebastiaan", 18_3285.1, "Owner"],
        ["KutieKatj", 15_000, "Admin"],
        ["Jake", "MoreThanU", "Helper"],
        ["Joe", -12, "Idk Tbh"]
    ],
    labels=["User", "Messages", "Role"]
)

table2 = make_table(
    rows=[
        ["apple", 5, 70, "Red"],
        ["banana", 3, 5, "Yellow"],
        ["cherry", 7, 31, "Red"],
    ],
    labels=["Fruit", "Tastiness", "Sweetness", "Colour"],
    centered=True
)

table3 = make_table(
    rows=[
        ["Pneumonoultramicroscopicsilicovolcanoconiosis"],
        ["Hippopotomonstrosesquippedaliophobia"],
        ["Supercalifragilisticexpialidocious"],
        ["Pseudopseudohypoparathyroidism"],
        ["Floccinaucinihilipilification"],
        ["Antidisestablishmentarianism"],
        ["."]
    ],
    labels=["My Favourite Long Words"],
    centered=True
)

print(table1)
print(table2)
print(table3)
```
Output:

![](https://media.discordapp.net/attachments/823773596307947550/856788964861411328/unknown.png?width=709&height=670)
