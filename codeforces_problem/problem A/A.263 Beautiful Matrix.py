def beautiful_matrix():
    
    #ToDO: first we need to input the matrix
    matrix=[list(map(int,input().split())) for i in range(5)]
    print(matrix)
    #ToDO: we need to find the location of the i in the matrix
    for i in range(5):
        for j in range (5):
            if matrix[i][j]==1:
                x,y=i,j
    print(f'x: {x} and y: {y}')
    #ToDo: we need to determine the move need to make beautiful matrix
    moves=abs(x-2)+abs(y-2)
    print(moves)
    return


if __name__ == "__main__":
    beautiful_matrix()