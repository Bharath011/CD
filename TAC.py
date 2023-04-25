import ast

class CodeGenerator:
    def __init__(self):
        pass

    def generate_and_print(self, ast_tree):
        # Generate three-address code from the AST
        three_address_code = self.generate(ast_tree)

        # Print the three-address code
        print(three_address_code)

    def generate(self, node):
        # Generate three-address code recursively for all nodes in the AST
        if isinstance(node, ast.Module):
            code = ""
            for statement in node.body:
                code += self.generate(statement)
            return code
        elif isinstance(node, ast.Expr):
            return self.generate(node.value) + "\n"
        elif isinstance(node, ast.BinOp):
            left = self.generate(node.left)
            right = self.generate(node.right)
            temp = self.get_temp()
            op = self.get_operator(node.op)
            code = temp + " = " + left + " " + op + " " + right + "\n"
            return code + temp
        elif isinstance(node, ast.UnaryOp):
            operand = self.generate(node.operand)
            temp = self.get_temp()
            op = self.get_operator(node.op)
            code = temp + " = " + op + " " + operand + "\n"
            return code + temp
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Num):
            return str(node.n)
        else:
            raise NotImplementedError("Unsupported node type")

    def get_temp(self):
        # Generate a new temporary variable name
        CodeGenerator.temp_counter += 1
        return "t" + str(CodeGenerator.temp_counter)

    def get_operator(self, op):
        # Map operators to their corresponding symbols in three-address code
        if isinstance(op, ast.Add):
            return "+"
        elif isinstance(op, ast.Sub):
            return "-"
        elif isinstance(op, ast.Mult):
            return "*"
        elif isinstance(op, ast.Div):
            return "/"
        elif isinstance(op, ast.USub):
            return "-"
        else:
            raise NotImplementedError("Unsupported operator")

CodeGenerator.temp_counter = 0
# Example usage
import ast

code = 'x = (1 + 2) * 3'
ast_tree = ast.parse(code)
generator = CodeGenerator()
generator.generate_and_print(ast_tree)
