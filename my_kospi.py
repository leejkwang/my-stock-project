import FinanceDataReader as fdr
import matplotlib.pyplot as plt

# 데이터를 야후 파이낸스에서 가져옵니다 (^KS11)
df = fdr.DataReader('^KS11', '2024-01-01', '2025-12-31')

# 데이터 저장 및 그래프 설정
df.to_csv('kospi_data.csv')
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Close'], color='blue', linestyle='--', marker='o')
plt.title('2025 KOSPI Index (Nov-Dec)')
plt.grid(True)
plt.savefig('kospi_graph.png')
print("성공! 데이터와 그래프 이미지가 만들어졌습니다.")
plt.show()
