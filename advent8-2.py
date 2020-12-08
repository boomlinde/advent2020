import sys

NOP, JMP, ACC = 0, 1, 2
mapping = { 'nop': NOP, 'jmp': JMP, 'acc': ACC, }
instructions = {
    NOP: lambda acc, pc, operand: (acc, pc + 1),
    JMP: lambda acc, pc, operand: (acc, pc + operand),
    ACC: lambda acc, pc, operand: (acc + operand, pc + 1),
}

def assemble(inp):
    code = []
    for line in inp:
        name, operand = line.strip().split()
        code.append((mapping[name], int(operand)))
    return code

def step(code, acc, pc):
    return instructions[code[pc][0]](acc, pc, code[pc][1])

def terminates(code):
    acc, pc = 0, 0
    executed = {}
    while True:
        if executed.get(pc):
            return False, acc
        if pc >= len(code):
            return True, acc
        executed[pc] = True
        acc, pc = step(code, acc, pc)

def findterminating(code):
    for i, ins in enumerate(code):
        op, operand = ins
        if op in (NOP, JMP):
            newins = ((NOP if op == JMP else JMP), operand)
            code[i] = newins
            ok, acc = terminates(code)
            if ok:
                return acc
            code[i] = ins

code = assemble(sys.stdin)

print findterminating(code)
