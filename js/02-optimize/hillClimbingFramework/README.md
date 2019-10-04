# 通用的爬山演算法架構

* [hillClimbing.js](hillClimbing.js)

## 實作：通用的爬山演算法架構

* [hillClimbingNumber.js](hillClimbingNumber.js)
  * [solutionNumber.js](../solution/solutionNumber.js)

```
$ node .\hillClimbingNumber
s=energy(0.000)=4.000
0: energy(0.010)=4.000
1: energy(0.020)=4.000
4: energy(0.030)=3.999
6: energy(0.040)=3.998
9: energy(0.050)=3.998
...
409: energy(1.960)=0.158
410: energy(1.970)=0.119
412: energy(1.980)=0.080
414: energy(1.990)=0.040
415: energy(2.000)=0.000
solution: energy(2.000)=0.000
```

## 實例 2 ：多變數函數的最佳化

* [hillClimbingArray.js](hillClimbingArray.js)
  * [solutionArray.js](../solution/solutionArray.js)

```
$ node .\hillClimbingArray
s=energy( 1.000  1.000  1.000 )=1.000
1: energy( 1.000  0.990  1.000 )=0.970
3: energy( 1.010  0.990  1.000 )=0.950
4: energy( 1.010  0.990  1.010 )=0.921
5: energy( 1.020  0.990  1.010 )=0.901
6: energy( 1.030  0.990  1.010 )=0.881
...
710: energy( 2.000  0.500  2.450 )=-2.998
716: energy( 2.000  0.500  2.460 )=-2.998
726: energy( 2.000  0.500  2.470 )=-2.999
728: energy( 2.000  0.500  2.480 )=-3.000
729: energy( 2.000  0.500  2.490 )=-3.000
732: energy( 2.000  0.500  2.500 )=-3.000
solution: energy( 2.000  0.500  2.500 )=-3.000
```

## 實例 3 ：線性聯立方程組求解

注意：

1. 原本算法只會調一個軸，所以如果傾斜的方向才有更低點，就會因找不到更低而停止了。
2. 後來調成能改 n 個軸，所以如果45度的方向有更低點，就不會停止了。(但是如果不是 45度，那還是有可能找不到)
3. 也可以改成調整方向是任意的，但這樣會嘗試更多狀況。

(問題是：聯立方程式的能量函數 ( ()^2 + ()^2 ....+ ()^2 ) 會不會有多個低點呢?)


* [hillClimbingEquation.js](hillClimbingEquation.js)
  * [solutionEquations.js](../solution/solutionEquations.js)

```
$ node .\hillClimbingEquation
s=energy([0.000 0.000])=26.000
1: energy([0.000 0.010])=25.920
4: energy([0.000 0.020])=25.841
6: energy([0.000 0.030])=25.762
9: energy([0.010 0.030])=25.642
...
1190: energy([2.950 2.000])=0.005
1196: energy([2.960 2.000])=0.003
1197: energy([2.970 2.000])=0.002
1225: energy([2.980 2.000])=0.001
1231: energy([2.990 2.000])=0.000
1235: energy([3.000 2.000])=0.000
solution: energy([3.000 2.000])=0.000
```

## 實例 4 -- 排課系統

