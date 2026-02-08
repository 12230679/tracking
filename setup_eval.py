import os
import subprocess
import shutil

# 1. TrackEval 다운로드 (git 없어도 되도록 zip으로 받기)
if not os.path.exists('TrackEval'):
    print("TrackEval 다운로드 중...")
    # git이 있다면 아래 명령어, 없다면 직접 다운로드 필요
    os.system('git clone https://github.com/JonathonLuiten/TrackEval.git')

# 2. 필요한 폴더 구조 자동 생성
# 이 경로는 TrackEval의 표준 규격입니다.
gt_dir = r'TrackEval/data/gt/mot_challenge/dancetrack-val/dancetrack0004/gt'
tracker_dir = r'TrackEval/data/trackers/mot_challenge/dancetrack-val/my_tracker/data'

os.makedirs(gt_dir, exist_ok=True)
os.makedirs(tracker_dir, exist_ok=True)

# 3. 파일 복사 (경로는 본인의 환경에 맞게 수정하세요)
# 내 결과 파일 복사 및 이름 변경
shutil.copy('dancetrack0004_results.txt', os.path.join(tracker_dir, 'dancetrack0004.txt'))

print("✅ 모든 준비가 끝났습니다!")
print("이제 터미널에서 아래 명령어를 입력하세요:")
print("cd TrackEval")
print("python scripts/run_mot_challenge.py --BENCHMARK dancetrack --SPLIT_TO_EVAL val --TRACKERS_TO_EVAL my_tracker --METRICS HOTA MOTA IDF1 --USE_PARALLEL False")