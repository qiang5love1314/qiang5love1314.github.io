---
permalink: /
title: ""
excerpt: ""
author_profile: true
layout: default
title: news
news:
- "2025.7: 🎉🎉 Good news! A paper has been accepted by ICONIP (CCF C)."
- "2025.7: 🎉🎉 Good news! A paper has been accepted by ECAI (CCF B)."
- "2025.6: 🎉🎉 Good news! Two papers have been accepted by Software Guide (CCF C)."
- "2025.6: Invited to give a talk at the Chinese Institute of Electronics Excellent PhD Forum on \"Intelligent Indoor Localization Theory and Methods for Integrated Sensing and Communication.\""
- "2025.6: 🎉🎉 Good news! Two papers have been accepted by IEEE UIC (CCF C)."
- "2025.5: 🎉🎉 Good news! A paper has been accepted by ICWS (CCF B)."
- "2025.5: 🎉🎉 Good news! Two undergraduate innovation projects under my supervision have been recognized as National-level and Beijing municipal-level projects, respectively."
- "2025.4: 🎉🎉 Good news! A paper has been accepted by NETINFO SECURITY (CCF C)."
- "2025.3: 🎉🎉 Good news! Two papers have been accepted by Computer Education (CCF B) and ICC workshop (CCF C)."
- "2025.1: 🎉🎉 Good news! One of our team's papers has been accepted by SCIENCE CHINA Information Sciences (CCF A)."
- "2024.12: 🎉🎉 Good news! Two of our team's papers have been accepted by IEEE TCCN."
- "2024.12: 🎉🎉 Good news! One of our team's papers has been accepted by the 2025 IEEE INFOCOM (CCF A)."
- "2024.10: 🎉🎉 Good news! IEEE TBD has accepted my paper."
- "2024.10: I have been exceptionally selected as a master's supervisor."
- "2024.10: 🎉🎉 Good news! IEEE SmartIoT has accepted one paper, and two papers have been accepted by IEEE MSN (CCF C)."
- "2024.08: 🎉🎉 Good news! I have been awarded a grant under the National Natural Science Foundation of China, Youth Program."
- "2024.07: 🎉🎉 Good news! My paper has been accepted by IEEE COMST, the highest impact factor (35.6) in all the IEEE journals."
- "2024.06: 🎉🎉 Good news! I have been awarded a grant under the National Postdoctoral Program."
- "2024.05: I have supervised five groups of students on undergraduate innovation and entrepreneurship projects, covering areas such as signal prediction and sensing, behavior recognition, and cryptographic system design."
- "2024.03: 🎉🎉 Good news! Received the minor version from IEEE COMST."
- "2024.02: 🎉🎉 I have been awarded a key project grant from the Shandong Academy of Sciences Open Project."
- "2024.01: 🎉🎉 I have received recognition for the Excellent Completion of the Ministry of Education's Teaching Reform Project, Rank 2."
- "2023.12: 🎉🎉 I have been awarded a grant under the National Postdoctoral Program for Innovative Talents."
- "2023.09: I am going to open the sources of the activity recognition datasets, which include running, jumping, walking, sit down, pick up, etc. More than 10 different kinds of activities."
- "2023.06: I finished the first research at Beijing Jiaotong University, which focuses on privacy protection."
- "2023.03: 🎉🎉 I have been selected for the Beijing Jiaotong University Youth Talent Cultivation Program, Class II."
- "2023.02: 🎉🎉 I started working as a lecturer at the School of Software Engineering, Beijing Jiaotong University. I am looking forward to the future with great anticipation."
- "2022.12: 🎉🎉 I finished my PhD thesis defense."
- "2022.04: I left the ETH Zurich. I am most sincerely grateful for the great support, understanding, and involvement in the lab."
- "2022.03: I decided to make all the datasets and codes open source for my PhD research. I hope they can be helpful to everyone. You can find them at <a href=\"https://github.com/qiang5love1314\"><font color=\"blue\"> my Github</font></a>."
- "2022.03: 🎉🎉 Good news! IEEE TNSE has accepted my paper."
- "2021.11: 🎉🎉 Good news! IEEE TMC has accepted my paper."
- "2021.04: I got my work contract and will study at ETH Zurich for one year."

redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
# 🧑‍🏫  About me
I received the Ph.D. degree in software engineering from Tianjin University, China, in 2022, and the M.S. degree in computer science from Dalian University of Technology, China, in 2018. I was a jointly doctoral student at ETH Zurich, Switzerland with CSC funding in 2021. 

I am currently a Lecturer with the School of Cyberspace Science and Technology, <a href="https://www.bjtu.edu.cn/">Beijing Jiaotong University, China</a>. My primary research interests lie in Machine Learning, Privacy Protection, and the Internet of Things (IoT). Additionally, I engage in research related to Computer Vision, focusing on encryption algorithms based on chaos theory. My passion for leveraging artificial intelligence to address and solve real-world problems drives my work. 

I am committed to fostering collaboration and knowledge-sharing within the academic community. By integrating interdisciplinary approaches, I strive to contribute to the evolution of intelligent systems and their applications in solving complex challenges.

# 🔥 News
<ul>
  {% for item in page.news limit:10 %}
  <li>{{ item }}</li>
  {% endfor %}
</ul>

<button onclick="toggleNews()" style="background-color: #6C757D; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Show more news</button>


<ul id="more-news" style="display:none;">
  {% for item in page.news offset:10 %}
  <li>{{ item }}</li>
  {% endfor %}
</ul>

<script>
function toggleNews() {
  var moreNews = document.getElementById("more-news");
  if (moreNews.style.display === "none") {
    moreNews.style.display = "block";
  } else {
    moreNews.style.display = "none";
  }
}
</script>

# 📖 Educations
Ph. D., Software Engineering, <a href="http://www.tju.edu.cn/">Tianjin University, China</a>, 09.2018 - 12.2022
- Member of Tianjin Key Laboratory of Advanced Networking, supervised by Prof. Tie Qiu and Prof. Wenyu Qu
- Research Topic: Artificial Intelligence, Internet of Things, Indoor Localization
- Thesis Title: "Lightweight Intelligent Indoor Localization Algorithm Based on CSI Fingerprint Signal"

Jointly Doctoral Student, Computer Science, <a href="https://ethz.ch/en.html">ETH Zurich, Switzerland</a>, 04.2021 - 04.2022
- The state-sponsored student with financial support from China Scholarship Council
- Member of D-ITET Center for Integrated Systems Laboratory, supervised by Dr. Michele Magno and IEEE/ACM Fellow. Prof. Luca Benini
- Project: "mmWave Sensors For Indoor Localization and Tracking"

