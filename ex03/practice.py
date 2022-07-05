board_x = 0
board_y = 0
road_w = 0
road_map = []
piece_x = 0
piece_y = 0
is_playing = False
is_goal = False
piece_size = 0
play_time = 0
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
is_search_left = False
piece_dir = 0
mode3D=False
def make_board(x, y, w):
    global board_x, board_y
    global road_w
    global road_map
    board_x = x + 4
    board_y = y + 4
    road_w = w
    road_map = [[0 for y in range ( board_y )] for x in range ( board_x )]
def init_maze():
    global is_mouse_playing
    global piece_x, piece_y
    global is_playing
    global is_goal
    global piece_size
    global play_time
    global is_search_left
    global piece_dir
    for x in range(0, board_x):
        for y in range(0, board_y):
            road_map[x][y] = 1
    for x in range(3, board_x-3):
        for y in range(3, board_y-3):
            road_map[x][y] = 0
    piece_x = 2
    piece_y = 3
    is_playing = False
    is_goal = False
    is_mouse_playing = False
    piece_size = 0.7*road_w
    play_time = 0
    is_search_left = False
    piece_dir = 0
    road_map[2][3] = 2
    road_map[board_x-3][board_y-4] = 3
    
def draw_maze():
    noStroke()
    background(100)
    for x in range(2, board_x-2):
        for y in range(2,board_y-2):
            if road_map[x][y] == 0:
                fill(100, 0, 0)
            elif road_map[x][y] == 1:
                fill(0, 200, 0)
            elif road_map[x][y] == 2:
                fill(200, 200, 0)
            elif road_map[x][y] == 3:
                fill(200, 0, 200)
            rect(road_w*x, road_w*y,road_w,road_w)
def setup():
    size(800, 600, P3D)
    make_board(13, 9, 46)
    init_maze()
def draw():
    if mode3D:
        draw_maze3D()
    else:
        camera(width/2,height/2,(height/2)/tan(PI/6),
               width/2,height/2,0,0,1,0)
        perspective(PI/3,float(width)/float(height),
                    (height/2)/tan(PI/6)/10,(height/2)/tan(PI/6)*10)   
        draw_maze()
        draw_piece() 
    if is_playing or is_goal or is_mouse_playing:
        draw_info()
    check_finish()    
    if is_search_left:
        search_left()


def keyPressed():
    global piece_x, piece_y
    global is_playing
    global is_search_left  
    global mode3D,piece_dir  
    if key == 'a':
        generate_maze_up_down()
    elif key == 'k':
        is_playing = True
    elif key == 'i':
        init_maze()
    elif key == 'r':
        generate_maze_random()
    elif key == 's':
        is_search_left = True
    elif key == 'm':
        if mode3D:
            mode3D=False
        else:
            mode3D=True
    if is_playing:
        if mode3D:
            if keyCode== UP:
                if piece_dir == 0 and road_map[piece_x+1][piece_y] != 1:
                    piece_x += 1
                elif piece_dir == 1 and road_map[piece_x][piece_y+1] != 1:
                    piece_y += 1
                elif piece_dir == 2 and road_map[piece_x-1][piece_y] != 1:
                    piece_x -= 1
                elif piece_dir == 3 and road_map[piece_x][piece_y-1] != 1:
                    piece_y -= 1
            elif keyCode == DOWN:
                if piece_dir == 0 and road_map[piece_x+1][piece_y] != 1:
                    piece_x -= 1
                elif piece_dir == 1 and road_map[piece_x][piece_y+1] != 1:
                    piece_y -= 1
                elif piece_dir == 2 and road_map[piece_x-1][piece_y] != 1:
                    piece_x += 1
                elif piece_dir == 3 and road_map[piece_x][piece_y-1] != 1:
                    piece_y += 1
            elif keyCode == LEFT:
                piece_dir = (piece_dir+3)%4
            elif keyCode == RIGHT:
                piece_dir = (piece_dir+3)%4
        else:
            if keyCode == UP and piece_y > 0:
                if not road_map[piece_x][piece_y-1] == 1:
                    piece_y -= 1
            if keyCode == RIGHT and piece_x < board_x-1:
                if not road_map[piece_x+1][piece_y] == 1:
                    piece_x += 1
            if keyCode == DOWN and piece_y < board_y-1:
                if not road_map[piece_x][piece_y+1] == 1:
                    piece_y += 1
            if keyCode == LEFT and piece_x > 0:
                if not road_map[piece_x-1][piece_y] == 1:
                    piece_x -= 1        
