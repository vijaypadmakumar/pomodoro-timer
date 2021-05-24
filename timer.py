import time as t
from log import log


def timer():
    work_time = 0
    break_time = 0
    while work_time:
        mins, secs = divmod(work_time, 60)
        work_timer = f"{mins}:{secs}"
        print(work_timer)
        t.sleep(1)
        work_time -= 1
    # add audio alert here
    print(f"break for 5 mins")
    while break_time:
        mins, secs = divmod(break_time, 60)
        break_timer = f"{mins}:{secs}"
        print(break_timer)
        t.sleep(1)
        break_time -= 1
    print(f"break over, time to work for 25 mins")

    # logging
    log()
