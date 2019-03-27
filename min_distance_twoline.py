
# 计算两条线段的最短距离
# 輸入綫段1（x11, y11）, （x12, y12）,
# 綫段2（x21, y21）, （x22, y22）

import math

def swap(x1, x2):
    return x2, x1

# 找最靠近交点的点
def min_di_point(x11, y11, x12, y12, met_point_x, met_point_y):
    if math.sqrt(math.pow(x11 - met_point_x, 2) + math.pow(y11 - met_point_y, 2)) > math.sqrt(
                    math.pow(x12 - met_point_x, 2) + math.pow(y12 - met_point_y, 2)):
        x1 = x12
        y1 = y12
    else:
        x1 = x11
        y1 = y11
    return x1, y1


def min_d(x11, y11, x12, y12, x21, y21, x22, y22):
    # 固定X11和X12 的大小值
    if x11 > x12:
        x11, x12 = swap(x11, x12)
        y11, y12 = swap(y11, y12)
    if x21 > x22:
        x21, x22 = swap(x21, x22)
        y21, y22 = swap(y21, y22)
    print(x11, y11, x12, y12, x21, y21, x22, y22)
    # y = A*x + B
    A1, B1, A2, B2 = 0, 0, 0, 0
    if x12 - x11==0:
        A1 = 0
        # print('A!:',A1)
    else:
        A1 = float((y12 - y11) / (x12 - x11) * 1.0)
    B1 = y11 - A1 * x11
    if x22 - x21==0:
        A2 = 0
    else:
        A2 = float((y22 - y21) / (x22 - x21) * 1.0)
    B2 = y21 - A2 * x21
    # 首先判断平行
    if A1 == A2:
        if A1 == 0:
            print('math.fabs(B1 - B2):',math.fabs(B1 - B2))
            return math.fabs(B1 - B2)
        else:
            return math.fabs(B1 - B2) / math.sqrt(math.pow(A1, 2) + math.pow(A2, 2))

    met_point_x = (B2 - B1) / (A1 - A2)
    met_point_y = A1 * met_point_x + B1
    # print('met_point:',met_point_x,met_point_y)
    # 其次判断是否存在交点
    if x11 <= met_point_x <= x12 and x21 <= met_point_x <= x22 and min(y11, y12) <= met_point_y <= max(y11,
                                                                                                       y12) and min(y21,
                                                                                                                    y22) <= met_point_y <= max(
            y21, y22):
        # print('good')
        return 0
    else:
        # 没有交点的计算二者的垂线交点是否在对方线条内，如果不在就求这两点的距离
        # 先用线段1的法向量
        x1, y1, x2, y2 = 0, 0, 0, 0
        x1, y1 = min_di_point(x11, y11, x12, y12, met_point_x, met_point_y)
        x2, y2 = min_di_point(x21, y21, x22, y22, met_point_x, met_point_y)
        result = []
        result.append(math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)))
        # 判断A是否为0
        # FA 法綫斜率
        # FA1, FB1, FA2, FB2 = 0, 0, 0, 0
        # cm 交點
        # cm1_x, cm1_y, cm2_x, cm2_y = 0, 0, 0, 0
        # A=0 --> y= B 法綫 x = x2
        if A1 == 0:
            # pass
            cm1_x = x2
            cm1_y = B1
            if x11 <= cm1_x <= x12 and min(y11, y12) <= cm1_y <= max(y11, y12):
                result.append(math.sqrt(math.pow(x2 - cm1_x, 2) + math.pow(y2 - cm1_y, 2)))
        else:
            FA1 = float(-1.0 / A1)
            FB1 = y2 - FA1 * x2
            #     计算线段1的法线与线段1的交点
            cm1_x = (FB1 - B1) / (A1 - FA1)
            cm1_y = A1 * cm1_x + B1
            if x11 <= cm1_x <= x12 and min(y11, y12) <= cm1_y <= max(y11, y12):
                result.append(math.sqrt(math.pow(x2 - cm1_x, 2) + math.pow(y2 - cm1_y, 2)))
        if A2 == 0:
            # pass
            cm2_x = x1
            cm2_y = B2
            if x21 <= cm2_x <= x22 and min(y21, y22) <= cm2_y <= max(y21, y22):
                result.append(math.sqrt(math.pow(x1 - cm2_x, 2) + math.pow(y1 - cm2_y, 2)))
        else:
            FA2 = float(-1.0 / A2)
            FB2 = y1 - FA2 * x1
            #     计算线段2的法线与线段2的交点
            cm2_x = (FB2 - B2) / (A2 - FA2)
            cm2_y = A2 * cm2_x + B2
            if x21 <= cm2_x <= x22 and min(y21, y22) <= cm2_y <= max(y21, y22):
                result.append(math.sqrt(math.pow(x1 - cm2_x, 2) + math.pow(y1 - cm2_y, 2)))

        return min(result)


if __name__ == '__main__':
    # res = min_d(0, 0, 1, 1, 0, 1, 1, 0)
    res = min_d(0, 0, 1, 0, 0, 1, 1, 1)
    print('result:', res)
