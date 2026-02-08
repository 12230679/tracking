import os

# 결과 폴더
path = r'C:\tracking\TrackEval\data\trackers\mot_challenge\dancetrack-val\my_tracker'

print("\n🔍 모든 결과 파일을 뒤져서 MOTA와 IDF1을 찾습니다...")

found = False
for file in os.listdir(path):
    if file.endswith(".txt") or file.endswith(".csv"):
        file_path = os.path.join(path, file)
        with open(file_path, 'r') as f:
            content = f.read()
            if "MOTA" in content or "IDF1" in content:
                print(f"\n✅ [{file}] 에서 점수 발견!")
                print("-" * 50)
                # 줄바꿈 기준으로 잘라서 점수 부분만 출력
                lines = content.split('\n')
                for line in lines[:3]: # 상위 몇 줄만 출력
                    print(line)
                found = True

if not found:
    print("\n❌ 어느 파일에서도 MOTA/IDF1을 찾지 못했습니다. 명령어를 수정해서 다시 실행해야 합니다.")