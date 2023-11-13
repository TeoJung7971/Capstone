# Capstone

필요 라이브러리
cv2
numpy
pandas
pygame
pygamevideo (폴더 안에 넣어두어서 따로 import할 필요 없음)

[주의사항]
- pygamevideo.py 파일에서 *position: Union[tuple[float, float], pygame.Vector2, pygame.Rect]* 부분에서 에러 발생 시
- from typing import Tuple 추가한 뒤 tuple을 Tuple로 변경

- 음악 실행 중 소리가 이상하게 들린다면 아래 부분 주석 처리
#음악 재생 시 에러 발생 추후 수정 예정
mixer.init()
mixer.music.load('media/MUSIC_CHILL.mp3')
mixer.music.set_volume = 0.5
mixer.music.play()

- 현재 웹캠 기능은 꺼 둔 상태임에 유의
