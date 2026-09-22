import shutil, os, subprocess, datetime

SOURCE_DIR = r"E:\APDS\Debashish Saha\DS10\fno_scanner\data"
DEST_DIR   = r"E:\quantlight-signals\data"

FILES_TO_SHARE = [
    "gd_picks.json",
    "gamma_structural_trade_log.json",
    "stock_indicators.json",
    "market_structure.json",
    "gamma_profiles.json",
    "intraday_picks.json",
    "watchlist_structural.json",
]

os.makedirs(DEST_DIR, exist_ok=True)

for fname in FILES_TO_SHARE:
    src = os.path.join(SOURCE_DIR, fname)
    dst = os.path.join(DEST_DIR, fname)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied: {fname}")
    else:
        print(f"Skipped (not found): {fname}")

os.chdir(r"E:\quantlight-signals")
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Signal update: {now}"])
subprocess.run(["git", "push", "origin", "main"])
print("✅ Signals pushed to GitHub")