'''
if background image not display and code not run in your device,please add complete path of image 
that i uploaded along with code zip in scr.bgpic() in line 167
Thank you
'''
import turtle,random,os
count=0
moves_list=[]
def start():
    global count,board,moves_list,shuffling
    count=0
    moves_list=[]
    tur=turtle.Turtle()
    scr=turtle.Screen()
    counter=turtle.Turtle()
    res=turtle.Turtle()
    counter.speed(0)
    res.speed(0)
    counter.ht()
    counter.pu()
    counter.goto(0,220)
    counter.color("black")
    res.ht()
    res.pu()
    res.goto(-200,220)
    res.color("black")
    res.write("Reset",align="right",font=("Arial",24,"bold"))
    def reset(x,y):
        if -300 <= x <= -100 and 200 <= y <= 240:
            scr.clearscreen()
            start()
    scr.onclick(reset)
    def draw_grid(r, c):
        counter.clear()
        counter.write("Moves taken= " + str(count), align="left", font=("Arial", 24, "bold"))
        scr.tracer(0)
        tur.color("cyan","lightyellow")
        tur.penup()
        tur.goto(-200+c*100,200-r*100)
        tur.pendown()
        tur.begin_fill()
        for i in range(4):
            tur.forward(100)
            tur.right(90)
        tur.end_fill()
        if board[r][c] is not None:
            tur.color("black")
            tur.penup()
            tur.goto(-200+c*100+50,200-r*100-60)
            tur.pendown()
            tur.write(str(board[r][c]),align="center",font=("Arial", 24, "bold"))
        scr.update()
    def win():
        cor = list(range(1,16)) + [None]
        flat = [board[r][c] for r in range(4) for c in range(4)]
        if flat == cor:
            scr.clear()
            tur.hideturtle()
            scr.bgcolor("lightgreen")
            tur.color("black")
            tur.penup()
            tur.goto(0,0)
            tur.write("SOLVED!!!", align="center", font=("Arial", 48, "bold"))
            scr.update()
            c = str(count)
            tur.pu()
            tur.goto(100,-200)
            tur.write("Moves taken= "+str(count),font=("Arial",20,"bold"))
            name=scr.textinput("Victory!","Enter your name:")
            if name:
                score(name,count)
            scores=leaderboard()
            tur.goto(0,-100)
            tur.write("Leaderboard:", align="center", font=("Arial", 24, "bold"))
            y=-140
            for i, (name, moves) in enumerate(scores[:5], start=1):  # top 5
                tur.goto(0, y)
                tur.write(f"{i}. {name} - {moves} moves", align="center", font=("Arial", 18, "normal"))
                y -= 30
            cont = scr.textinput("Game Over","You solved it!! moves taken= "+c+", Play again? (yes/no):")
            if cont and cont.lower() == "yes":
                scr.clearscreen()
                start()
            else:
                replay = scr.textinput("Replay?", "Do you want to watch your replay? (yes/no):")
                if replay and replay.lower() == "yes":
                    play_replay(scr, tur)
                else:
                    turtle.bye()
            return True
    def move_up(replay=False):
        for r in range(4):
            for c in range(4):
                if board[r][c] is None:
                    if r < 3:
                        board[r][c], board[r+1][c] = board[r+1][c], board[r][c]
                        if not shuffling and not replay:
                            global count
                            count += 1
                            moves_list.append("up")
                        draw_grid(r, c)
                        draw_grid(r+1, c)
                        if not shuffling and not replay:
                            win()
                        return
    def move_down(replay=False):
        for r in range(4):
            for c in range(4):
                if board[r][c] is None:
                    if r > 0:
                        board[r][c], board[r-1][c] = board[r-1][c], board[r][c]
                        if not shuffling and not replay:
                            global count
                            count += 1
                            moves_list.append("down")
                        draw_grid(r, c)
                        draw_grid(r-1, c)
                        if not shuffling and not replay:
                            win()
                        return
    def move_right(replay=False):
        for r in range(4):
            for c in range(4):
                if board[r][c] is None:
                    if c > 0:
                        board[r][c], board[r][c-1] = board[r][c-1], board[r][c]
                        if not shuffling and not replay:
                            global count
                            count += 1
                            moves_list.append("right")
                        draw_grid(r, c)
                        draw_grid(r, c-1)
                        if not shuffling and not replay:
                            win()
                        return
    def move_left(replay=False):
        for r in range(4):
            for c in range(4):
                if board[r][c] is None:
                    if c < 3:
                        board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
                        if not shuffling and not replay:
                            global count
                            count += 1
                            moves_list.append("left")
                        draw_grid(r, c)
                        draw_grid(r, c+1)
                        if not shuffling and not replay:
                            win()
                        return
    def score(name,moves):
        with open("leaderboard.txt","a") as f:
            f.write(f"{name},{moves}\n")
    def leaderboard():
        if not os.path.exists("leaderboard.txt"):
            return []
        with open("leaderboard.txt","r") as f:
            scores=[]
            for l in f:
                name,moves=l.strip().split(",")
                scores.append((name,int(moves)))
            scores.sort(key=lambda x:x[1])
            return scores
    def play_replay(scr, tur):
        global board
        scr.clear()
        shuffled_copy = [row[:] for row in shuffled_board]
        board = [row[:] for row in shuffled_copy]
        for r in range(4):
            for c in range(4):
                draw_grid(r, c)
        scr.update()
        def step(idx):
            if idx < len(moves_list):
                move = moves_list[idx]
                if move == "up":
                    move_up(replay=True)
                elif move == "down":
                    move_down(replay=True)
                elif move == "left":
                    move_left(replay=True)
                elif move == "right":
                    move_right(replay=True)
                scr.ontimer(lambda: step(idx + 1), 400)
            else:
                tur.penup()
                tur.goto(0,-200)
                tur.write("Replay Finished!", align="center", font=("Arial", 24, "bold"))
        step(0)
    tur.speed(0)
    scr.title("FenPuzzle")
    scr.bgpic(r"D:\code\BTech 1st sem\game\bg.gif")
    tur.ht()
    tur.color("cyan")
    tur.penup()
    tur.goto(-200, 200)
    tur.pendown()
    tur.begin_fill()
    for i in range(4):
        tur.fillcolor("lightyellow")
        tur.forward(400)
        tur.right(90)
    tur.end_fill()
    tur.color("cyan")
    tur.penup()
    tur.goto(-200,100)
    tur.pendown()
    for i in range(1,4):
        tur.forward(400)
        tur.penup()
        tur.goto(-200,100-i*100)
        tur.pendown()
    tur.penup()
    tur.goto(-100,200)
    tur.right(90)
    tur.pendown()
    for i in range(1,4):
        tur.forward(400)
        tur.penup()
        tur.goto(-100+i*100,200)
        tur.pendown()
    tur.penup()
    number = list(range(1,16)) + [None]
    board = [number[i:i+4] for i in range(0,16,4)]
    tur.color("black")
    for r in range(4):
        for c in range(4):
            if board[r][c] is not None:
                x = -200 + c*100 + 50
                y = 200 - r*100 - 60
                tur.goto(x, y)
                tur.write(str(board[r][c]),align="center",font=("Arial", 24, "bold"))
    tur.left(90)
    level = scr.textinput("Choose Difficulty", "Type easy, medium, or hard:").lower()
    moves = {"easy":30,"medium":60,"hard":120}.get(level,30)
    last_move = None
    all_moves = [move_up, move_down, move_left, move_right]
    opp = {move_up:move_down, move_down:move_up, move_left:move_right, move_right:move_left}
    shuffling = True
    for i in range(moves):
        choices = all_moves[:]
        if last_move and opp[last_move] in choices:
            choices.remove(opp[last_move])
        move = random.choice(choices)
        move()
        last_move = move
    shuffling = False
    shuffled_board = [row[:] for row in board]
    # Controls
    scr.listen()
    scr.onkey(move_up, "Up")
    scr.onkey(move_down, "Down")
    scr.onkey(move_right, "Right")
    scr.onkey(move_left, "Left")
start()
turtle.done()