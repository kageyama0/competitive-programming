# 木クラスを import
from tree.binary_search_tree import BinarySearchTree
from tree.binary_search_tree.recursive import BinarySearchNode


def main():
    n = int(input())
    W = list(map(int, input().split()))
    bst = BinarySearchTree(BinarySearchNode)
    for i in range(n):
        bst.insert(W[i])
    print(bst)


if __name__ == "__main__":
    main()
