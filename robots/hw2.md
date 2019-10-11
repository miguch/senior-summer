# 智能机器人技术第二次作业

**陈铭涛**

16340024

1. 由图，

   $\begin{bmatrix}v_x\\v_y \end{bmatrix} = \begin{bmatrix}-[l_1sin\theta_1+l_2sin(\theta_1+\theta_2)]\dot{\theta_1}-l_2sin(\theta_1+\theta_2)\dot{\theta_2}\\ [l_1cos\theta_1+l_2cos(\theta_1+\theta_2)]\dot{\theta_1}+l_2cos(\theta_1+\theta_2)\dot{\theta_2}\end{bmatrix}​$

   将表4.1数据代入得：

   $\begin{bmatrix}\dot{\theta_1}\\\dot{\theta_2} \end{bmatrix}_1 =\begin{bmatrix}-2 \\4  \end{bmatrix} ​$

   $\begin{bmatrix}\dot{\theta_1}\\\dot{\theta_2} \end{bmatrix}_2=\begin{bmatrix}-2\\0  \end{bmatrix} ​$

   $\begin{bmatrix}\dot{\theta_1}\\\dot{\theta_2} \end{bmatrix}_3 =\begin{bmatrix}-4 \\2\sqrt{3}+6 \end{bmatrix} $

2. 平衡状态时机械手作用力$F=\begin{bmatrix}0\\mg \end{bmatrix}$

   各关节力矩$\tau=\begin{bmatrix}\tau_1\\\tau_2\\\tau_3\end{bmatrix}=J^TF​$

   机械手断点位置$x,y​$与关节变量关系为：

   $\begin{cases}x=l_1cos\theta_1+l2cos(\theta_1+\theta_2)+l_3cos(\theta_1+\theta_2+\theta_3)=x(\theta_1,\theta_2,\theta_3)\\y=l_1sin\theta_1+l_2sin(\theta_1+\theta_2)+l_3sin(\theta_1+\theta_2+\theta_3)=y(\theta_1,\theta_2,\theta_3) \end{cases}​$

   微分得：

   $J=\begin{bmatrix}\frac{\partial x}{\partial\theta_1}&\frac{\partial x}{\partial\theta_2}&\frac{\partial x}{\partial\theta_3}\\\frac{\partial y}{\partial\theta_1}&\frac{\partial y}{\partial\theta_2}&\frac{\partial y}{\partial\theta_3}\end{bmatrix}​$

   其中，

   $\frac{\partial x}{\partial\theta_1}=-l_1sin\theta_1-l_2sin(\theta_1+\theta_2)-l_3sin(\theta_1+\theta_2+\theta_3)$

   $\frac{\partial x}{\partial\theta_2}=-l_2sin(\theta_1+\theta_2)-l_3sin(\theta_1+\theta_2+\theta_3)$

   $\frac{\partial x}{\partial\theta_3}=-l_3sin(\theta_1+\theta_2+\theta_3)​$

   $\frac{\partial y}{\partial\theta_1}=l_1cos\theta_1+l_2cos(\theta_1+\theta_2)+l_3cos(\theta_1+\theta_2+\theta_3)​$

   $\frac{\partial y}{\partial\theta_2}=l_2cos(\theta_1+\theta_2)+l_3cos(\theta_1+\theta_2+\theta_3)​$

   $\frac{\partial y}{\partial\theta_3}=l_3cos(\theta_1+\theta_2+\theta_3)​$

   将关节变量代入得：

   $\tau=J^TF=\begin{bmatrix}-0.4\sqrt3-0.4&0.4+0.8\\-0.4&0.8\\-0.4&0\end{bmatrix}\begin{bmatrix}0\\10g\end{bmatrix}=\begin{bmatrix}12g\\8g\\0\end{bmatrix}​$

3. 力矩$\tau_1=\frac{d}{dt}\frac{\partial L}{\partial \dot{\theta_1}}-\frac{\partial L}{\partial \theta_1}\\=(m_1p_1^2+m_2p_2^2+m_2l_1^2+2m_2l_1p_2c_2)\ddot{\theta_1}+(m_2p_2^2+m_2l_1p_2c_2)\ddot{\theta_2}+(-2m_2l_1p_2s_2)\dot\theta_1\dot\theta_2\\+(-m_2l_1p_2s_2)\dot\theta_2^2+(m_1p_1+m_2l_1)gs_1+m_2gp_2s_{12}\\=D_{11}\ddot{\theta_1}+D_{12}\ddot\theta_2+D_{112}\dot\theta_1\dot\theta_2+D_{122}\dot\theta_2^2+D_1$

   由此得，

   $\begin{cases}D_{11}=m_1p_1^2+m_2p_2^2+m_2l_1^2+2m_2l_1p_2c_2\\D_{12}=m_2p_2^2+m_2l_1p_2c_2\\D_{112}=-2m_2l_1p_2s_2\\D_{122}=-m_2l_1p_2s_2\\D_1=(m_1p_1+m_2l_1)gs_1+m_2p_2gs_{12}\end{cases}$

   $\tau_2=\frac{d}{dt}\frac{\partial L}{\partial \dot\theta_2}-\frac{\partial L}{\partial \theta_2}\\=(m_2p_2^2+m_2l_1p_2c_2)\ddot\theta_1+m_2p_2^2\ddot\theta_2+(m_2l_1p_2s_2-m_2l_1p_2s_2)\dot\theta_1\dot\theta_2+(m_2l_1p_2s_2)\dot\theta_1^2+m_2gp_2s_{12}\\=D_{21}\ddot\theta_1+D_{22}\ddot\theta_2+D_{212}\dot\theta_1\dot\theta_2+D_{211}\dot\theta_1^2+D_2​$

   $\begin{cases}D_{21}=m_2p_2^2+m_2l_1p_2c_2\\D_{22}=m_2p_2^2\\D_{212}=-m_2l_1p_2s_2+m_2l_1p_2s_2=0\\D_{211}=m_2l_1p_2s_2\\D_2=m_2gp_2s_{12}\end{cases}$

