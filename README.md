과학융합탐구 발표 대본
이 알고리즘을 떠올리게 된 계기는 밤에 잠에서 깨서 물을 마시러 가기 위해 불을 킬 때 벽을 짚으면서 스위치를 찾는데 정말 우연하게 1학년 정보 시간에 배웠던 프랙탈 도형의 선이 반복되는 모습이 떠오른 것입니다.
생각을 정리하면서 특정 지점에 도달할 때마다 선을 다시 여러 각도로 뻗는 작업을 반복하면 목표 지점에 도달할 수 있는 경로를 얻을 수 있을 것이라고 생각했습니다. 또 각 지점의 거리를 0에 가깝게 줄일수록 최적에 가까운 경로가 얻어질 것이라고 생각했습니다.
이와 비슷한 사례가 있는데 바로 한정된 영역인 해안선, 섬이 무한에 가까운 값을 가지게 될수 있다는 해안선 역설입니다.
예를 들어 미국의 상원 연구기관에서는 미국의 해안선을 19928(만구천구백이십팔)km, CIA는 30455(삼만사백오십오)km, 미국 해양기상청에서는 153646(십오만삼천육백사십육)km라고 발표했다고 합니다.
이러한 현상이 발생하는 이유는 해안선을 직선으로 나타내는 범위가 짧을수록 이 선이 무한히 많이 필요하게 되기 때문입니다. 즉 해안선이 프랙탈 형태이기 때문입니다.
프랙탈은 일부 작은 조각이 전체와 비슷한 기하학적 형태를 말합니다.
프랙탈은 자기유사성이라는 특징이 있습니다. 자기 유사성은 부분을 확대할 때 자신을 포함한 전체와 닮은 모습을 보여주는 성질입니다.
프랙탈은 망델브로 집합, 칸토어 집합, 시에르핀스키 삼각형, 페아노 곡선, 코흐 곡선 등 뿐만 아니라 구름, 산, 번개, 난류, 해안선, 나뭇가지 등 여러 자연물이나 도시 구획 등에서도 찾아볼 수 있으며 매우 불규칙한 물체들을 표현하는데에도 사용할 수 있습니다.
프랙탈은 컴퓨터 소프트웨어 등에서 재귀적이거나 반복적인 작업에 의해 만들어지기도 합니다. 프랙탈 기하학은 과학, 공학, 컴퓨터 예술, 인공지능, 시뮬레이션, 우주 분야 등 다양한 분야에 적용됩니다. 자세한 예로는 이미지 압축, 일정하게 변화하는 형태를 나타내는 프랙탈 시각 예술, 불규칙적인 자연 현상과 비슷한 형태로 여러 음악에 적용되기도 한다고 합니다.
이 세가지 영상은 알고리즘을 파이썬으로 구현해 제한 경로를 다르게 하며 경로에 도달할 수 있는지 확인한 과정입니다.
알고리즘을 코드로 구현하는 과정에서 정확하게 프랙탈을 사용하진 않았고 일정한 길이의 직선만 반복하도록 많들었습니다.
순서도를 이용해 나타낸 알고리즘을 설명하겠습니다.
시작을 하면 우선 특정 지점을 구분할 수 있도록 가로 세로로 검은 선과 제한 경로를 나타낼 빨간 선을 긋습니다. 그 후 지정한 좌표에서 선과 겹칠 때까지 앞으로 이동합니다.
선에 닿았을 때 빨간색이라면 좌표를 리스트에 저장하지 않고 검은색이라면 리스트에 저장한 뒤 각도를 바꾸어 리스트에 있는 이전 실행 다음 좌표로 이 과정을 반복합니다.
만약 목표 지점에 도착했다면 알고리즘을 종료합니다.
오른쪽의 사진은 알고리즘을 파이썬 코드로 구현한 모습입니다.
가능한 간단하게 구현하기 위해서 터틀 라이브러리 만을 사용했습니다.
Grid 함수는 최초 한번만 호출되며 가로 세로 선과 제한 경로를 그리고 터틀 각도를 설정합니다. 이후 main 부분에서 point 함수를 한번 호출해 xlist, ylist, dlist에 초기 값을 저장한 뒤
목표 경로에 도달할 때까지 이전 시행에서 얻은 좌표로 point 함수를 호출하고 리스트의 원소 순서를 나타내는 변수인 cnt를 1 증가시킵니다.
가장 핵심인 부분은 point 함수로 매 시행마다 입력된 지점에서 여러 방향(코드에선 시간상 세
방향)으로 선을 뻗으며 이 선이 검은 선에 도달하면 xlist, ylist에 추가하고 거리를 계산해 dlist 에 저장합니다. 빨간선에 닿았을 땐 저장하지 않고 다음 시행으로 넘어갑니다.
시간이나 효율성의 문제 때문에 이 코드에선 이동 거리가 일정 이하거나 뒤로 지나치게 많이 가는 경우 검은선에 도달해도 저장하지 않도록 만들었습니다.
떠올렸던 알고리즘을 코드로 구현하면서 정말 생각하던 대로 경로를 구하니 성취감을 느낄수 있었습니다. 하지만 구현하는 도구로 선택한 파이썬 터틀에서 색을 감지하기 위해 좌표 1씩만 움직이다 보니 굉장히 느렸고 매 시행마다 좌표와 거리를 저장하니 실행한지 좀 지나면 굉장히 리스트가 길어져 오류가 발생하는 경우도 많았습니다. 그리고 가장 아쉬웠던 점은 뻗는 방향을 셋으로만 제한하고 구상했던 것보다 지점 사이의 거리가 커서 최적 경로라는 목표랑 멀어졌던 점과 도달까진 했지만 경로를 출력하는데에는 어려움이 있다는 점입니다. 후에 다른 방식으로 이 알고리즘을 구현해 센서를 장착해 주변을 탐색할 수 있는 드론이나 차량 모형등에 적용해 자율 주행을 구현해 보고 싶습니다.
