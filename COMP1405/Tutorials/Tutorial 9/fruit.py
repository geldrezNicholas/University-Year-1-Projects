fruits = ['apple','tomato','banana','tomato','apple','orange','avocado',
          'banana','apple','tomato','grape','orange','avocado']

def count_fruit(fruit_list):
    fruit_count = {}
    for fruit in fruit_list:
        if fruit not in fruit_count:
            fruit_count[fruit] = 1
        else:
            fruit_count[fruit] += 1
    return fruit_count

def main():
    print(count_fruit(fruits))

main()