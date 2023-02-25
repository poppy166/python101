import turtle
tao = turtle.Pen()
tao.shape('turtle')
    
for i in range(5):
    tao.penup()
    tao.right(90)
    tao.forward(45)
    tao.left(90)
    tao.pendown()
    for i in range(2):
        tao.penup()
        tao.right(90)
        tao.forward(5)
        tao.right(90)
        tao.backward(20)
        tao.pendown()
        for i in range(7):
            tao.penup()
            tao.forward(20)
            tao.pendown()
            for i in range(6):
                tao.forward(10)
                tao.left(60)