def generate_maze_up_down():
    for x in range(4, board_x-3, 4):
        for y in range(3, board_y-4):
            road_map[x][y] = 1
    for x in range(6, board_x-3, 4):
        for y in range(board_y-4, 3, -1):
            road_map[x][y] = 1        
def draw_piece():
    global piece_x, piece_y
    if is_mouse_playing:
        in_touch = False
        pos_x = mouseX % road_w
        pos_y = mouseY % road_w
        p_x = mouseX / road_w
        p_y = mouseY / road_w
        if p_x >= 2 and p_x < board_x-2 and p_y >= 2 and p_y < board_y-2:
            piece_x = p_x
            piece_y = p_y
        if road_map[piece_x][piece_y] == 1 or (road_map[piece_x+1][piece_y] == 1 and pos_x > road_w - piece_size/2) or (road_map[piece_x-1][piece_y] == 1 and pos_x < piece_size/2) or (road_map[piece_x][piece_y+1]==1 and pos_y > road_w-piece_size/2) or (road_map[piece_x][piece_y-1] == 1 and  pos_y < road_w-piece_size/2):
            in_touch = True
        if in_touch:
            fill(255, 0, 0)
        else:
            fill(0, 200, 0)
        ellipse(mouseX, mouseY, piece_size, piece_size)
    else:
        fill(0, 200, 0)
        ellipse((piece_x+0.5)*road_w, (piece_y+0.5)*road_w, piece_size, piece_size)
def draw_info():
    global play_time
    if is_playing or is_mouse_playing:
        play_time += 1
    textSize(30)
    fill(255, 255, 0)
    text("Time = "+ str(play_time), 20, 30)
        
def check_finish():
    global is_playing, is_goal, is_mouse_playing, is_search_left
    if road_map[piece_x][piece_y] == 3:
        is_playing = False
        is_goal = True
        is_mouse_playing = False
        is_search_left = False
def generate_maze_random():
    count = 1
    while count != 0:
        count = 0
        for x in range(2,board_x-2, 2):
            for y in range(2, board_y-2, 2):
                if road_map[x][y] == 1:
                    r = int(random(0,4))
                    dx = dir_x[r]
                    dy = dir_y[r]
                    if road_map[x+dx*2][y+dy*2] == 0:
                        road_map[x+dx][y+dy] = 1
                        road_map[x+dx*2][y+dy*2] = 1
                else:
                    count += 1         
def mousePressed():
    global is_mouse_playing
    if road_map[mouseX/road_w][mouseY/road_w]==2:
        is_mouse_playing=True
def search_left():
    global piece_dir, piece_x, piece_y
    if frameCount % 10 == 0:
        for i in range(4):
            dir = (piece_dir + 3 + i) % 4
            x = piece_x + dir_x[dir]
            y = piece_y + dir_y[dir]
            if road_map[x][y] == 0 or road_map[x][y] == 3:
                break
        piece_dir = dir
        piece_x = x
        piece_y = y

def draw_maze3D():###
    background(100)
    stroke(0)
    camera(piece_x*road_w,piece_y*road_w,0,
           piece_x*road_w+dir_x[piece_dir],piece_y*road_w+dir_y[piece_dir],0,
           0,0,-1)
    perspective(radians(100),float(width)/float(height),1,800)
    for x in range(2,board_x-2):
        for y in range(2,board_y-2):
            if road_map[x][y]==0:
                fill(100,0,0)
            elif road_map[x][y]==1:
                fill(0,200,0)
            elif road_map[x][y]==2:
                fill(200,200,0)
            elif road_map[x][y]==3:
                fill(200,0,200)
            pushMatrix()
            if road_map[x][y]==1:
                translate(x*road_w,y*road_w,0)
                box(road_w)
            else:
                translate(x*road_w,y*road_w,-road_w/2)
                box(road_w,road_w,1)
            popMatrix()