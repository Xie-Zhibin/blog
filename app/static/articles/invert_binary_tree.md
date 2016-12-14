# 二叉树翻转

故事是这样的：
> Homebrew 的作者 Max Howell 在 twitter 上发表了如下一内容
> ```Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.```

> 大意是，Max Howell 去 Google 面试，面试官说：虽然在 Google 有 90% 的工程师用你写的 Homebrew，但是你居然不能在白板上写出翻转二叉树的代码，所以滚蛋吧。

> 题目参考Leetcode中的[invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

***
先看二叉树的定义(wikipedia)：
> 在计算机科学中，二叉树（英语：Binary tree）是每个节点最多有两个子树的树结构。通常子树被称作“左子树”（left subtree）和“右子树”（right subtree）。二叉树常被用于实现二叉查找树和二元堆积。
二叉树的每个节点至多只有二棵子树(不存在度大于2的节点)，二叉树的子树有左右之分，次序不能颠倒。二叉树的第i层至多有 {\displaystyle 2^{i-1}} 2^{i-1}个节点；深度为k的二叉树至多共有 {\displaystyle 2^{\begin{aligned}k+1\end{aligned}}-1} {\displaystyle 2^{\begin{aligned}k+1\end{aligned}}-1}个节点；对任何一棵二叉树T，如果其终端节点数为 {\displaystyle n_{0}} n_0，度为2的节点数为 {\displaystyle n_{2}} n_{2}，则 {\displaystyle n_{0}=n_{2}+1} n_0=n_2+1。
一棵深度为k，且有 {\displaystyle 2^{\begin{aligned}k+1\end{aligned}}-1} {\displaystyle 2^{\begin{aligned}k+1\end{aligned}}-1}个节点称之为满二叉树；深度为k，有n个节点的二叉树，当且仅当其每一个节点都与深度为k的满二叉树中，序号为1至n的节点对应时，称之为完全二叉树。
与树不同，树的节点个数至少为1，而二叉树的节点个数可以为0；树中节点的最大度数没有限制，而二叉树节点的最大度数为2；树的节点无左、右之分，而二叉树的节点有左、右之分。

> ---------------

> 图论中的定义:
二叉树是一个连通的无环图，并且每一个顶点的度不大于3。有根二叉树还要满足根节点的度不大于2。有了根节点之后，每个顶点定义了唯一的父节点，和最多2个子节点。然而，没有足够的信息来区分左节点和右节点。如果不考虑连通性，允许图中有多个连通分量，这样的结构叫做森林。

关于二叉树的其余细节参考数据结构相关书籍资料

****

## 翻转二叉树
> 翻转二叉树即交换所有左右子树的位置, 自顶向下直到所有树叶被交换。以递归的形式实现比较容易理解.

二叉树翻转的递归实现(Java):
```
public class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) {  // 树叶
            return null;
        }
        // 交换左右子树
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
		// 递归交换
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
}
```