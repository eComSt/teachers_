from pprint import pprint
pascal_triangle = [[1],
                    [1,1],
                    [1,2,1],
                    [1,3,3,1],
                    [1,4,6,4,1],
                    [1,5,10,10,5,1],
                    ]
pascal_triangle_dict = {}
for num,line in enumerate(pascal_triangle):
    pascal_triangle_dict[num] = line
pprint(pascal_triangle_dict)

for num in range(len(pascal_triangle)):
    pascal_triangle_dict[num] = pascal_triangle[num]
pprint(pascal_triangle_dict)