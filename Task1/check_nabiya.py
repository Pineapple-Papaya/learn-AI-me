"""用官方检查器与回归测试验证本目录的作业1.py。"""

import importlib.util
from pathlib import Path
import runpy
import sys
import unittest


def main() -> None:
    task_dir = Path(__file__).resolve().parent
    homework = task_dir / "作业1.py"
    checks = (
        task_dir.parent
        / "docs/work-2026/foundation/Nabia_Snack_Incident"
    )

    spec = importlib.util.spec_from_file_location("longmen_vs_nabiya", homework)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载作业：{homework}")
    battle = importlib.util.module_from_spec(spec)
    sys.modules["longmen_vs_nabiya"] = battle
    spec.loader.exec_module(battle)

    print("检查对象：Task1/作业1.py", flush=True)
    runpy.run_path(str(checks / "check_my_code.py"), run_name="__main__")
    suite = unittest.defaultTestLoader.discover(
        start_dir=str(checks), pattern="test_battle.py"
    )
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)


if __name__ == "__main__":
    main()
