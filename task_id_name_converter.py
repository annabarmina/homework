def camel_to_snake(name):
    snake = []
    for i in name:
        if i.isupper():
            snake.append('_')
        snake.append(i.lower())
    if snake[0] == '_':
        snake.remove(snake[0])
    return(''.join(snake))
    #print(snake)
