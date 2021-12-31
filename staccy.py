import sys


if __name__ == "__main__":
    stack = []
    data = ""

    if len(sys.argv) == 1:
        data = input("")
    elif len(sys.argv) >= 2:
        try:
            with open(sys.argv[1], "r") as f:
                data = f.read()
        except FileNotFoundError:
            print(f"Error: File {sys.argv[1]} was not found.")
            exit(1)
    debug = False
    if len(sys.argv) >= 3:
        debug = (sys.argv[2].lower() == "true")

    """
    0 - push 0 on stack
    1 - push 1 on stack
    2 - push 2 on stack
    3 - push 3 on stack
    4 - push 4 on stack
    5 - push 5 on stack
    6 - push 6 on stack
    7 - push 7 on stack
    8 - push 8 on stack
    9 - push 9 on stack
    + - pop two values from stack and add them together
    * - pop two values from stack and multiply them
    - - pop two values from stack and subtract top from bottom
    / - pop two values from stack and divide top by bottom
    % - pop value from stack and print it out as number
    $ - pop value from stack and print it out as ascii char
    ! - duplicate the value on top of the stack
    ~ - swap the positions of the top two values on the stack
    ^ - pop two values from stack and xor them
    & - pop two values from stack and perform binary AND on them
    # - push input as number
    ` - pop from stack and goto the character in the code (all characters count, yes even newlines)
    < - 1 if top less than bottom 0 otherwise
    > - 1 if top grtr than bottom 0 otherwise
    = - 1 if top eqls bottom 0 otherwise
    """

    instr_counter = 0

    while instr_counter < len(data):
        instr = data[instr_counter]
        if instr not in "0123456789+*-/%$!=^&#@`<>~":
            instr_counter += 1
            continue

        if instr in "0123456789":
            stack.append(int(instr))
        elif instr == "+":
            stack.append(stack.pop() + stack.pop())
        elif instr == "*":
            stack.append(stack.pop() * stack.pop())
        elif instr == "-":
            stack.append(stack.pop() - stack.pop())
        elif instr == "/":
            stack.append(stack.pop() / stack.pop())
        elif instr == "%":
            print(stack.pop(), end="")
        elif instr == "$":
            print(chr(stack.pop()), end="")
        elif instr == "!":
            stack.append(stack[-1])
        elif instr == "~":
            stack.extend((stack.pop(), stack.pop(-1)))
        elif instr == "^":
            stack.append(stack.pop() ^ stack.pop())
        elif instr == "&":
            stack.append(stack.pop() & stack.pop())
        elif instr == "#":
            stack.append(ord(input()))
        elif instr == "=":
            stack.append(int(stack.pop() == stack.pop()))
        elif instr == "<":
            stack.append(int(stack.pop() < stack.pop()))
        elif instr == ">":
            stack.append(int(stack.pop() > stack.pop()))

        if instr == "`":
            instr_counter = stack.pop()
        else:
            instr_counter += 1

        if debug:
            print(f"\n{instr} at {instr_counter}; {stack = }")
