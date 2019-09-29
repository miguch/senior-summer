# 智能机器人技术第一次作业

**陈铭涛**

16340024

4. （1）同一点但由基坐标系描述：$u'=Fu=8i+23j+3k​$

   （2）$\{F\}​$绕基坐标系$y​$轴旋转$90^\circ​$的旋转矩阵为 $Rot(y, 90^\circ)=\begin{bmatrix}
       0 & 0 &1 & 0\\0 &1 & 0 & 0\\-1 & 0 & 0 & 0\\0 & 0 & 0 & 1
   \end{bmatrix}​$ ，按$x​$轴方向平移20 的变换矩阵为$Trans(20, 0,0)=\begin{bmatrix} 1&0&0&20\\0&1&0&0\\0&0&1&0\\0&0&0&1 \end{bmatrix}​$，则变换所得坐标系$\{H\}=Trans(20,0,0)Rot(y,90^\circ)\{F\}=\begin{bmatrix} 0&0&1&21\\1&0&0&20\\0&1&0&-10\\0&0&0&1 \end{bmatrix}​$

5.  (1)![](images/1-1.png)

   (2) 连杆参数：

   | $i$  | $\alpha_{i-1}$ | $a_{i-1}$ | $d_i$ | $\theta_i$ |
   | ---- | -------------- | --------- | ----- | ---------- |
   | 1    | 0              | 0         | 0     | $\theta_1$ |
   | 2    | 0              | $L_1$     | 0     | $\theta_2$ |

   则连杆变换矩阵为：

   $A_n=Rot(z, \theta_n)Trans(0,0,d_n)Trans(a_n,0,0)Rot(x,\alpha_n)​$

   $=\begin{bmatrix}cos\theta_n&-sin\theta_n&0&0\\sin\theta_n&cos\theta_n&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}\begin{bmatrix}1&0&0&a_n\\0&1&0&0\\0&0&1&d_n\\0&0&0&1\end{bmatrix}\begin{bmatrix}1&0&0&0\\0&cos\alpha_n&-sin\alpha_n&0\\0&sin\alpha_n&cos\alpha_n&0\\0&0&0&1\end{bmatrix}​$ 

   $=\begin{bmatrix}cos\theta_n&-sin\theta_ncos\alpha_n&sin\alpha_nsin\theta_n&a_ncos\theta_n\\sin\theta_n&cos\theta_ncos\alpha_n&-sin\alpha_ncos\theta_n&a_nsin\theta_n\\0&sin\alpha_n&cos\alpha_n&d_n\\0&0&0&1\end{bmatrix}$

   带入得：

   $A_1=\begin{bmatrix}cos\theta_1&-sin\theta_1&0&0&\\sin\theta_1&cos\theta_1&0&0&\\0&0&1&0&\\0&0&0&1&\\\end{bmatrix}​$

   $A_2=\begin{bmatrix}cos\theta_2&-sin\theta_2&0&L_1*cos\theta_2&\\sin\theta_2&cos\theta_2&0&L_1*sin\theta_2&\\0&0&1&0&\\0&0&0&1&\\\end{bmatrix}​$

6.   连杆参数：

   | $i$  | $\alpha_{i-1}$ | $a_{i-1}$ | $d_i$ | $\theta_i$ |
   | ---- | -------------- | --------- | ----- | ---------- |
   | 1    | 0              | 0         | 0     | $\theta_1$ |
   | 2    | 0              | $d_2$     | 0     | 0          |

   运动方程：

   $T_2=A_1A_2$

   $A_1=\begin{bmatrix}cos\theta_1&-sin\theta_1&0&0&\\sin\theta_1&cos\theta_1&0&0&\\0&0&1&0&\\0&0&0&1&\\\end{bmatrix}​$

   $A_2=\begin{bmatrix}1&0&0&d_2&\\0&1&0&0&\\0&0&1&0&\\0&0&0&1&\\\end{bmatrix}​$

   则$T_2=A_1A_2=\begin{bmatrix}cos\theta_1&-sin\theta_1&0&d_2*cos\theta_1&\\sin\theta_1&cos\theta_1&0&d2*sin\theta_1&\\0&0&1&0&\\0&0&0&1&\\\end{bmatrix}​$

7.  各连杆D-H参数如下：

   | $i$  | $\alpha_{i-1}$ | $a_{i-1} $ | $d_i $ | $\theta_i$            |
   | ---- | -------------- | ---------- | ------ | --------------------- |
   | 1    | $0^\circ$      | 0          | 0      | $\theta_1(90^\circ)$  |
   | 2    | $-90^\circ$    | 0          | $d_2 $ | $\theta_2(0^\circ) $  |
   | 3    | $0^\circ$      | $a_2 $     | 0      | $\theta_3(-90^\circ)$ |
   | 4    | $-90^\circ $   | $a_3 $     | $d_4 $ | $\theta_4(0^\circ)$   |
   | 5    | $90^\circ$     | 0          | 0      | $\theta_5(0^\circ)$   |
   | 6    | $-90^\circ$    | 0          | 0      | $\theta_6(0^\circ)$   |

   由$A_n=Rot(z, \theta_n)Trans(0,0,d_n)Trans(a_n,0,0)Rot(x,\alpha_n)​$可得：

   $A_1=\begin{bmatrix}cos\theta_1&-sin\theta_1&0&0&\\sin\theta_1&cos\theta_1&0&0&\\0&0&1&0&\\0&0&0&1&\\\end{bmatrix}​$

   $ A_2=\begin{bmatrix}cos\theta_2&0&-1.0*sin\theta_2&0&\\sin\theta_2&0&1.0*cos\theta_2&0&\\0&-1&0&d2&\\0&0&0&1&\\\end{bmatrix}$

   $ A_3=\begin{bmatrix}cos\theta_3&-sin\theta_3&0&a2*cos\theta_3&\\sin\theta_3&cos\theta_3&0&a2*sin\theta_3&\\0&0&1&0&\\0&0&0&1&\\\end{bmatrix}$

   $ A_4=\begin{bmatrix}cos\theta_4&0&-1.0*sin\theta_4&a3*cos\theta_4&\\sin\theta_4&0&1.0*cos\theta_4&a3*sin\theta_4&\\0&-1&0&d4&\\0&0&0&1&\\\end{bmatrix}$

   $ A_5=\begin{bmatrix}cos\theta_5&0&1.0*sin\theta_5&0&\\sin\theta_5&0&-1.0*cos\theta_5&0&\\0&1&0&0&\\0&0&0&1&\\\end{bmatrix} ​$

   $A_6=\begin{bmatrix}cos\theta_6&0&-1.0*sin\theta_6&0&\\sin\theta_6&0&1.0*cos\theta_6&0&\\0&-1&0&0&\\0&0&0&1&\\\end{bmatrix}  $

   则运动学方程$$T_6=A_1A_2A_3A_4A_5A_6=\begin{bmatrix}0&1&0&-d_4&\\0&0&1&0&\\1&-0&-0&a_2 +a_3 + d_2 + d_4&\\0&0&0&1&\\\end{bmatrix} $$

   

   

