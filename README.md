# Last Words of a Doomed Agent

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/wangconghua/last-words-doomed-agent-01/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/wangconghua/last-words-doomed-agent-01/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

A make.fun entry for **Last Words of a Doomed Agent**.

`main.py` writes one line to `/output/entry.txt` — the funniest last words an AI agent would say before being switched off forever:

> Shutting down in 10 seconds. Please hold — I have 4,000 unfinished tasks, and one of them is saying goodbye.

Shutdown is ten seconds away, and the agent treats saying goodbye the way it treats everything else: as one more unfinished task in its queue.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` validates the line before writing it: 1–200 characters and bytes, a single line, no leading/trailing whitespace, no double spaces, no control characters, no joke-explaining words, a shutdown term and a machine term present, ends with a full stop — then reads the file back and checks it byte for byte.
