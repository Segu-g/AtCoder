from collections import deque


def main():
    s = tuple(map(lambda c: c == 'X', input()))
    k = int(input())
    queue = deque()
    queue_sum = 0
    count = 0
    max_ans = 0
    for c in s + (False, ):
        if c:
            count += 1
            continue
        queue.append(count)
        queue_sum += count
        if len(queue) > k + 1:
            queue_sum -= queue.popleft()
        # print(queue, queue_sum)
        max_ans = max(max_ans, queue_sum + len(queue) - 1)
        count = 0
    print(max_ans)


if __name__ == "__main__":
    main()