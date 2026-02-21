# Codebase task proposals

1. **Typo fix task**
   - **Issue found:** The UI text says `change averaging rage` and `comma seperated values`.
   - **Proposed task:** Correct these user-facing typos to `change averaging range` and `comma separated values`.
   - **Why it matters:** Improves professionalism and avoids confusion in CLI prompts.
   - **References:** `Kernlogger.py` lines 122 and 130.

2. **Bug fix task**
   - **Issue found:** The `t` command stores input in `title`, but plotting uses `tit`, so title changes are ignored.
   - **Proposed task:** Update the `t` command branch to assign to `tit` (or refactor to a single consistent variable name).
   - **Why it matters:** Restores expected behavior for changing plot titles from the menu.
   - **References:** `Kernlogger.py` lines 11, 111, 125-127.

3. **Comment/documentation discrepancy task**
   - **Issue found:** A comment says `let's wait one second`, but the code sleeps for `samplerate` seconds (default 1.2 and user configurable).
   - **Proposed task:** Rewrite the comment to match actual behavior, e.g. `wait for the configured sample interval`.
   - **Why it matters:** Prevents misleading maintenance guidance and helps future debugging.
   - **References:** `Kernlogger.py` lines 59-60.

4. **Test improvement task**
   - **Issue found:** No automated tests validate command handling or serial parsing logic.
   - **Proposed task:** Add a unit test module that mocks serial + keyboard I/O and verifies:
     - `t` command updates the plot title variable used by `plotter`.
     - `avg`, `ra`, and `csv` command branches parse inputs correctly.
     - `run()` appends averaged values after the expected sample count.
   - **Why it matters:** Reduces regressions in this interactive hardware-facing script.
   - **References:** `Kernlogger.py` lines 42-73 and 91-131.