4. 连杆1动能：

   $E_{k1}=\frac12m_1l_1^2\theta_1^2$

   连杆2质心位置：

   $x_2=l_1c_1+l_2c_{12}\\y_2=l_1s_1+l_2s_12​$

   质心速度平方：

   $\dot x_2=-l_1s_1\dot \theta_1-l_2s_{12}(\dot \theta_1+\dot \theta_2)​$

   $\dot y_2=l_1c_1\dot \theta_1+l_2c_{12}(\dot \theta_1+\dot \theta_2)$

   $\dot x_2^2+\dot y_2^2=l_1^2\dot \theta_1^2+l_2^2(\dot \theta_1+\dot \theta_2)^2+2(l_1l_2\dot \theta_1(\dot \theta_1+\dot \theta_2))c_2​$

   动能：

   $E_{k2}=\frac12m_2l_1^2\dot \theta_1^2+\frac12m_2l_2^2(\dot \theta_1+\dot \theta_2)^2+m_2l_1l_2\dot \theta_1(\dot \theta_1+\dot \theta_2)c_2​$

   连杆3质心位置：

   $\dot x_3=\dot x_2\\\dot y_3=\dot y_2$

   速度平方：

   $\dot x_3^2+\dot y_3^2=\dot x_2^2+\dot y_2^2​$

   动能：

   $E_{k3}=\frac12m_3l_1^2\dot \theta_1^2+\frac12m_3l_2^2(\dot \theta_1+\dot \theta_2)^2+m_3l_1l_2\dot \theta_1(\dot \theta_1+\dot \theta_2)c_2​$

   总动能：

   $E_k=\sum_{i=1}^3E_{ki}\\=\frac12(m_1+m_2+m_3)l_1^2\dot\theta_1^2+(m_2+m_3)(\frac12l_2^2(\dot \theta_1+\dot \theta_2)^2+l_1l_2\dot \theta_1(\dot \theta_1+\dot \theta_2)c_2)$

   系统总势能：

   $E_{p}=m_1gl_1s_1+m_2g(l_1s_1+l_2s_{12})+m_3g(l_1s_1+l_2s_{12})$

   代入拉格朗日函数：

   $L=E_k-E_p$

   $\frac{\partial L}{\partial \dot\theta_1}=(m_1+m_2+m_3)l_1^2\dot\theta_1+(m_2+m_3)(l_2^2\dot\theta_1+l_2^2\dot\theta_1\dot\theta_2+2l_1l_2c_2\dot\theta_1+l_1l_2c_2\dot\theta_2) ​$

   $\frac{\partial L}{\partial \theta_1}=(m_1+m_2)gl_1c_1+m_2gl_2c_{12}+m_3g(l_1c_1+l_2c_{12})$

   动力学方程：

   $\tau_1=\frac{d}{dt}\frac{\partial L}{\partial \dot\theta_1}-\frac{\partial L}{\partial \theta_1}\\=(m_1+m_2+m_3)l_1^2\ddot\theta_1+(m_2+m_3)(l_2^2\ddot\theta_1+l_2^2\ddot\theta_1\dot\theta_2+l_2^2\dot\theta_1\ddot\theta_2+2l_1l_2c_2\ddot\theta_1+l_1l_2c_2\ddot\theta_2)\\=2.8\ddot\theta_1+0.825(\ddot\theta_1\dot\theta_2+\dot\theta_1\ddot\theta_2+c_2\dot\theta_2)+1.65c_2\dot\theta_1$

   $\tau_2=\frac{d}{dt}\frac{\partial L}{\partial \dot\theta_2}-\frac{\partial L}{\partial \theta_2}​$

   $\tau_3=\frac{d}{dt}\frac{\partial L}{\partial \dot\theta_3}-\frac{\partial L}{\partial \theta_3}$

   

