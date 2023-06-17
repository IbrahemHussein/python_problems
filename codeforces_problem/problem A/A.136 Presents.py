def Presents():
    # TODO: first line ask user for the number of member of friends of the party
    num = int(input())
    # TODO: ask for number of gift that members of the party give to anther frinds
    gifts = list(map(int, input().split(' ')))
    # TODO: dict for each member of the party and each gifts
    #this dict will conatain the number of gift to number of receivers like that {giver:receivers}
    receivers = {}
    for i in range(num):
        
        receiver = i + 1
        giver = gifts[i]
        receivers[giver] = receiver
    #TODO: print each received gift for each  giver
    for i in range(1, num + 1):
        print(receivers[i], end=' ')


Presents()
