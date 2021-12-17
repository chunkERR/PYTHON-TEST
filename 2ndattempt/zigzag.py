import sys, time

indent = 0
indentIncreasing = True

# main game loop

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)
        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
            
except KeyboardInterrupt:
    sys.exit()
