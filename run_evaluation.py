import os
import subprocess

trackeval_path = r'C:\tracking\TrackEval'
script_path = os.path.join(trackeval_path, 'scripts', 'run_mot_challenge.py')

command = [
    'python', script_path,
    '--BENCHMARK', 'dancetrack',
    '--SPLIT_TO_EVAL', 'val',
    '--TRACKERS_TO_EVAL', 'my_tracker',
    '--USE_PARALLEL', 'False'
]

print("📊 드디어 제대로 된 점수를 확인할 시간입니다! 잠시만 기다리세요...")
subprocess.run(command, cwd=trackeval_path)