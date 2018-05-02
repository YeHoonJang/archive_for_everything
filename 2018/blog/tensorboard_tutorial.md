---
layout: post
title: "TensorBoard: Visualizing Learning"
date: 2018-04-30
tags: TensorBoard Tutorial
category: Tutorials
author: jangyehoon
---

이번 포스팅에서는 TensorBoard의 간단한 사용법에 대해 다양한 tensorflow를 활용한 예시 code와 함께 알아보도록 하겠습니다.
***

_TensorBoard 사용법에 대해 궁금해 하는 사람들 중 TensorFlow를 모르는 사람은 없을 거라 생각하지만 간단히 TensorFlow와 TensorBoard에 대해 살펴보고 Tutorial로 넘어가도록 하겠습니다 :-)_

## TensorFlow? TensorBoard?

### TensorFlow
TensorFlow는 Google의 인공지능 연구 조직인 Google Brain 팀이 기계학습(Machine Learning)과 심층 신경망(Deep Neural Network) 연구를 위해 개발한 오픈소스 소프트웨어 라이브러리입니다. TensorFlow는 데이터 플로우 그래프(Data Flow Graph) 방식을 사용하여 모델 내에서 수행되는 방대한 양의 연산과 데이터의 흐름을 표현합니다. 데이터 플로우 그래프는 수학연산을 나타내는 노드(node)와 그 노드들 간의 입/출력 관계를 나타내는 엣지(edge)로 구성되어 있으며, **TensorFlow**의 이름에서도 알 수 있듯이 다차원 데이터 배열인 Tensor는 이 엣지들을 통해 노드 간 흐름을 따릅니다.

### TensorBoard
TensorFlow는 매우 견고하면서도 유연한 아키텍처를 가지고 있어 별도의 코드 수정 없이 학습 모델을 설계할 수 있고 실행시킬 수 있습니다. 하지만 거대하고 복잡한 뉴럴넷의 코드만을 보고 계산과정이나 데이터의 흐름을 이해하기란 매우 추상적이며 복잡하고 난해할 수 있습니다. 디버깅과 최적화도 매우 어려운 작업이 될 수 있습니다. 이에 TensorFlow는 **TensorBoard**라는 시각화 툴을 통해 사용자들이 그래프 내에서 Tensor의 흐름을 쉽게 이해하고, 각 변수들의 양적 변화를 한 눈에 알 수 있도록 돕는 여러 기능을 제공합니다.

***
```{.python}
def sum(a, b):
    return a+b
```
