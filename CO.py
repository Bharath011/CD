import ast

class Optimizer:
    def __init__(self):
        pass

    def optimize_and_print(self, code):
        # Parse the input code and construct an AST
        ast_tree = ast.parse(code)

        # Print the original code
        print("Original code:\n" + code)

        # Apply constant folding to the AST
        self.constant_folding(ast_tree)

        # Convert the optimized AST back into code
        optimized_code = ast.unparse(ast_tree)

        # Print the optimized code
        print("Optimized code:\n" + optimized_code)

    def constant_folding(self, node):
        # Apply constant folding recursively to all nodes in the AST
        for child in ast.iter_child_nodes(node):
            self.constant_folding(child)

        if isinstance(node, ast.BinOp) and isinstance(node.left, ast.Num) and isinstance(node.right, ast.Num):
            # If both operands are constants, evaluate the operation and replace the node with the result
            result = self.evaluate_binop(node.op, node.left.n, node.right.n)
            new_node = ast.Num(n=result)
            ast.copy_location(new_node, node)
            ast.fix_missing_locations(new_node)
            ast_parent = ast.parse("")
            ast_parent.body = [new_node]
            return new_node
        else:
            return node

    def evaluate_binop(self, op, left, right):
        # Evaluate a binary operation between two constants
        if isinstance(op, ast.Add):
            return left + right
        elif isinstance(op, ast.Sub):
            return left - right
        elif isinstance(op, ast.Mult):
            return left * right
        elif isinstance(op, ast.Div):
            return left // right
        else:
            raise NotImplementedError("Unsupported operator")

# Example usage
code = "x = 3 + 4 * 2 - 1"
optimizer = Optimizer()
optimizer.optimize_and_print(code)
