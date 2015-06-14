
def triangle_type(side_list):
    hyp = max(side_list)
    hyp_square = hyp ** 2
    side_sum = 0
    for side in side_list:    
        if side != hyp:
            side_sum += side ** 2
    if side_sum == hyp_square:
        return 'R'
    elif side_sum < hyp_square:
        return 'O'
    else:
        return 'A'
        
    
with open('test.txt') as data_file:
    N = int(data_file.readline())
    for dummy_idx in range(N):
        tri = map(int, data_file.readline().split())
        print triangle_type(tri),