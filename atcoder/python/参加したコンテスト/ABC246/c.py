N, K, X = map(int, input().split())
A = list(map(int, input().split()))


# X円で引ける分だけとりあえず引く
for i in range(N):
    # クーポンがもう残っていないならループ終了
    if K <= 0:
        break

    # クーポンで何回値引きできるか
    can_discount = A[i] // X

    # 引ける回数が、クーポンの残り枚数より多い場合
    if can_discount > K:
        A[i] -= X * K
        K = 0
        break
    # クーポンを使って値引きしても、まだクーポンが余っている場合
    else:
        A[i] -= can_discount * X
        K -= can_discount

# print(A)

# まだクーポンが残っている場合
if K > 0:
    A.sort(reverse=True)

    p = 0
    # クーポンが余っていて、かつまだ全部の配列に対して値引きしていない場合
    while K > 0 and p <= N-1:
        # クーポンを使って値段を0にする
        A[p] = 0

        # クーポンを使った分引いておく
        K -= 1

        # クーポンを使う対象を移動する
        p += 1


print(sum(A))
