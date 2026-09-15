# Frank (Qingtao) Liu
<img width="1918" height="430" alt="image" src="https://github.com/user-attachments/assets/5285e824-347d-41d3-afa6-f5efd65e8a49" />

## Merge output on `main`

![Screenshot of git merge develop on main](merge-output.png)

## Activity 3: Issue, pull request and merge conflict

![Pull request showing a merge conflict in helloworld.py](pr-conflict.png)

![Pull request #2 successfully merged and closed](pr-merged.png)

![git log on main showing the merge commit](merge-log.png)

## Activity 4: Unit tests

`utils.py` defines the `utils` class with `reversed` and `formatter`; `utils_tests.py` tests both with integer, float and string inputs.
Run with `python -m unittest utils_tests -v`.

![Commits for utils.py and utils_tests.py](activity4-commits.png)

## Activity 5: Git rebase

Branch `rebase` was created from `develop` with commits c1 and c2. Then c3 and c4 were added on `develop`.

Before the rebase, c1/c2 and c3/c4 sat on separate lines of history:

![History before the rebase](rebase-before.png)

`git rebase develop` (run on the `rebase` branch) replayed c1 and c2 on top of c4, giving them new commit hashes:

![git rebase develop output](rebase-command.png)

`develop` was then fast-forwarded to the rebased commits and both branches were pushed. Final order: c3 -> c4 -> c1 -> c2.

![History after the rebase and push](rebase-after.png)
