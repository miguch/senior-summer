# 智能机器人技术第二次作业

**陈铭涛**

16340024

1. 由图，

   $\begin{bmatrix}v_x\\v_y \end{bmatrix} = \begin{bmatrix}-[l_1sin\theta_1+l_2sin(\theta_1+\theta_2)]\dot{\theta_1}-l_2sin(\theta_1+\theta_2)\dot{\theta_2}\\ [l_1cos\theta_1+l_2cos(\theta_1+\theta_2)]\dot{\theta_1}+l_2cos(\theta_1+\theta_2)\dot{\theta_2}\end{bmatrix}​$

   将表4.1数据代入得：

   $\begin{bmatrix}\dot{\theta_1}\\\dot{\theta_2} \end{bmatrix}_1 =\begin{bmatrix}-2 \\4  \end{bmatrix} ​$

   $\begin{bmatrix}\dot{\theta_1}\\\dot{\theta_2} \end{bmatrix}_2=\begin{bmatrix}-2\\0  \end{bmatrix} ​$

   $\begin{bmatrix}\dot{\theta_1}\\\dot{\theta_2} \end{bmatrix}_3 =\begin{bmatrix}-4 \\2\sqrt{3}+4 \end{bmatrix} $s

2. 平衡状态时机械手作用力$F=\begin{bmatrix}0\\mg \end{bmatrix}$

   各关节力矩$\tau=\begin{bmatrix}\tau_1\\\tau_2\\\tau_3\end{bmatrix}=J^TF$

   机械手断点位置$x,y​$与关节变量关系为：

   $\begin{cases}x=l_1cos\theta_1+l2cos(\theta_1+\theta_2)+l_3cos(\theta_1+\theta_2+\theta_3)=x(\theta_1,\theta_2,\theta_3)\\y=l_1sin\theta_1+l_2sin(\theta_1+\theta_2)+l_3sin(\theta_1+\theta_2+\theta_3)=y(\theta_1,\theta_2,\theta_3) \end{cases}$

   微分得：

   $J=\begin{bmatrix}\frac{\partial x}{\partial\theta_1}&\frac{\partial x}{\partial\theta_2}&\frac{\partial x}{\partial\theta_3}\\\frac{\partial y}{\partial\theta_1}&\frac{\partial y}{\partial\theta_2}&\frac{\partial y}{\partial\theta_3}\end{bmatrix}​$

   其中，

   $\frac{\partial x}{\partial\theta_1}=-l_1sin\theta_1-l_2sin(\theta_1+\theta_2)-l_3sin(\theta_1+\theta_2+\theta_3)$

   $\frac{\partial x}{\partial\theta_2}=-l_2sin(\theta_1+\theta_2)-l_3sin(\theta_1+\theta_2+\theta_3)$

   $\frac{\partial x}{\partial\theta_3}=-l_3sin(\theta_1+\theta_2+\theta_3)$

   $\frac{\partial y}{\partial\theta_1}=l_1cos\theta_1+l_2cos(\theta_1+\theta_2)+l_3cos(\theta_1+\theta_2+\theta_3)​$

   $\frac{\partial y}{\partial\theta_2}=l_2cos(\theta_1+\theta_2)+l_3cos(\theta_1+\theta_2+\theta_3)​$

   $\frac{\partial y}{\partial\theta_3}=l_3cos(\theta_1+\theta_2+\theta_3)$

   将关节变量代入得：

   $\tau=J^TF=​$

   