```
$ node .\hillClimbingScheduling.js

start: score=27.400
 A11:結構 A12:媒體 A13:機率 A14:演算 A15:線代 A16:　　 A17:
 A21:計概 A22:機率 A23:軟工 A24:演算 A25:媒體 A26:工數 A27:
 A31:視窗 A32:機率 A33:系統 A34:科學 A35:工數 A36:線代 A37:離散
 A41:視窗 A42:　　 A43:　　 A44:　　 A45:　　 A46:智慧 A47:行動
 A51:視窗 A52:演算 A53:計概 A54:視窗 A55:動畫 A56:動畫 A57:視窗
 B11:演算 B12:離散 B13:智慧 B14:網路 B15:結構 B16:智慧 B17:計概
 B21:電子 B22:嵌入 B23:科學 B24:離散 B25:結構 B26:媒體 B27:媒體
 B31:嵌入 B32:線代 B33:工數 B34:演算 B35:機率 B36:科學 B37:結構
 B41:　　 B42:軟工 B43:網路 B44:計概 B45:　　 B46:媒體 B47:視窗
 B51:網站 B52:行動 B53:演算 B54:網路 B55:網路 B56:嵌入 B57:演算
...
6: score=26.200
 A11:結構 A12:媒體 A13:機率 A14:演算 A15:線代 A16:　　 A17:
 A21:計概 A22:機率 A23:軟工 A24:演算 A25:媒體 A26:工數 A27:
 A31:視窗 A32:機率 A33:系統 A34:科學 A35:工數 A36:線代 A37:離散
 A41:　　 A42:　　 A43:　　 A44:　　 A45:　　 A46:智慧 A47:行動
 A51:視窗 A52:演算 A53:計概 A54:視窗 A55:動畫 A56:動畫 A57:視窗
 B11:演算 B12:離散 B13:智慧 B14:網路 B15:結構 B16:智慧 B17:計概
 B21:電子 B22:嵌入 B23:科學 B24:離散 B25:結構 B26:媒體 B27:媒體
 B31:嵌入 B32:線代 B33:工數 B34:演算 B35:機率 B36:科學 B37:結構
 B41:網站 B42:軟工 B43:網路 B44:計概 B45:　　 B46:網路 B47:視窗
 B51:　　 B52:行動 B53:演算 B54:媒體 B55:網路 B56:嵌入 B57:演算
...
234: score=5.900
 A11:網站 A12:電子 A13:網路 A14:結構 A15:嵌入 A16:線代 A17:網站
 A21:動畫 A22:科學 A23:媒體 A24:電子 A25:計概 A26:科學 A27:系統
 A31:　　 A32:　　 A33:視窗 A34:行動 A35:視窗 A36:演算 A37:演算
 A41:機率 A42:視窗 A43:網頁 A44:網頁 A45:計概 A46:計概 A47:離散
 A51:智慧 A52:媒體 A53:媒體 A54:機率 A55:工數 A56:軟工 A57:計概
 B11:嵌入 B12:離散 B13:離散 B14:網站 B15:嵌入 B16:電子 B17:網頁
 B21:結構 B22:結構 B23:網路 B24:軟工 B25:嵌入 B26:　　 B27:智慧
 B31:　　 B32:網路 B33:網頁 B34:智慧 B35:軟工 B36:行動 B37:行動
 B41:線代 B42:結構 B43:線代 B44:工數 B45:動畫 B46:系統 B47:系統
 B51:演算 B52:　　 B53:動畫 B54:電子 B55:工數 B56:　　 B57:動畫
...

2800: score=-1.100
 A11:　　 A12:媒體 A13:行動 A14:行動 A15:電子 A16:電子 A17:電子
 A21:線代 A22:線代 A23:結構 A24:計概 A25:離散 A26:演算 A27:演算
 A31:智慧 A32:系統 A33:系統 A34:線代 A35:科學 A36:科學 A37:演算
 A41:　　 A42:　　 A43:　　 A44:　　 A45:軟工 A46:軟工 A47:軟工
 A51:行動 A52:行動 A53:工數 A54:工數 A55:智慧 A56:機率 A57:機率
 B11:網路 B12:網路 B13:媒體 B14:媒體 B15:視窗 B16:視窗 B17:網頁
 B21:系統 B22:網頁 B23:視窗 B24:電子 B25:嵌入 B26:嵌入 B27:嵌入
 B31:　　 B32:　　 B33:網路 B34:動畫 B35:科學 B36:計概 B37:計概
 B41:　　 B42:網站 B43:網站 B44:網站 B45:結構 B46:網頁 B47:工數
 B51:　　 B52:離散 B53:離散 B54:智慧 B55:動畫 B56:動畫 B57:結構
....
solution: score=-4.000
 A11:　　 A12:結構 A13:結構 A14:結構 A15:媒體 A16:媒體 A17:媒體
 A21:　　 A22:智慧 A23:智慧 A24:智慧 A25:計概 A26:計概 A27:計概
 A31:　　 A32:嵌入 A33:嵌入 A34:嵌入 A35:視窗 A36:視窗 A37:視窗
 A41:　　 A42:行動 A43:行動 A44:行動 A45:系統 A46:系統 A47:系統
 A51:　　 A52:　　 A53:機率 A54:機率 A55:線代 A56:線代 A57:線代
 B11:　　 B12:軟工 B13:軟工 B14:軟工 B15:離散 B16:離散 B17:離散
 B21:　　 B22:工數 B23:工數 B24:工數 B25:網頁 B26:網頁 B27:網頁
 B31:　　 B32:網站 B33:網站 B34:網站 B35:網路 B36:網路 B37:網路
 B41:電子 B42:電子 B43:電子 B44:電子 B45:動畫 B46:動畫 B47:動畫
 B51:　　 B52:科學 B53:科學 B54:科學 B55:演算 B56:演算 B57:演算
```