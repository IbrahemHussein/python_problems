def total_faces_polyedrons():
    num = int(input())
    count = 0
    for _ in range(num):
        shape = input().lower()
        if shape == 'tetrahedron':
            count += 4
        elif shape == 'cube':
            count += 6
        elif shape == 'octahedron':
            count += 8
        elif shape == 'dodecahedron':
            count += 12
        else:
            count += 20
    return count


print(total_faces_polyedrons())
