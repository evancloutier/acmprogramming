'''
black squares = files to remove
white squares = files to keep



For each black square as your starting point : (O(n))
    start with a box around just that black square
    sort all the other black squares so that the next black square on the list requires the smallest expansion of the square to compute (O(n logn))
        for each black square in this ^ list:(O(n))
            compute the number of moves needed to have all the black squares in the box and all the whites outside (O(n))
            keep track of that
            expand the box to add the next square

O(n^3) overall
'''

import math

row_idx = 0
col_idx = 1

def get_dist(point1, point2):
    x_2 = (point1[0] - point2[0]) ** 2
    y_2 = (point1[1] - point2[1]) ** 2
    dist = math.sqrt(x_2 + y_2)
    return dist

def get_distances_from_point(point, delete_locations):
    sorted_distances = sorted(delete_locations, key=lambda x: get_dist(x, point))
    return sorted_distances

def location_string_to_list(str_arr):
    arr = str_arr.split(" ")
    ret_arr = []

    for i in range(0, len(arr), 2):
        ret_arr.append([int(arr[i]) + 7, int(arr[i + 1]) + 4])

    return ret_arr

def compute_num_moves(left, right, top, bottom, delete_locations, remain_locations):
    num_moves = 0
    for file_coords in delete_locations:
        if file_coords[col_idx] > right or file_coords[col_idx] < left or file_coords[row_idx] < bottom or file_coords[row_idx] > top:
            num_moves += 1
    for file_coords in remain_locations:
        if file_coords[col_idx] <= right and file_coords[col_idx] >= left and file_coords[row_idx] >= bottom and file_coords[row_idx] <= top:
            num_moves += 1

    return num_moves

def delete_this(pixel_rows, pixel_cols, num_delete, num_remain, delete_locations, remain_locations):
    min_num_moves = float("inf")
    for file_to_delete in delete_locations:
        sorted_distances = get_distances_from_point(file_to_delete, delete_locations)
        for idx, next_file in enumerate(sorted_distances):
            if idx == 0:
                left,right = [file_to_delete[col_idx],file_to_delete[col_idx]]
                top,bottom = [file_to_delete[row_idx], file_to_delete[row_idx]]
            else:
                left = min(left, next_file[col_idx])
                bottom = min(bottom, next_file[row_idx])
                right = max(right, next_file[col_idx])
                top = max(top, next_file[row_idx])
            num_moves = compute_num_moves(left, right, top, bottom, delete_locations, remain_locations)
            min_num_moves = min(num_moves, min_num_moves)

    return min_num_moves

delete_locations = "75 5 25 20 50 35"
remain_locations = "50 5 25 35"
pixel_rows = 80
pixel_cols = 50
num_delete = 3
num_remain = 2
delete_locations = location_string_to_list(delete_locations)
remain_locations = location_string_to_list(remain_locations)


print "min number of moves: " + str(delete_this(pixel_rows, pixel_cols, num_delete, num_remain, delete_locations, remain_locations))
