[目录](#content)
- [第一章 绪论](#chapter1)
    - [1.1. 什么是计算](#1-1)
    - [1.2. 什么是好计算](#1-2)
    - [1.3. 如何衡量DSA的时间成本](#1-3)
        - [1.3.1. 衡量时间成本的三种方法](#1-3-1)
        - [1.3.2. 如何计算T（n）](#1-3-2)
    - [1.4. 大O记号法：渐进复杂度](#1-4)
        - [1.4.1. 几种主要的复杂度](#1-4-1)
        - [1.4.2. 复杂度分析的方法](#1-4-2)
            - [1.4.2.1. 迭代](#1-4-2-1)
              - [1.4.2.1.1. 级数计算](#1-4-2-1-1)
              - [1.4.2.1.2. 图形分析](#1-4-2-1-2)
            - [1.4.2.2. 递归](#1-4-2-2)
                - [1.4.2.2.1. 递归跟踪](#1-4-2-2-1)
                - [1.4.2.2.2. 递推方程](#1-4-2-2-2)
        - [1.4.3. 递归的优缺点](#1-4-3)
        - [1.4.4. 用动态规划提高计算效率](#1-4-4)
- [第二章 向量](#chapter2)
    - [2.1. 向量的构造与析构](#2-1)
      - [2.1.1. 复制](#2-1-1)
      - [2.1.2. 扩充](#2-1-2)
    - [2.2. 无序向量的操作接口](#2-2)
        - [2.2.1. 插入](#2-2-1)
        - [2.2.2. 区间删除](#2-2-2)
        - [2.2.3. 查找](#2-2-3)
        - [2.2.4. 唯一化](#2-2-4)
    - [2.3. 有序向量的操作接口](#2-3)
        - [2.3.1. 去重](#2-3-1)
        - [2.3.2. 查找](#2-3-2)
            - [2.3.2.1. 版本A：初始二分查找](#2-3-2-1)
            - [2.3.2.2. 版本B：Fibonacci查找](#2-3-2-2)
            - [2.3.2.3. 版本C：二分查找改进](#2-3-2-3)
            - [2.3.2.4. 版本D：插值查找](#2-3-2-4)
    - [2.4. 从无序到有序：排序算法](#2-4)
        - [2.4.1. 起泡排序](#2-4-1)
        - [2.4.2. 归并排序](#2-4-2)
- [第三章 列表](#chapter3)
  - [3.1. 列表的构造](#3-1)
  - [3.2. 无序列表的操作接口](#3-2)
    - [3.2.1. 循秩访问](#3-2-1)
    - [3.2.2. 查找](#3-2-2)
    - [3.2.3. 插入](#3-2-3)
    - [3.2.4. 删除](#3-2-4)
    - [3.2.5. 唯一化](#3-2-5)
  - [3.3. 有序列表的操作接口](#3-3)
    - [3.3.1. 唯一化](#3-3-1)
    - [3.3.2. 查找](#3-3-2)
  - [3.4. 无序到有序：排序算法](#3-4)
    - [3.4.1. 选择排序](#3-4-1)
    - [3.4.2. 插入排序](#3-4-2)
    - [*3.4.3. 补充知识：逆序对](#3-4-3)
- [第四章 栈与队列](#chapter4)
  - [4.1. 栈的应用1：进制转换](#4-1)
  - [4.2. 栈的应用2：括号匹配](#4-2)
  - [4.3. 栈的应用3：栈混洗](#4-3)
  - [4.4. 栈的应用4：中缀表达式求值](#4-4)
  - [4.5. 栈的应用5：逆波兰表达式](#4-5)
- [第七章 二叉搜索树](#chapter7)
- [第八章 高级搜索树](#chapter8)
- [第九章 词典](#chapter9)
- [第十章 优先级队列](#chapter10)
- [第十一章 串比对](#chapter11)


<a name='chapter1'><h2>第一章 绪论</h2></a>

![](./picture/01.jpg)

![](./picture/02.jpg)

![](./picture/03.jpg)

![](./picture/04.jpg)

![](./picture/05.jpg)

![](./picture/06.jpg)

![](./picture/07.jpg)

![](./picture/08.jpg)

![](./picture/09.jpg)

![](./picture/10.jpg)

![](./picture/11.jpg)

<a name='chapter2'><h2>第二章 向量</h2></a>

![](./picture/12.jpg)

![](./picture/13.jpg)

![](./picture/14.jpg)

![](./picture/15.jpg)

![](./picture/16.jpg)

![](./picture/17.jpg)

![](./picture/18.jpg)

![](./picture/19.jpg)

![](./picture/20.jpg)

![](./picture/21.jpg)

<a name='chapter3'><h2>第三章 列表</h2></a>

![](./picture/22.jpg)

![](./picture/23.jpg)

![](./picture/24.jpg)

![](./picture/25.jpg)

![](./picture/26.jpg)

![](./picture/27.jpg)

![](./picture/28.jpg)

![](./picture/29.jpg)

<a name='chapter4'><h2>第四章 栈与队列</h2></a>

![](./picture/30.jpg)

![](./picture/31.jpg)

![](./picture/32.jpg)

![](./picture/33.jpg)

![](./picture/34.jpg)

![](./picture/35.jpg)

<a name='chapter7'><h2>第七章 二叉搜索树</h2></a>

![](./picture/36.jpg)

![](./picture/37.jpg)

![](./picture/38.jpg)

![](./picture/39.jpg)

![](./picture/40.jpg)

![](./picture/41.jpg)

![](./picture/42.jpg)

![](./picture/43.jpg)

![](./picture/44.jpg)

![](./picture/45.jpg)

![](./picture/46.jpg)

![](./picture/47.jpg)

![](./picture/48.jpg)

![](./picture/49.jpg)

![](./picture/50.jpg)

![](./picture/51.jpg)

![](./picture/52.jpg)

![](./picture/53.jpg)

![](./picture/54.jpg)

![](./picture/55.jpg)

<a name='chapter8'><h2>第八章 高级搜索树</h2></a>

![](./picture/56.jpg)

![](./picture/57.jpg)

![](./picture/58.jpg)

![](./picture/59.jpg)

![](./picture/60.jpg)

![](./picture/61.jpg)

![](./picture/62.jpg)

![](./picture/63.jpg)

![](./picture/64.jpg)

![](./picture/65.jpg)

![](./picture/66.jpg)

![](./picture/67.jpg)

![](./picture/68.jpg)

![](./picture/69.jpg)

![](./picture/70.jpg)

![](./picture/71.jpg)

![](./picture/72.jpg)

![](./picture/73.jpg)

![](./picture/74.jpg)

![](./picture/75.jpg)

![](./picture/76.jpg)

![](./picture/77.jpg)

![](./picture/78.jpg)

![](./picture/79.jpg)

![](./picture/80.jpg)

![](./picture/81.jpg)

![](./picture/82.jpg)

![](./picture/83.jpg)

![](./picture/84.jpg)

![](./picture/85.jpg)

<a name='chapter9'><h2>第九章 词典</h2></a>

![](./picture/86.jpg)

![](./picture/87.jpg)

![](./picture/88.jpg)

![](./picture/89.jpg)

![](./picture/90.jpg)

![](./picture/91.jpg)

![](./picture/92.jpg)

![](./picture/93.jpg)

![](./picture/94.jpg)

<a name='chapter10'><h2>第十章 优先级队列</h2></a>

![](./picture/95.jpg)

![](./picture/96.jpg)

![](./picture/97.jpg)

![](./picture/98.jpg)

![](./picture/99.jpg)

![](./picture/100.jpg)

![](./picture/101.jpg)

![](./picture/102.jpg)

![](./picture/103.jpg)

![](./picture/104.jpg)

![](./picture/105.jpg)

![](./picture/106.jpg)

![](./picture/107.jpg)

![](./picture/108.jpg)

![](./picture/109.jpg)

![](./picture/110.jpg)

<a name='chapter11'><h2>第十一章 串比对</h2></a>

![](./picture/111.jpg)

![](./picture/112.jpg)

![](./picture/113.jpg)

![](./picture/114.jpg)

![](./picture/115.jpg)

![](./picture/116.jpg)

![](./picture/117.jpg)

![](./picture/118.jpg)

![](./picture/119.jpg)

![](./picture/120.jpg)

![](./picture/121.jpg)

![](./picture/122.jpg)

![](./picture/123.jpg)

![](./picture/124.jpg)

![](./picture/125.jpg)

![](./picture/126.jpg)

![](./picture/127.jpg)

![](./picture/128.jpg)

![](./picture/129.jpg)

![](./picture/130.jpg)

![](./picture/131.jpg)

![](./picture/132.jpg)

![](./picture/133.jpg)

![](./picture/134.jpg)

![](./picture/135.jpg)

![](./picture/136.jpg)

![](./picture/137.jpg)

![](./picture/138.jpg)

![](./picture/139.jpg)

![](./picture/140.jpg)


