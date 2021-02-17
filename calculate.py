from math import sqrt
import json

stats = ["type", "atk%", "crate%", "cdam%", "hp%", "def%", "spd", "acc"]
types = {"atk%": 15, "crate%": 12, "cdam%": 20, "hp%": 15, "def%": 15, "spd": 11, "acc": 40, "prec": (5, 40)}
item_set = [[], [], [], [], [], []]
set_list = []
target_stats = {
    "atkacc": {"atk%": (100, 7), "crate%": (50, 5), "cdam%": (50, 4), "hp%": (6, 1), "def%": (6, 2), "spd": (60, 6), "acc": (60, 3)},
    "defacc": {"atk%": (0, 1), "crate%": (40, 3), "cdam%": (35, 2), "hp%": (100, 6), "def%": (100, 7), "spd": (60, 5), "acc": (60, 4)},
    "sup": {"atk%": (0, 4), "crate%": (0, 3), "cdam%": (0, 2), "hp%": (100, 5), "def%": (100, 6), "spd": (60, 7), "acc": (0, 1)},
    "def": {"atk%": (0, 1), "crate%": (50, 4), "cdam%": (50, 3), "hp%": (120, 6), "def%": (120, 7), "spd": (60, 5), "acc": (0, 2)}
    }

    
def save_data():
    with open("items.txt", mode="w") as file:
        file.write(json.dumps(item_set))
        file.write("\n")
        file.write(json.dumps(set_list))
        file.write("\n")
        file.write(json.dumps(list(target_stats)))


def load_data():
    with open("items.txt", mode="r") as file:
        global item_set
        global set_list
        global target_stats
        lines = file.readlines()
        item_set = json.loads(lines[0])
        set_list = json.loads(lines[1])
        target_stats = json.loads(lines[2])[1:-1] 


def add_item(slot_number):
    stat_vals = [input(f"{stat}: ") for stat in stats]
    int(stat_vals[1:])
    item = {key: value for key, value in zip(stats, stat_vals)}
    item_set[slot_number].append(item)
    save_data()
    print(item_set)
    print(item_set[slot_number])


def set_stats(set_id, *args):
    new_set = {}
    args = [arg for arg in args]
    for slot, index in zip(set_id, args):
        for key, value in slot[index].items():
            if key not in new_set:
                new_set.update({key: value})
            else:
                new_set[key] += value
    set_list.append(new_set)
    save_data()

    
def set_rating(set_id, *flags):
    flags = [flag for flag in flags]
    rating = 0
    target = target_stats["".join(flags)]
    for el, ref in zip(set_id.keys(), target.keys()):
        elkey = set_id[el]
        refkey = target[ref][0]
        greater = refkey if refkey >= elkey else elkey
        lesser = refkey if refkey < elkey else elkey
        rating += (1 - ((greater - lesser) / refkey) ** (2 + 0.1 * target[ref][1]))
    rating = rating / len(target)
    return rating

def add_target(name):
    print(stats)
    stat_vals = [(int(input(f"{stat}: ")), int(input(f"{stat} rank (1-9, 1 is smallest): "))) for stat in stats]
    target = {key: value for key, value in zip(stats, stat_vals)}
    target_stats.update({name: target})
    save_data()
    print(target_stats)

def main():
    load_data()
    print(target_stats)

    # add_item(0)
    # set_stats(test_set, 0, 0, 0, 0, 0, 0)
    # set_stats(test_set2, 0, 0, 0, 0, 0, 0)
    # set_stats(test_set3, 0, 0, 0, 0, 0, 0)
    # set_stats(test_set4, 0, 0, 0, 0, 0, 0)
    # set_stats(test_set5, 0, 0, 0, 0, 0, 0)
    # set_stats(ref_set, 0, 0, 0, 0, 0, 0)
    # a = set_rating(set_list[0], "atk", "acc")
    # b = set_rating(set_list[1], "atk", "acc")
    # c = set_rating(set_list[2], "atk", "acc")
    # d = set_rating(set_list[3], "atk", "acc")
    # e = set_rating(set_list[4], "atk", "acc")
    # f = set_rating(set_list[5], "atk", "acc")
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    # print(e)
    # print(f)
    # add_target("special")
    # print(item_set)
    # print(set_list)
    # print(target_stats)


if __name__ == "__main__":
    main()

        