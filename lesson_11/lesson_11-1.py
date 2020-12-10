win = int(input("Win: "))
draw = int(input("Draw: "))
loss = int(input("loss: "))
def count_points(win, draw, loss):
    any_sum =  win * 3 + draw * 1 + loss * 04
    return any_sum
print('count_points (win, draw, loss) -> ', count_points(win, draw, loss))



