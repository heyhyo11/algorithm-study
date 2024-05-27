import sys
input = sys.stdin.readline
n = int(input())
tree = {}


for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]


# 전위 순회
def preorder(now):
    if now == '.':
        return
    print(now, end='') # 현재 노드
    preorder(tree[now][0]) # 왼쪽 탐색
    preorder(tree[now][1]) # 오른쪽 탐색


# 중위 순회
def inorder(now):
    if now == '.':
        return
    inorder(tree[now][0])
    print(now, end='')
    inorder(tree[now][1])


# 후위 순회
def postorder(now):
    if now == '.':
        return
    postorder(tree[now][0])
    postorder(tree[now][1])
    print(now, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')