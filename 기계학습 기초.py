from imblearn.pipeline import sklearn_version
from sklearn import  datasets

#
d=datasets.load_iris() # iris 데이터셋을 읽고
# print(d.DESCR) #내용출력
#
# for i in range(0,len(d.data)):
#     print(i+1,d.data[i],d.target[i])

# 기계학습에서 데이터셋의 표현
# 샘플을 특징: 벡터와 레이블로 표현(특정 벡터는 x로 표기 )

# 모델링과 예측

# 훈련집합:기계 학습 모델을 학습하는데 쓰는 데이터로서 특징 벡터와 레이블 정보를 모두제공

# 테스트 집합: 학습을 마친 모델의 성능을 측정하는데 쓰는 데이터로서 예측할 때는 특징 벡터 정보만 제공.
# 예측 결과를 가지고 정확률을 측정할 때 레이블 정보를 사용

# from sklearn import svm
#
# s=svm.SVC(gamma=0.1,c=10) #SVM의  분류기 모델 SVC 클래스의 객체를 생성하여 s에저장
# s.fit(d.data,d.target) #객체 s의 fit 함수는 룬련 집합을 가지고 학습을 수행
# new_d= [[6.4,3.2,6.0,2.5],[7.1,3.1,4.7,1.35]]
# res=s.predict(new_d) #테스트 집합 # 객체 s의 predict 함수는 테스트 집합을 가지고 예측 수행
# print("새로운 2개의 샘플의 부류는 ",res)