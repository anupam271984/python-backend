# index in list
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "white"]
        #[  0,       1,        2,        3,      4,       5,        6,        7,       8  ]# positive index
        #[ -9,      -8,       -7,       -6,     -5,      -4,       -3,       -2,      -1  ]# Negaaive index

print(colors[3:7])	#using positive indexes will start from 3 but end before 7 
print(colors[-7:-2])	#using negative indexes'
'''Starts at index -7 ("yellow").
   Stops before index -2 ("black").
    Result: ['yellow', 'green', 'blue', 'indigo', 'violet']'''

print(colors[4:])	#using positive indexes
'''Starts at index 4 ("blue") and grabs everything after it.
    Result: ['blue', 'indigo', 'violet', 'black', 'white']'''

print(colors[-4:])	#using negative indexes
'''Starts at the 4th item from the end ("indigo") and goes to the end.
   Result: ['indigo', 'violet', 'black', 'white']'''

print(colors[:6])	#using positive indexes
'''Starts at the beginning and stops before index 6 ("violet").
   Result: ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']'''

print(colors[:-3])	#using negative indexes
'''Starts at the beginning and stops before the 3rd item from the end ("violet").
   Result: ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']'''

print(colors[::2])		#using positive indexes
'''Starts at the beginning, goes to the end, but only takes every 2nd item.
   Result: ['red', 'yellow', 'blue', 'violet', 'white']'''

print(colors[-8:-1:2])	#using negative indexes
'''Start: -8 ("orange").
   Stop: Before -1 ("white").
   Step: Jump by 2.
   Result: ['orange', 'green', 'indigo', 'black']'''

print(colors[1:8:3])
'''The Breakdown
    Start (1): "orange"
    Stop (8): Before "white"
    Step (3): Jump 3 positions each time.
The Selection Process
    Start at index 1: orange
    Jump 3 steps (1 + 3 = 4): blue
    Jump 3 steps (4 + 3 = 7): black
    Next jump (7 + 3 = 10): Out of range (stops here).'''

print(colors[1:8:-3])
'''The Breakdown for colors[8:1:-3]
    Start (8): "white"
    Stop (1): Before "orange" (so it stops at index 2)
    Step (-3): Jump backward 3 positions each time.
The Selection Process
    Start at index 8: white
    Jump back 3 steps (8 - 3 = 5): indigo
    Jump back 3 steps (5 - 3 = 2): yellow
    Next jump (2 - 3 = -1): This would be index 1 ("orange"), but since we stop before index 1, it is excluded.
    ['white', 'indigo', 'yellow']'''

print(colors[::-1]) 
# reverse the entire list

del colors[1:3]
print(f" new color list {colors}")

colors.pop(2)
print(f" new color list {colors}")