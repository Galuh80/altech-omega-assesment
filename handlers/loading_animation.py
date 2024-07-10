import sys
import time

class LoadingAnimation:
    def __init__(self, total):
        self.total = total

    def animate(self, iteration):
        animation = "|/-\\"
        idx = iteration % len(animation)
        sys.stdout.write(f"\rSeeding data... {animation[idx]} {iteration + 1}/{self.total}")
        sys.stdout.flush()
        time.sleep(0.1)

    def finish(self):
        sys.stdout.write("\rSeeding data... Done!\n")
        sys.stdout.flush()
