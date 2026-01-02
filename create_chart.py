import FinanceDataReader as fdr
import matplotlib.pyplot as plt

# 데이터 가져오기 (야후 파이낸스 방식)
df = fdr.DataReader('^KS11', '2025-11-01', '2025-12-31')

# 그래프 그리기
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Close'], color='blue', linestyle='--', marker='o')
plt.title('2025 KOSPI Index (Web Version)')
plt.grid(True)

# 핵심: 웹사이트가 읽을 수 있도록 이미지로 저장
plt.savefig('kospi_web.png')
print("1단계 완료: 웹용 kospi_web.png 이미지가 생성되었습니다!")