M.S., Computer Science, <a href="https://www.dlut.edu.cn/">Dalian University of Technology, China</a>, 09.2016 - 07.2018
- Postgraduate Recommendation, supervised by Prof. Xingyuan Wang (World's Top 2% Scientists)
- Research Topic: Image Processing, Encryption Algorithm, Chaos Theory
- Thesis Title: "Image Encryption Algorithm Based on Multiple Mixed Hash Functions"

# 🎓 Fundings
- 北京交通大学研究生教改项目，《软件缺陷检测与可信评估实践》课程思政示范课程建设项目，No. YJSSQ20250022，3万，2025-2027，主持
- 国家自然科学基金——青年科学基金项目，基于生成式网络的智能信道状态信息通感模型研究，No. 62401037，30万，2025-2027，主持
- 中国博士后科学基金——面上项目，面向信道状态信息的轻量级智能通感一体化关键技术研究，No. 2024M750166，8万，2024-2026，主持
- 国家资助博士后研究人员计划，面向安全应用的智能通感一体化关键技术研究，No. GZC20230224，24万，2024-2025，主持
- 山东省科学院开放课题重点项目，面向智能通感算融合网络的关键技术研究，No. 2023ZD039，10万，2024-2026，主持
- 北京交通大学自然科学类人才基金项目，面向无线信号的智能感知鲁棒性与安全性研究，No. 2023XKRC016，20万，2023-2026，主持

# 📝 Publications 
<!-- <div class='paper-box-text' markdown="1"> -->
## Published Papers
1. <p> <span style="color: #FF0000;">[CCF C]</span> S. Hu, W. Yu, J. Liu, Z. Ji, <b><span style="color: #4682b4;">X. Zhu*</span></b>, et al. "DTSAT-DRQN: A Novel DRQN-Enhanced Chaos Communication Strategy with Dual-TCN", <b><i>ICONIP</i></b>, 2025.</p>
2. <p> <span style="color: #FF0000;">[CCF B]</span> X. Xin, C. Liu, C. Wang, L. An, <b><span style="color: #4682b4;">X. Zhu</span></b>. "QGA-CDM: A Dynamic Cognitive Diagnosis Model with Genetic Algorithm-Enhanced Q-Matrix", <b><i><span style="color: #4682b4;">ECAI</span></i></b>, 2025.</p>
3. <p> <span style="color: #FF0000;">[CCF C]</span> 乔子轩, 谢雨桐, 姚苏眩, <b><span style="color: #4682b4;">朱晓强*</span></b>, 姚英英. "基于混沌系统和机器学习的医学图像加密算法", <b><i><span style="color: #4682b4;">软件导刊</span></i></b>, 2025, 1-18.</p>
4. <p> <span style="color: #FF0000;">[CCF C]</span> 刘吉强, 任城仪, <b><span style="color: #4682b4;">朱晓强*</span></b>, 王健. "基于三维混沌系统与Hopfield神经网络的彩色图像加密算法", <b><i><span style="color: #4682b4;">软件导刊</span></i></b>, 2025, 1-17.</p>
5. <p> <span style="color: #FF0000;">[CCF C]</span> H. Liu, X. Jiang, Z. Ji, <b><span style="color: #4682b4;">X. Zhu</span></b>. "YOLOv7-AFDH: an Anchor-Free and Decoupled-Head Based Object Detection Model", <b><i><span style="color: #4682b4;">IEEE UIC</span></i></b>, 2025.</p>
6. <p> <span style="color: #FF0000;">[CCF C]</span> W. Zhang, Z. Ji, J. Dai, <b><span style="color: #4682b4;">X. Zhu</span></b>, et. al. "A FAN-Enhanced iTransformer Model for Cold Chain Logistics Demand Forecasting", <b><i><span style="color: #4682b4;">IEEE UIC</span></i></b>, 2025.</p>
7. <p> <span style="color: #FF0000;">[CCF B]</span> P. Yuan, Y. Pei, C. Wang, X. Zhao, Z. Liu, <b><span style="color: #4682b4;">X. Zhu</span></b>, T. Taleb. "GCA-YOLO: An Edge-optimized Traffic Sign Detection Model", <b><i><span style="color: #4682b4;">ICWS</span></i></b>, 2025, 1-10.</p>
8. <p> <span style="color: #FF0000;">[CCF C]</span> <b><span style="color: #4682b4;">朱晓强*</span></b>, 张皓文, 林彦孜, 刘吉强. "基于可信数字身份的轻量级分布式认证方案", <b><i><span style="color: #4682b4;">信息网络安全</span></i></b>, 2025, 1-14.</p>
9. <p> <span style="color: #FF0000;">[CCF C]</span> M. Zhang, L. Lu, A. Ullah, <b><span style="color: #4682b4;">X. Zhu*</span></b>, et al. "BLINK: An Effective Indoor Localization Method Based on CSI by Broad Learning and Kolmogorov-Arnold Network", <b><i><span style="color: #4682b4;">IEEE ICC workshop</span></i></b>, 2025.</p>
10. <p> <span style="color: #FF0000;">[CCF B]</span> 赵宏, 冯凤娟, <b><span style="color: #4682b4;">朱晓强</span></b>. "融合知识传授、价值引领的数据结构课程思政建设", <b><i><span style="color: #4682b4;">计算机教育</span></i></b>, 2025, 362(02): 66-69+74.</p>
11. <p> <span style="color: #FF0000;">[CCF A]</span> 张皓文, <b><span style="color: #4682b4;">朱晓强*</span></b>, 张焘, 等. "CreChain实现IIoT高效安全交易：一种基于信用机制的分布式账本模型", <b><i><span style="color: #4682b4;">中国科学：信息科学</span></i></b>, 2024, 1-17, DOI: 10.1360/SSI-2024-0281.</p>
12. <p> <span style="color: #FF0000;">[1区]</span> <b><span style="color: #4682b4;">X. Zhu</span></b>, J. Liu, T. Zhang, et al. "CPPU: Policy Space Diversity for Informative Path Planning and GAI-enabled Updating CSI in ISAC", <b><i><span style="color: #4682b4;">IEEE TCCN</span></i></b>, 2024, 1-14, DOI: 10.1109/TCCN.2024.3522088.</p>
13. <p> <span style="color: #FF0000;">[1区]</span> W. Feng, R. Zhang, Y. Zhu, C. Wang, C. Sun, <b><span style="color: #4682b4;">X. Zhu</span></b>, X. Li, T. Taleb. "Exploring Collaborative Diffusion Model Inferring for AIGC-enabled Edge Services", <b><i><span style="color: #4682b4;">IEEE TCCN</span></i></b>, 2024, 1-14, DOI: 10.1109/TCCN.2024.3519320.</p>
14. <p> <span style="color: #FF0000;">[CCF A]</span> R. Lin, B. Liu, Y. Cui, D. Liu, R. Gao, <b><span style="color: #4682b4;">X. Zhu</span></b>, J. Liu, L. Li. "LuminaLink: Enabling Low Cost Secure Visible Light Communication with Birefringence", <b><i><span style="color: #4682b4;">IEEE INFOCOM</span></i></b>, 2025.</p>
15. <p> <span style="color: #FF0000;">[2区]</span> <b><span style="color: #4682b4;">X. Zhu</span></b>, W. Qu, T. Qiu, et al. "Dynamic Radio Map Construction with Minimal Manual Intervention: A State Space Model-Based Approach with Imitation Learning", <b><i><span style="color: #4682b4;">IEEE TBD</span></i></b>, 2024, 1-13, DOI: 10.1109/TBDATA.2024.3489425.</p>
16. <p> <span style="color: #FF0000;">[CCF C]</span> S. Hu, C. Zhang, J. Liu, <b><span style="color: #4682b4;">X. Zhu*</span></b>, L. Li. "Proto-CSNet: A Prototype Network Model Integrating CNN and Self-Attention for Enhanced Human Activity Recognition", <b><i><span style="color: #4682b4;">IEEE MSN</span></i></b>, 2024.</p>
17. <p> <span style="color: #FF0000;">[CCF C]</span> M. Zhang, L. Lu, <b><span style="color: #4682b4;">X. Zhu*</span></b>, L. Li, R. Gao. "DBLG: An Innovative Deep-Broad Learning and GAN Framework for CSI Fingerprint Database Refinement", <b><i><span style="color: #4682b4;">IEEE MSN</span></i></b>, 2024.</p>
18. <p> [EI] <b><span style="color: #4682b4;">X. Zhu</span></b>, J. Liu, D. Zhang, et al. "Enhancing Patient Privacy in IoT-Enabled Intelligent Medical Systems: A Deep and Broad Learning-Based Efficient Encryption Network", <b><i><span style="color: #4682b4;">IEEE SmartIoT</span></i></b>, 2024, 51-58.</p>
19. <p> <span style="color: #FF0000;">[1区, IF: 46.7]</span> <b><span style="color: #4682b4;">X. Zhu</span></b>, J. Liu, L. Lu, et al. "Enabling Intelligent Connectivity: A Survey of Secure ISAC in 6G Networks", <b><i><span style="color: #4682b4;">IEEE COMST</span></i></b>, 2024, 1-34, DOI: 10.1109/COMST.2024.3432871.</p>
20. <p> <span style="color: #FF0000;">[CCF A]</span> <b><span style="color: #4682b4;">X. Zhu</span></b>, T. Qiu, W. Qu, et al. "Path Planning for Adaptive CSI Map Construction with A3C in Dynamic Environments", <b><i><span style="color: #4682b4;">IEEE TMC</span></i></b>, 2023, 22(5): 2925-2937.</p>
21. <p> <span style="color: #FF0000;">[CCF A]</span> <b><span style="color: #4682b4;">X. Zhu</span></b>, T. Qiu, W. Qu, et al. "BLS-Location: A Wireless Fingerprint Localization Algorithm Based on Broad Learning", <b><i><span style="color: #4682b4;">IEEE TMC</span></i></b>, 2023, 22(1): 115-128.</p>
22. <p> <span style="color: #FF0000;">[2区]</span> <b><span style="color: #4682b4;">X. Zhu</span></b>, W. Qu, X. Zhou, et al. "Intelligent Fingerprint-based Localization Scheme using CSI Images for Internet of Things". <b><i><span style="color: #4682b4;">IEEE TNSE</span></i></b>, 2022, 9(4): 2378-2391.</p>
23. <p> <span style="color: #FF0000;">[1区, IF: 35.6]</span> <b><span style="color: #4682b4;">X. Zhu</span></b>, W. Qu, T. Qiu, et al. "Indoor intelligent fingerprint‑based localization: Principles, approaches and challenges", <b><i><span style="color: #4682b4;">IEEE COMST</span></i></b>, 2020, 22(4): 2634‑2657.</p>
24. <p> <span style="color: #FF0000;">[2区]</span> X. Wang, Y. Wang, <b><span style="color: #4682b4;">X. Zhu</span></b>, et al. "A novel chaotic algorithm for image encryption utilizing one-time pad based on pixel level and DNA level", <b><i><span style="color: #4682b4;">Opt Lasers Eng</span></i></b>, 2020, 125: 105851.</p>
25. <p> <span style="color: #FF0000;">[2区]</span> X. Wang, Y. Wang, <b><span style="color: #4682b4;">X. Zhu</span></b>, et al. "Image encryption scheme based on Chaos and DNA plane operations", <b><i><span style="color: #4682b4;">Multimed Tools Appl</span></i></b>, 2019, 78(18): 26111‑26128.</p>
26. <p> <span style="color: #FF0000;">[2区]</span> X. Wang, <b><span style="color: #4682b4;">X. Zhu</span></b>, X. Wu, et al. "Image encryption algorithm based on multiple mixed hash functions and cyclic shift", <b><i><span style="color: #4682b4;">Opt Lasers Eng</span></i></b>, 2018, 107: 370‑379.</p>
27. <p> <span style="color: #FF0000;">[2区]</span> X. Wang, <b><span style="color: #4682b4;">X. Zhu</span></b>, Y. Zhang, et al. "An image encryption algorithm based on Josephus traversing and mixed chaotic map", <b><i><span style="color: #4682b4;">IEEE Access</span></i></b>, 2018, 6: 23733‑23746.</p>
28. <p> <span style="color: #FF0000;">[CCF A]</span> 王春鹏, 王兴元, 张川, <b><span style="color: #4682b4;">朱晓强</span></b>, 夏之秋. "基于三元数极谐-Fourier矩和混沌映射的立体图像零水印算法",<b><i><span style="color: #4682b4;">中国科学：信息科学</span></i></b>, 2018, 1: 79‑99.</p>

## 📚 Book
1. <p> <span style="color: #FF0000;">[Whole Book]</span> <b><span style="color: #4682b4;">X. Zhu</span></b>, Y. Liu, C. Wang. "Intelligent Localization for Integrated Sensing and Communication", <b><i><span style="color: #4682b4;">Springer Nature</span></i></b>, ISBN: 978-981-96-9384-9, 2025. </p>

## Under Review Papers
1. <p> [CCF A] W. Kong, Z. Ji, X. Zhang, Z. Xiong, <b>X. Zhu</b>, J. Liu. "From Ill-Posed to Well-Posed: Federated Uncertainty Aware Learning via Constrained Inference", <b><i>AAAI</i></b>, 2026.</p>
2. <p> [CCF A] R. Tian, C. Li, Y. Xin, H. Wu, D. Liu, F. Dang, R. Gao, <b>X. Zhu</b>, L. Li. "CE-AdaSAC: Real-Time Cloud-Edge Inference with Adaptive Self-Pruning and Fast Deployment", <b><i>IEEE INFOCOM</i></b>, 2026.</p>
3. <p> [CCF A] X. Chen, C. Chen, H. Xing, <b>X. Zhu</b>. "DKD-FedAgg: Personalized and Mobility-Aware Agglomerative Federated Learning in End-Edge-Cloud Systems", <b><i>IEEE INFOCOM</i></b>, 2026.</p>
4. <p> [EI] Z. Qiao, S. Yao, Y. Xie, <b>X. Zhu*</b>, et al. "Secure Medical Image Encryption via Dual-Channel Strategy and Digital Signature Verification", <b><i>IEEE SmartIoT</i></b>, 2025.</p>
5. <p> [CCF A] H. Zhang, J. Xie, Y. Lin, <b>X. Zhu*</b>, et al. "PoGL: A GAN-Based Proof of Federated Learning Framework to Defend Against Adversarial Attacks", <b><i>IEEE TIFS</i></b>, 2025.</p>
6. <p> [1区] W. Yu, S. Hu, L. Zhang, <b>X. Zhu*</b>, et al. "Sia-RSNet: A Siamese Network Model Integrating Resnet and Squeeze-and-Excitation for Human Activity Recognition", <b><i>IEEE TCCN</i></b>, 2025.</p>
7. <p> [CCF B] A. Hussain, <b>X. Zhu*</b>, et al. "AeroFlex-RL: A Reinforcement Learning Framework for Adaptive Resource Allocation in Future Wireless Systems", <b><i>IEEE TCOM</i></b>, 2025.</p>
8. <p> [JCR Q1] M. Zhang, X. He, <b>X. Zhu*</b>. "Lightweight Intelligent Localization for Internet of Robotic Things: Method, Theory, Application", <b><i>IEEE IoT Magazine</i></b>, 2025.</p>
9. <p> [CCF C] X. He, M. Zhang, <b>X. Zhu*</b>, et al. "A High-Precision CSI-Based Localization Framework with Kolmogorov-Arnold Network and Broad Learning", <b><i>IEEE ICPADS</i></b>, 2025.</p>
10. <p> [2区] S. Tian, T. Zhang, J. Liu, J. Wang, X. Wu, <b>X. Zhu</b>, et al. "Exploring the Role of Large Language Models in Cybersecurity: A Systematic Survey", <b><i>IEEE TNSE</i></b>, 2025.</p>


<!--
7. <p> [CCF C] A. Hussain, Y. Ding, <b>X. Zhu*</b>, A. Ullah. "DualStream-Attention Network for Optimizing Latency, Throughput, and SNR Prediction in Indoor Wireless Networks", <b><i>IEEE ICC</i></b>, 2025.</p>
<p> [CCF A] W. Chen, Z. Xie, F. Liu, R. Gao, <b>X. Zhu*</b>, G. Han. "Energy-Efficient Transmission Scheduling with Uncertainty-Aware Data Imputation for MHealth", <b><i>IEEE TMC</i></b>, 2025.</p>
<p> [CCF A] J. Dai, Z. Ji, Z. Xiong, <b>X. Zhu</b>, et al. "Modal Interaction and Gradient Calibration for Few-shot Class-Incremental Learning", <b><i>ACM MM</i></b>, 2025.</p>
<p> [CCF C] A. Hussain, <b>X. Zhu*</b>. "AnomSpectraNet: Spectrum-Based Anomaly Detection Using CSI and Attention Mechanisms for Elderly Health Monitoring", <b><i>ICONIP</i></b>, 2025.</p>
<p> [CCF A] W. Kong, Z. Ji, X. Zhang, <b>X. Zhu</b>, J. Liu. "FedFlow: Federated Parameter Matching via Optimal Probability Flows", <b><i>NeurIPS</i></b>, 2025.</p>
-->

## Grant Patents
1. <p><b>朱晓强</b>, 余旺, 胡思宇, 等. "基于小样本学习的人体姿态识别算法研究", 2025.</p>
2. <p><b>朱晓强</b>, 何炫锜, 张明博, 等. "一种基于Kolmogorov-Arnold网络和宽度学习系统的高精度CSI定位框架技术", 2025.</p>
3. <p><b>朱晓强</b>, 胡思宇, 余旺, 等. "一种基于深度强化学习的增强型OFDM-DCSK混沌加密方法", 2025.</p>
4. <p><b>朱晓强</b>, 胡思宇, 刘吉强, 等. "一种基于融合注意力机制原型神经网络的人体行为识别方法", No. 202411463529.7, 2024.</p>
5. <p><b>朱晓强</b>, 张明博, 鲁凌云, 等. "基于深度与宽度学习的CSI指纹数据库优化方法", No. 2024113941670, 2024.</p>
6. <p><b>朱晓强</b>, 刘吉强, 鲁凌云, 等. "一种基于强化学习的CSI指纹地图构建的路径规划方法", No. 202310874838.2, 2023.</p>
7. <p><b>朱晓强</b>, 刘吉强, 张大林, 等. "一种基于模仿学习的智能自适应CSI指纹地图更新方法", No. 202310775481.2, 2023.</p>
8. <p> 邱铁, <b>朱晓强</b>, 曲雯毓. "一种基于CSI图像的增量式智能室内定位方法", No. CN113691940A, 2022.09.27.</p>
9. <p> 邱铁, <b>朱晓强</b>, 曲雯毓. "一种基于宽度学习的快速室内指纹定位方法", No. CN111929641A, 2022.08.09</p>
10. <p> 邱铁, 黄慧娟, 周晓波, 张朝昆, <b>朱晓强</b>. "基于信道状态信息的心率监测方法及呼吸事件检测方法", No. 202210661544.</p>
11. <p> 邱铁, 吴琛, 赵来平, 李克秋, <b>朱晓强</b>. "一种基于集成宽度学习的快速高精度室内指纹定位方法", No. 202110866814.</p>

# 🎖 Honors and Awards
- *2023* National Funding Postdoctoral Researcher Program, China Postdoctoral Science Foundation
- *2023* Youth Talent Cultivation Program, Beijing Jiaotong University
- *2021* China Scholarship Council, Ministry of Education of the People’s Republic of China
- *2020* Outstanding Volunteer, 2020 IEEE International Conference on Smart Internet of Things
- *2019* Outstanding Volunteer, 2019 IEEE International Conference on Smart Internet of Things
- *2019* 1st Award Postgraduate Scholarship, Tianjin University
- *2018* Outstanding Postgraduate Student, Dalian University of Technology
- *2017* 1st Award Postgraduate Scholarship, Dalian University of Technology
- *2016* Outstanding Postgraduate Student, Education funding item of Liaoning province
- *2015* National Inspirational Scholarship, Ministry of Education of the People’s Republic of China

# 💻 Academic Services
## Guest Editor
- Journal on Wireless Communications and Networking, <a href="https://www.springeropen.com/collections/imen?utm_medium=email&utm_source=generic&utm_content=null&utm_term=null&utm_campaign=APSR13638_CON1_GL_PHSS_03HEQ_fhdiacjebi">Special Issue: Integrating Large Models and Edge Sensing in Next Generation Networks.</a>

## Reviewer
- IEEE Transactions on Mobile Computing, IEEE Journal on Selected Areas in Communications, IEEE/ACM Transactions on Networking, IEEE Transactions on Computers, IEEE Transactions on Wireless Communications, IEEE Transactions on Cognitive Communications and Networking, IEEE Internet of Things Journal, IEEE Transactions on Communications, IEEE Communications Letters, IEEE Transactions on Network Science and Engineering, IEEE Transactions on Consumer Electronics, IEEE MultiMedia, Information Sciences, Nonlinear Dynamic, IET Signal Processing, Optics and Lasers in Engineering, The Journal of Supercomputing, Peer-to-Peer Networking and Applications, China Communications, Computer Science, SCIENCE CHINA Information Sciences.
- IEEE SmartIoT' 2019‑2022, IEEE CSCWD' 2020‑2021, IEEE IWQoS' 2020, IEEE iThings' 2023, DASFAA' 2025, GLOBECOM' 2025.

## PC Member and Session Chair
- IEEE CSCWD 2020, IEEE SmartIoT 2019

# 🏫 Supervising and Mentoring Activities
- Data Structure, M310002B
- Professional Course Comprehensive Practical Training I, P210001B
- Cloud Computing and Big Data Platform Analysis, M510014B
- Software Testing, M310007B

# 🧑‍💻 Students
## 2023级硕
- 张明博 (录用：IEEE MSN, IEEE ICC workshop, 专利 * 1。在审：IEEE IoTM)
- 胡思宇 (录用：IEEE MSN, ICONIP, 专利 * 2。)
- 任城仪 (录用：《软件导刊》)
- 张皓文 (录用：《中国科学：信息科学》, 《信息网络安全》。在审：IEEE TIFS)
  
## 2023级本
- 贾佩伦
- 徐滔
- 章步峰
- 汪雨辰
- 林彦孜
- 方首岳
- 谢建轩
- 庄浩然
  
## 2022级本
- 余旺（专利 * 1, 在审：IEEE TCCN）
- 何炫绮（专利 * 1, 在审：IEEE ICPADS）

<!-- # 💻 My blog -->
