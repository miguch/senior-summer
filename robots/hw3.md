# 智能机器人技术第二次作业

**陈铭涛**

16340024

1. 断点位置约束$\begin{cases}\theta(0)=\theta_0\\\theta(t_f)=\theta_f\end{cases}, f=1,2,3 $

   速度约束$\begin{cases}\dot\theta(0)=\omega_0\\\dot\theta(t_f)=\omega_f\end{cases}, f=1,2,3 ​$

   则有$\begin{cases}\theta_0=a_0\\\theta_f=a_0+a_1t_f+a_2t_f^2+a_3t_f^3\\\omega_0=a_1\\\omega_f=a_1+2a_2t_f+3a_3t_f^2\end{cases}, f=1,2,3 $

   因此需要3个独立的多项式，

   求解得$\begin{cases}a_0=\theta_0\\a_1=\omega_0\\a_2=\frac3{t_f^2}(\theta_f-\theta_0)-\frac1{t_f}(2\omega_0+\omega_f)\\a_3=-\frac2{t_f^3}(\omega_f-\omega_0)+\frac1{t_f^2}(\omega_0+\omega_f)\end{cases}$

   共需要12个系数

2. （1）由条件代入公式得：

   $\begin{cases}a_0=5\\a_1=0\\a_3=\frac{255}{16}\\a_3=-\frac{85}{32}\end{cases}​$

   位置函数：

   $\theta(t)=5+15.9375t^2-2.65625t^3$

   求导得角速度与角加速度：

   $\dot\theta(t)=31.875t-7.96875t^2​$

   $\ddot\theta(t)=31.875-15.9375t$

   （2）角加速度值条件：

   $\ddot\theta\geq\frac{4(80-(-5))}{4^2}=21.25$

   设加速度$\ddot\theta=25$，则

   $t_a=\frac42-\frac{\sqrt{25^2\times4^2-4\times25\times(80-(-5))}}{2*25}=1.2254​$

   则轨迹终止点角速度与关节角度：

   $\dot\theta_{ta}=\ddot\theta t_a=30.635$

   $\theta_1=\theta_0+\frac12\ddot\theta t_a^2=32.5401$

   

   

   

   