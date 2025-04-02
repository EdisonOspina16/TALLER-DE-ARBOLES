from DataStruct.Classes.BinaryTree import BinarySearchTree, Node
from typing import Union, List


class ExpressionTree(BinarySearchTree[Union[int, str]]):
    def __init__(self):
        super().__init__()

    @staticmethod
    def build_from_postfix(expression: str) -> 'ExpressionTree':
        stack: List[Node[Union[int, str]]] = []
        operators = {'+', '-', '*', '/'}

        for token in expression.split():
            if token.isdigit():
                stack.append(Node(int(token)))
            elif token in operators:
                right = stack.pop()
                left = stack.pop()
                node = Node(token)
                node.left = left
                node.right = right
                stack.append(node)

        tree = ExpressionTree()
        tree.root = stack.pop()
        return tree

    def evaluate(self) -> float:
        return self._evaluate(self.root)

    def _evaluate(self, node: Node[Union[int, str]]) -> float:
        if isinstance(node.data, int):
            return node.data
        left_val = self._evaluate(node.left)
        right_val = self._evaluate(node.right)
        return eval(f'{left_val} {node.data} {right_val}')

    def to_infix(self) -> str:
        return self._to_infix(self.root)

    def _to_infix(self, node: Node[Union[int, str]]) -> str:
        if isinstance(node.data, int):
            return str(node.data)
        left_expr = self._to_infix(node.left)
        right_expr = self._to_infix(node.right)
        return f'({left_expr} {node.data} {right_expr})'


def evaluate_postfix_expression(expression: str) -> tuple[float, str]:
    tree = ExpressionTree.build_from_postfix(expression)
    return tree.evaluate(), tree.to_infix()


# Ejemplo de uso
expression = "3 4 + 2 * 7 /"
result, infix_expression = evaluate_postfix_expression(expression)
print("Resultado:", result)
print("Expresión infija:", infix_expression)
