/**
 * 236. Lowest Common Ancestor of a Binary Tree.
 *
 * @see https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 * @see https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/932/
 */

// noinspection ES6ConvertVarToLetConst

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
  let target = null

  const dfs = function (root, p, q) {
    if (!root) {
      return 0
    }

    const leftCount = dfs(root.left, p, q)
    const rightCount = dfs(root.right, p, q)

    const match = root === p || root === q

    const rootCount = match + leftCount + rightCount
    // Since the recursion will go through the tree, So for Lowest Common Ancestor
    // we should set it only once to the first matched node.
    if (rootCount === 2 && !target) {
      target = root
    }

    return rootCount
  }

  dfs(root, p, q)

  return target
};
