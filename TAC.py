class ThreeAddressCodeGenerator:
    def __init__(self):
        self.temp_var_count = 0
        self.instructions = []
    
    def generate(self, node):
        if node.op == '+':
            left_operand = self.generate(node.left)
            right_operand = self.generate(node.right)
            temp_var = 't' + str(self.temp_var_count)
            self.temp_var_count += 1
            instruction = temp_var + ' = ' + left_operand + ' + ' + right_operand
            self.instructions.append(instruction)
            return temp_var
        elif node.op == '-':
            left_operand = self.generate(node.left)
            right_operand = self.generate(node.right)
            temp_var = 't' + str(self.temp_var_count)
            self.temp_var_count += 1
            instruction = temp_var + ' = ' + left_operand + ' - ' + right_operand
            self.instructions.append(instruction)
            return temp_var
        elif node.op == '*':
            left_operand = self.generate(node.left)
            right_operand = self.generate(node.right)
            temp_var = 't' + str(self.temp_var_count)
            self.temp_var_count += 1
            instruction = temp_var + ' = ' + left_operand + ' * ' + right_operand
            self.instructions.append(instruction)
            return temp_var
        elif node.op == '/':
            left_operand = self.generate(node.left)
            right_operand = self.generate(node.right)
            temp_var = 't' + str(self.temp_var_count)
            self.temp_var_count += 1
            instruction = temp_var + ' = ' + left_operand + ' / ' + right_operand
            self.instructions.append(instruction)
            return temp_var
        else:
            return node.value
    
    def print_output(self):
        for instruction in self.instructions:
            print(instruction)
parser = Parser()
ast = parser.parse('x = (a + b) * c')
generator = ThreeAddressCodeGenerator()
generator.generate(ast)
generator.print_output()
