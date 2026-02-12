t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    def simulate(start_with_white):
        white = a
        dark = b
        size = 1
        layers = 0
        turn_white = start_with_white

        while True:
            if turn_white:
                if white < size:
                    break
                white -= size
            else:
                if dark < size:
                    break
                dark -= size

            layers += 1
            size *= 2
            turn_white = not turn_white

        return layers

    ans = max(simulate(True), simulate(False))
    print(ans)
