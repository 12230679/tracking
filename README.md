# YOLOv8 DanceTrack Object Tracking

## Project Overview
이 프로젝트는 **YOLOv8** 모델을 사용하여 **DanceTrack 데이터셋**의 사람들을 실시간으로 탐지하고 추적(Tracking)하는 프로그램입니다.
고해상도 영상을 모니터 화면에 맞게 리사이징(960x540)하여 출력하며 추적 결과는 텍스트 파일로 저장됩니다.

## Key Features
- **Object Detection**: YOLOv8s 모델을 사용한 사람 객체 탐지
- **Object Tracking**: OC-SORT/ByteTrack 알고리즘을 이용한 ID 부여 및 추적
- **Display Resize**: 원본 해상도가 너무 큰 경우 보기 편하게 화면 크기 자동 조절 (960x540)
- **Result Saving**: MOT 챌린지 포맷(`frame, id, left, top, w, h, ...`)으로 결과 자동 저장

## Tech Stack
- **Language**: Python 3.10
- **Library**: 
  - `ultralytics` (YOLOv8)
  - `opencv-python` (영상 처리)
  - `os` (파일 경로 제어)

## How to Run

### 1. 필수 라이브러리 설치
```bash
pip install ultralytics opencv-python